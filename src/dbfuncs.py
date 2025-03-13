import sqlite3

def initialize_database():
    #Creats database / Connnection
    conn = sqlite3.connect("recipe_database.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    cur.execute(
        """CREATE TABLE IF NOT EXIST Ingredient (
        ID INTEGER,
        Name Text
        PRIMARY KEY(ID, ASC)
        ) 
        """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXIST Recipes (
        ID INTEGER, 
        Name TEXT UNIQUE NOT NULL,
        Catagory TEXT,
        PRIMARY KEY(ID, ASC)
        );
        """
        )

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

    cur.execute(
        """CREATE TABLE IF NOT EXIST Recipe_Ingredient_Link (
        RecipeID INTEGER,
        IngredientID INTEGER
        FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
        FOREIGN KEY(IngredientID) REFERENCES Ingredient(ID)
        )
         """
    )


    conn.close()