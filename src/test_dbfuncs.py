import unittest
import dbfuncs

class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        
        self.conn = sqlite3.connect(":memory:")
        self.cur = conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON;")

        #Creates Ingredient Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXIST Ingredient (
            ID INTEGER,
            Name Text,
            Ammount FLOAT,
            Unit Text,
            PRIMARY KEY(ID, ASC)
            ) 
            """
        )

        #Creates Recipe Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXIST Recipe (
            ID INTEGER, 
            Name TEXT UNIQUE NOT NULL,
            Category TEXT,
            PRIMARY KEY(ID, ASC)
            );
            """
            )

        #Creates Instruction Table
        self.cur.execute(
            """CREATE TABLE IF NOT EXIST Instruction (
            ID INTEGER,
            RecipeID INTEGER,
            Description TEXT NOT NULL,
            StepNumber INTEGER
            PRIMARY KEY(ID, ASC)
            FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
            )
            """
        )

        #Creates a table that links recipes to ingredients
        self.cur.execute(
            """CREATE TABLE IF NOT EXIST Recipe_Ingredient_Link (
            RecipeID INTEGER,
            IngredientID INTEGER
            FOREIGN KEY(RecipeID) REFERENCES Recipe(ID)
            FOREIGN KEY(IngredientID) REFERENCES Ingredient(ID)
            )
            """
        )
    
    def tearDown(self):
        self.conn.close()

    def test_add_recipe(self):
        pass

if __name__ == '__main__':
    unittest.main()