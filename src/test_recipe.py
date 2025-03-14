import unittest

from recipe import(
    Recipe, 
    Ingredient, 
    Instruction,)

class TestRescipeCreation(unittest.TestCase):

    def test_recipe_names(self):
        recipe = Recipe("pizza", "Italian")
        self.assertEqual(recipe.name, "PIZZA")
        self.assertEqual(recipe.category, "ITALIAN")

    def test_ingredient_name(self):
        ingredient = Ingredient("pepper", 4, "grams")
        self.assertEqual(ingredient.name, "PEPPER")
        self.assertEqual(ingredient.ammount, 4)
        self.assertEqual(ingredient.unit, "GRAMS")

    def test_bad_ingredient(self):
        with self.assertRaises(TypeError):
            ing = Ingredient(4, 4, "grams")
        with self.assertRaises(TypeError):
            ing = Ingredient("salt", "four", "tsp")
        with self.assertRaises(TypeError):
            ing = Ingredient("salt", 4, 5)

if __name__ == '__main__':
    unittest.main()