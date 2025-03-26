import sqlite3
from recipe import Recipe, Ingredient, Instruction

def initialize_database():
    #Creates database / Connnection
    conn = sqlite3.connect("recipe_database.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    #Creates Ingredient Table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Ingredient (
        ID INTEGER,
        Name Text,
        Ammount REAL,
        Unit Text,
        PRIMARY KEY(ID)
        ) 
        """
    )

    #Creates Recipe Table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Recipe (
        ID INTEGER, 
        Name TEXT UNIQUE NOT NULL,
        Category TEXT,
        PRIMARY KEY(ID ASC)
        );
        """
        )

    #Creates Instruction Table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Instruction (
        ID INTEGER,
        RecipeID INTEGER,
        Description TEXT NOT NULL,
        StepNumber INTEGER,
        PRIMARY KEY(ID ASC),
        FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
        )
        """
    )

    #Creates a table that links recipes to ingredients
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Recipe_Ingredient_Link (
        RecipeID INTEGER,
        IngredientID INTEGER,
        FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),
        FOREIGN KEY(IngredientID) REFERENCES Ingredient(ID)
        )
         """
    )

    #Closes DB connection
    conn.close()

#Fuction adds a list of ingredients and returns the ids in a list
def add_ingredients(conn, ing_list):
    data_ar = []
    for ing in ing_list:
        data_ar.append({"Name": ing.name, "Ammount": ing.ammount, "Unit": ing.unit})

    names = [data["Name"] for data in data_ar]
    names = tuple(names)

    cur = conn.cursor()

    cur.executemany("INSERT INTO Ingredient (Name, Ammount, Unit) VALUES (:Name, :Ammount, :Unit)", data_ar)
    cur.execute(f"SELECT ID FROM Ingredient WHERE Name IN ({', '.join(['?'] * len(names))})", names)
    id_list = [row[0] for row in cur.fetchall()]

    return id_list

#adds a recipe to table
def add_recipe(conn, recp):
    data = {"Name": recp.name, "Category": recp.category}
    cur = conn.cursor()

    cur.execute("INSERT INTO Recipe (Name, Category) VALUES (:Name, :Category)", data)
    recipe_id = cur.lastrowid

    return int(recipe_id)

#adds the link between ingredients and a recipe
def add_ingredient_recipe_link(conn, resp_id, ingred_id_list):
    data = []
    for igred_id in ingred_id_list:
        data.append({"RecipeID": resp_id, "IngredientID": igred_id})

    cur = conn.cursor()

    cur.executemany("INSERT INTO Recipe_Ingredient_Link (RecipeID, IngredientID) VALUES (:RecipeID, :IngredientID)", data)


def add_instructions_list(conn, recp_ID, instruct_list):
    data = []
    for instruct in instruct_list:
        data.append({"RecipeID": recp_ID, "Description": instruct.desc, "StepNumber": instruct.step_number})

    cur = conn.cursor()

    cur.executemany("INSERT INTO Instruction (RecipeID, Description, StepNumber) VALUES (:RecipeID, :Description, :StepNumber)", data)

#Gets the names of recipes from the DB
def get_recipe_list(conn):
    cur = conn.cursor()
    
    cur.execute("SELECT Name FROM Recipe")
    recp_name_list = [row[0] for row in cur.fetchall()]

    return recp_name_list

#Gets complete recipe based off name
def get_complete_recipe(conn, recp_name):
    cur = conn.cursor()

    cur.execute("SELECT * FROM Recipe WHERE Name = ?", (recp_name,))
    result = cur.fetchone()

    id = result[0]
    name = result[1]
    catagory = result[2]

    cur.execute("SELECT Description FROM Instruction WHERE ID = ? ORDER BY StepNumber", (id,))
    desc_list = [row[0] for row in cur.fetchall()]

    r = Recipe(name, catagory)

    for desc in desc_list:
        instruction = Instruction(desc)
        r.append_instruction(instruction)

    cur.execute("""SELECT * FROM INGREDIENT I 
                INNER JOIN Recipe_Ingredient_Link RIL ON I.ID = RIL.IngredientID
                WHERE RIL.RecipeID = ?""", (id,))
    
    result = cur.fetchall()

    for i in range(len(result)):
        ing = Ingredient(result[i][1], result[i][2], result[i][3])
        r.add_ingredient(ing)

    return r