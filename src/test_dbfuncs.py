import unittest
import sqlite3
from dbfuncs import add_recipe
from recipe import Recipe

class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON;")

        #Creates Ingredient Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Ingredient (
            ID INTEGER,
            Name Text,
            Ammount FLOAT,
            Unit Text,
            PRIMARY KEY(ID)
            ) 
            """
        )

        #Creates Recipe Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Recipe (
            ID INTEGER, 
            Name TEXT UNIQUE NOT NULL,
            Category TEXT,
            PRIMARY KEY(ID)
            );
            """
            )

        #Creates Instruction Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Instruction (
            ID INTEGER,
            RecipeID INTEGER,
            Description TEXT NOT NULL,
            StepNumber INTEGER,
            PRIMARY KEY(ID),
            FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
            )
            """
        )

        #Creates a table that links recipes to ingredients
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Recipe_Ingredient_Link (
            RecipeID INTEGER,
            IngredientID INTEGER,
            FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),
            FOREIGN KEY(IngredientID) REFERENCES Ingredient(ID)
            )
            """
        ) 

        self.conn.commit()
    
    def tearDown(self):
        self.conn.close()
    
    def test_add_recipe(self):
        recp = Recipe("PIZZA", "ITALAIN")
        id = add_recipe(self.conn, recp)

        self.cur.execute("SELECT * FROM Recipe WHERE ID = ?", (id,))
        result = self.cur.fetchone()

        self.assertEqual(result[1], "PIZZA")
    
        

if __name__ == '__main__':
    unittest.main()