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

    def test_instruction(self):
        instruc = Instruction("Take 5 and relax")
        self.assertEqual(instruc.desc, "Take 5 and relax")

    def test_bad_instruction(self):
        with self.assertRaises(TypeError):
            instuc = Instruction(4)

    def test_insertion(self):
        r =Recipe("Pizza", "Intalian")
        ins1 = Instruction("Mix flour and water")
        r.append_instruction(ins1)
        self.assertEqual(len(r.instructions), 1)
        self.assertEqual(r.instructions[0].step_number, 1)

    def test_instuction_insertion(self):
        r =Recipe("Pizza", "Intalian")
        ins1 = Instruction("Mix flour and water")
        ins2 = Instruction("Add yeast while mixing")
        ins3 = Instruction("Mix until fully incorperated")
        r.append_instruction(ins1)
        r.append_instruction(ins3)
        r.insert_instruction(ins2, 2)

        self.assertEqual(r.instructions[1].step_number, 2)

if __name__ == '__main__':
    unittest.main()