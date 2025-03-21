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
    cur.execute(f"SELECT ID FROM Ingredient WHERE Name IN ({",".join(["?"] * len(names))})", names)
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

    conn.commit()
    conn.close()

def add_instructions_list(conn, recp_ID, instruct_list):
    data = []
    for instruct in instruct_list:
        data.append({"RecipeID": recp_ID, "Description": instruct.desc})

    cur = conn.cursor()

    cur.executemany("INSERT INTO Instruction (RecipeID, Description) VALUES (:RecipeID, :Description)", data)

    conn.commit()
    conn.close()