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
    recipe_name_made = False
    has_confirmed_correctly = False
    while (not recipe_name_made):
        has_confirmed_correctly = False
        r_name = input("Please name recipe\n")
        while(not has_confirmed_correctly):
            confirm = input(f"Please confirm name: {r_name} (Yes/No)\n")
            confirm = confirm.upper()
            if (confirm == "YES"):
                recipe_name_made = True
                has_confirmed_correctly = True
            elif (confirm == "NO"):
                has_confirmed_correctly = True
                continue
            else:
                print("Must be yes or no")
    
    catagory_name_made = False
        
    while(not catagory_name_made):
        has_confirmed_correctly = False
        c_name = input("Please Input Catagory\n")
        while (not has_confirmed_correctly):
            confirm = input(f"Please confirm catagory: {c_name} (Yes/No)\n")
            confirm = confirm.upper()
            if (confirm == "YES"):
                print(f"Catagory Name: {c_name}")
                has_confirmed_correctly = True
                catagory_name_made = True
            elif (confirm == "NO"):
                has_confirmed_correctly = True
                continue
            else:
                print("Must be yes or no")
        
    r = Recipe(r_name, c_name)

    return r

#function that quickly gathers a list of instructions
#to import to a recipe, the recipe must be empty
def create_list_of_instuctions(recipe):
    if (len(recipe.instructions) != 0):
        raise ValueError("recipe must be empty")
    is_done = False
    instruction_lists = []
    ins = None
    count = 0
    has_confirmed_answer = False
    while(not is_done):
        ins = None
        is_instruction_made = False
        count += 1
        while(not is_instruction_made):
            ins = input(f"Please input instruction number {count}:\n")
            has_confirmed_answer = False
            while (not has_confirmed_answer):
                confirm = input(f"Is the following instruction correct:\n{ins}\n")
                confirm = confirm.upper()
                if (confirm == "YES"):
                    instruction_lists.append(ins)
                    is_instruction_made = True
                    has_confirmed_answer = True
                elif (confirm == "NO"):
                    has_confirmed_answer = True
                    continue
                else:
                    print("Must be yes or no")
        has_confirmed_answer = False
        while(not has_confirmed_answer):
            outer_confirm = input("Are you done adding? (Yes/No/Print)\n")
            outer_confirm = outer_confirm.upper()
            if (outer_confirm == "YES"):
                for i in instruction_lists:
                    i = Instruction(i)
                    recipe.append_instruction(i)
                is_done = True
                has_confirmed_answer = True
                print("Instructions added successfully")
                continue
            if (outer_confirm == "PRINT"):
                fmt_string = format_instruction_list_for_print(instruction_lists)
                print(fmt_string)
                continue
            elif (outer_confirm == "NO"):
                has_confirmed_answer = True
                continue
            else:
                print("Please type correct choice")

#This helper function will format a list of instructions to show the user before
#they add to the recipe so they can be sure that they are done
def format_instruction_list_for_print(list):
    fmt_list = []
    for i in range(0, len(list)):
        fmt_list.append(f"{i + 1}. " + list[i])
    fmt_string = "\n".join(fmt_list)
    return fmt_string

def get_new_ingredient_name():
    confirmed_name = False
    correct_confirm = False
    while(not confirmed_name):
        name = input("Please name ingredient")
        while(not correct_confirm):
            confirm = input("Is {name} the correct name? (Yes/No)")
            confirm.upper()
            match confirm:
                case "YES":
                    correct_confirm = True
                    confirmed_name = True
                case "NO":
                    correct_confirm = True
                    continue
                case _:
                    "Error please type yes or no"
    return name

def get_new_ammount():
    confirmed_ammount = False
    correct_confirm = False
    while(not confirmed_ammount):
        ammount = input("Please input the ammount")
        try:
            ammount = float(ammount)
        except ValueError:
            print("Please input number!")
            continue
        while(not correct_confirm):
            confirm = input("Is {ammount} the correct ammount? (Yes/No)")
            confirm.upper()
            match confirm:
                case "YES":
                    correct_confirm = True
                    confirmed_ammount = True
                case "NO":
                    correct_confirm = True
                    continue
                case _:
                    "Error please type yes or no"
    return ammount