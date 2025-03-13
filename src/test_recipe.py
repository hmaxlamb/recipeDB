import unittest
import recipe

class TestRescipeCreation(unittest.TestCase):

    def test_recipe_name(self):
        recipe = Recipe("pizza", "Itlian")
        self.assertEqual(recipe.name, "PIZZA")

if __name__ == '__main__':
    unittest.main()