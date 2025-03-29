import unittest
import sqlite3
from dbfuncs import (add_recipe, 
                     add_ingredients,
                     add_ingredient_recipe_link,
                     add_instructions_list,
                     get_recipe_list,
                     get_complete_recipe)
from recipe import Recipe, Ingredient, Instruction

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

        self.recp = Recipe("PIZZA", "ITALIAN")
        self.recp2 = Recipe("Popcorn", "American")
        self.ingr_list = [Ingredient("Flour", 2, "Cups"), Ingredient("Water", 2, "Cups")]
        self.instruct_list = [Instruction("Mix flour and water"), Instruction("Add yeast"),
                              Instruction("Mix all together"), Instruction("Knead until firm")]
        
        for instuction in self.instruct_list:
            self.recp.append_instruction(instuction)
    
    def tearDown(self):
        self.conn.close()
    
    def test_add_recipe(self):
        id = add_recipe(self.conn, self.recp)

        self.cur.execute("SELECT * FROM Recipe WHERE ID = ?", (id,))
        result = self.cur.fetchone()

        self.assertEqual(result[1], "PIZZA")
        self.assertEqual(result[2], "ITALIAN")

    def test_add_ingredients(self):
        id_list = add_ingredients(self.conn, self.ingr_list)
        id_list = tuple(id_list)

        self.cur.execute(f"SELECT * FROM Ingredient WHERE ID IN ({', '.join(['?'] * len(id_list))})", id_list)
        result = self.cur.fetchall()

        self.assertEqual(result[0][1], "FLOUR")
        self.assertEqual(result[1][1], "WATER")

        self.assertEqual(result[0][2], 2)
        self.assertEqual(result[1][2], 2)  

        self.assertEqual(result[0][3], "CUPS")
        self.assertEqual(result[1][3], "CUPS")

    def test_ing_rec_link(self):
        recp_id = add_recipe(self.conn, self.recp)
        ing_ids = add_ingredients(self.conn, self.ingr_list)

        add_ingredient_recipe_link(self.conn, recp_id, ing_ids)

        self.cur.execute("SELECT * FROM Recipe_Ingredient_Link WHERE RecipeID = ?", (recp_id,))
        result = self.cur.fetchall()

        self.assertIsNotNone(result[0][0])

        self.assertEqual(result[0][0], recp_id)
        self.assertEqual(result[1][0], recp_id)

        self.assertEqual(result[0][1], ing_ids[0])

    def test_add_instructions_list(self):
        id = add_recipe(self.conn, self.recp)
        add_instructions_list(self.conn, id, self.recp.instructions)

        self.cur.execute("SELECT * FROM Instruction WHERE RecipeID = ?", (id,))
        result = self.cur.fetchall()

        self.assertIsNotNone(result)
        self.assertEqual(result[0][1], id)
        self.assertEqual(result[0][2], self.recp.instructions[0].desc)
        self.assertEqual(result[1][2], self.recp.instructions[1].desc)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[3][3], 4)

    def test_get_recipe_list(self):
        add_recipe(self.conn, self.recp)
        add_recipe(self.conn, self.recp2)

        recp_name_list = get_recipe_list(self.conn)

        self.assertIsNotNone(recp_name_list)
        self.assertEqual(recp_name_list[0], "PIZZA")
        self.assertEqual(recp_name_list[1], "POPCORN")

    def test_get_complete_recipe(self):
        recp_id = add_recipe(self.conn, self.recp)
        ing_id_list = add_ingredients(self.conn, self.ingr_list)
        add_ingredient_recipe_link(self.conn, recp_id, ing_id_list)
        add_instructions_list(self.conn, recp_id, self.recp.instructions)

        r = get_complete_recipe(self.conn, "PIZZA")

        self.assertEqual(r.name, "PIZZA")
        self.assertEqual(r.category, "ITALIAN")
        self.assertIsNotNone(r.ingredients)
        self.assertIsNotNone(r.instructions)
        self.assertEqual(len(r.ingredients), 2)
        self.assertEqual(len(r.instructions), 4)
        self.assertEqual(r.instructions[0].desc, "Mix flour and water")
        self.assertEqual(r.instructions[1].desc, "Add yeast")
        self.assertEqual(r.instructions[2].desc, "Mix all together")
        self.assertEqual(r.instructions[3].desc, "Knead until firm")

if __name__ == '__main__':
    unittest.main()