import sqlite3

def initialize_database():
    #Creates database / Connnection
    conn = sqlite3.connect("recipe_database.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    #Creates Ingredient Table
    cur.execute(
        """CREATE TABLE IF NOT EXIST Ingredient (
        ID INTEGER,
        Name Text
        PRIMARY KEY(ID, ASC)
        ) 
        """
    )

    #Creates Recipe Table
    cur.execute(
        """CREATE TABLE IF NOT EXIST Recipe (
        ID INTEGER, 
        Name TEXT UNIQUE NOT NULL,
        Catagory TEXT,
        PRIMARY KEY(ID, ASC)
        );
        """
        )

    #Creates Instruction Table
    cur.execute(
        """CREATE TABLE IF NOT EXIST Instruction (
        ID INTEGER,
        RecipeID INTEGER,
        Name TEXT NOT NULL,
        StepNumber INTEGER
        PRIMARY KEY(ID, ASC)
        FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
        )
        """
    )

    #Creates a table that links recipes to ingredients
    cur.execute(
        """CREATE TABLE IF NOT EXIST Recipe_Ingredient_Link (
        RecipeID INTEGER,
        IngredientID INTEGER
        FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
        FOREIGN KEY(IngredientID) REFERENCES Ingredient(ID)
        )
         """
    )

    #Closes DB connection
    conn.close()