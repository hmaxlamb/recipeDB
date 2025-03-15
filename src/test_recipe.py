import unittest

from recipe import(
    Recipe, 
    Ingredient, 
    Instruction,
    format_instruction_list_for_print
    )

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

    def test_instruction_insertion(self):
        r =Recipe("Pizza", "Intalian")
        ins1 = Instruction("Mix flour and water")
        ins2 = Instruction("Add yeast while mixing")
        ins3 = Instruction("Mix until fully incorperated")
        insX = Instruction("Stop and take a break")
        insY = Instruction("Touch Grass")
        r.append_instruction(ins1)
        r.append_instruction(ins3)
        r.insert_instruction(ins2, 2)
        self.assertEqual(r.instructions[1].step_number, 2)

        r.insert_instruction(insX, 1)
        self.assertEqual(r.instructions[3].step_number, 4)
        r.insert_instruction(insY, 5)

    def bad_instruction_insertion(self):
        r =Recipe("Pizza", "Intalian")
        ins1 = Instruction("Mix flour and water")
        ins2 = Instruction("Add yeast while mixing")
        ins3 = Instruction("Mix until fully incorperated")
        r.append_instruction(ins1)
        r.append_instruction(ins3)

        with self.assertRaises(IndexError):
            r.insert_instruction(ins2, 4)

    def test_format_instruction_list_for_print(self):
        list = ["Mix Flour", "Bake Cookies"]
        fmt_string = format_instruction_list_for_print(list)
        self.assertEqual(fmt_string,"""1. Mix Flour\n2. Bake Cookies""")

if __name__ == '__main__':
    unittest.main()