import sqlite3
import dbfuncs

class Recipe:
   
   #init fuction to make recipe class
    def __init__(self, name, category):
        self.name = name.upper()
        self.category = category.upper()
        self.ingredients = []
        self.intructions = []

    def __add_ingredient(self, ingredient):
        self.ingredients.append(self, ingredient)

    def __append_instruction(self, instuction):
        instuction.step_number = len(self.intructions) + 1
        self.ingredients.append(instuction)

    #This fuction will insert the instrunction and -
    #move the current instuction at the index  to the left
    def __insert_instruction(self, instruction, step_num):
        index = step_num - 1
        self.instrunctions[index].step_number += 
        instruction.step_number = step_num

        self.instrunctions.insert(index, instruction)

        

class Ingredient:
    def __init__(self, name):
        self.name = name.upper()

class Instruction:
    def __init__(self, desc, step_number):
        self.desc = desc
        self.step_number = step_number
