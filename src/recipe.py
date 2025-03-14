import sqlite3
import dbfuncs

class Recipe:
   
   #init fuction to make recipe class
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name should be a string!")
        if not isinstance(category, str):
            raise TypeError("catagory should be a string!")

        self.name = name.upper()
        self.category = category.upper()
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(self, ingredient)

    #Adds instruction to the end of the list
    def append_instruction(self, instruction):
        instruction.step_number = len(self.instructions) + 1
        self.instructions.append(instruction)

    #This fuction will insert the instrunction and -
    #move the current instuction at the index  to the left
    def insert_instruction(self, instruction, step_num):
        if step_num > len(self.instructions) + 1:
            raise IndexError("Step number can't be greater than total size")
        index = step_num - 1
        instruction.step_number = step_num
        self.instructions.insert(index, instruction)
        for i in range(index + 1, len(self.instructions)):
            self.instructions[i].step_number += 1

        

class Ingredient:
    def __init__(self, name, ammount, unit=None):
        if not isinstance(name, str):
            raise TypeError("name must be string!")
        if isinstance(ammount, int):
            self.ammount = float(ammount)
        elif isinstance(ammount, float):
            self.ammount = ammount
        else:
            raise TypeError("ammount must be int or float!")
        if unit:
            if not isinstance(unit, str):
                raise TypeError("unit must be string!")
            self.unit = unit.upper()
        self.name = name.upper()
        
        


class Instruction:
    def __init__(self, desc):
        if not isinstance(desc, str):
            raise TypeError("The description must be a string!")
        self.desc = desc
        self.step_number = None

#This function prompts the recipe creation and returns a recipe
def prompt_recipe():
    recipe_name_not_made = True
    catagory_name_not_made = True
    while (recipe_name_not_made):
        r_name = input("Please name recipe")
        confirm = input(f"Please confirm name: {r_name} (Yes/No)")
        confirm.upper()
        if (confirm == "YES"):
            recipe_name_not_made = False
        elif (confirm == "NO"):
           print("Bruh")
           continue
        else:
           raise ValueError("Must be yes or no")
        
    while(catagory_name_not_made):
        c_name = input("Please Input Catagory")
        confirm = input(f"Please confirm catagory: {c_name} (Yes/No)")
        confirm.upper()
        if (confirm == "Yes"):
            print(f"Catagory Name: {c_name}")
            catagory_name_not_made = False
        elif (confirm == "NO"):
            print("Bruh")
            continue
        else:
            raise ValueError("Must be yes or no")
        
    r = Recipe(r_name, c_name)

    return r

#function that quickly gathers a list of instructions
#to import to a recipe, the recipe must be empty
def create_list_of_instuctions(recipe):
    if (len(recipe.instructions) == 0):
        raise ValueError("recipe must be empty")
    is_done = False
    instruction_lists = []
    ins = None
    count = 0
    while(not is_done):
        ins = None
        is_instruction_made = False
        count += 1
        while(not is_instruction_made):
            ins = input(f"Please input instruction number {count}")
            confirm = input("Is the following instruction correct:/n{ins}")
            confirm.upper()
            if (confirm == "YES"):
                instruction_lists.append(ins)
                is_instruction_made = True
            elif (confirm == "NO"):
                continue
            else:
                raise ValueError("Must be yes or no")
        outer_confirm = input("Are you done adding?")
        outer_confirm.upper()
        if (outer_confirm == "YES"):
            for i in instruction_lists:
                i = Instruction(i)
                recipe.append_instruction(i)
            is_done = True
            print("Instructions added successfully")
        elif (outer_confirm == "NO"):
            continue
        else:
            raise ValueError("must be yes or no")