import unittest
import sqlite3
from dbfuncs import add_recipe, add_ingredients
from recipe import Recipe, Ingredient

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
            Ammount REAL,
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

        self.recp = Recipe("PIZZA", "ITALAIN")
        self.ingr_list = [Ingredient("Flour", 2, "Cups"), Ingredient("Water", 2, "Cups")]
    
    def tearDown(self):
        self.conn.close()
    
    def test_add_recipe(self):
        id = add_recipe(self.conn, self.recp)

        self.cur.execute("SELECT * FROM Recipe WHERE ID = ?", (id,))
        result = self.cur.fetchone()

        self.assertEqual(result[1], "PIZZA")

    def test_add_ingredients(self):
        id_list = add_ingredients(self.conn, self.ingr_list)
        id_list = tuple(id_list)

        self.cur.execute(f"SELECT * FROM Ingredient WHERE ID IN ({', '.join(['?'] * len(id_list))})", id_list)
        result = self.cur.fetchall()
        print(result)

        self.assertEqual(result[0][1], "FLOUR")
    
        

if __name__ == '__main__':
    unittest.main()