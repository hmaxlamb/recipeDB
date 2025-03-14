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
        self.intructions = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(self, ingredient)

    def append_instruction(self, instuction):
        instuction.step_number = len(self.intructions) + 1
        self.ingredients.append(instuction)

    #This fuction will insert the instrunction and -
    #move the current instuction at the index  to the left
    def insert_instruction(self, instruction, step_num):
        index = step_num - 1
        self.intructions[index].step_number += 1
        instruction.step_number = step_num

        self.intructions.insert(index, instruction)

        

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
    def __init__(self, desc, step_number):
        if not isinstance(desc, str):
            raise TypeError("The description must be a string!")
        if not isinstance(step_number, int):
            raise TypeError("Step Number must be an int!")
        self.desc = desc
        self.step_number = step_number
