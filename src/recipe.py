import sqlite3
import dbfuncs

class Recipe:
   
   #init fuction to make recipe class
    def __init__(self, name, category):
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
        if type(step_num) is not int:
            raise ValueError("The step number must be a string!")
        index = step_num - 1
        self.instrunctions[index].step_number += 1
        instruction.step_number = step_num

        self.instrunctions.insert(index, instruction)

        

class Ingredient:
    def __init__(self, name, ammount, unit=None):
        if type(name) is str:
            self.name = name.upper()
        else:
            raise ValueError("name must be string!")
        if type(ammount) is int:
            self.ammount = float(ammount)
        elif type(ammount) is float:
            self.ammount = ammount
        else:
            raise ValueError("ammount must be int or float!")
        
        if unit:
            if type(unit) is str:
                self.unit = unit.upper()
            else:
                raise ValueError("unit must be string!")
        


class Instruction:
    def __init__(self, desc, step_number):
        if type(desc) is str:
            self.desc = desc
        else:
            raise ValueError("The desciption must be a string!")
        self.desc = desc
        self.step_number = step_number
