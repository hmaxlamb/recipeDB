import sqlite3
import dbfuncs

class Recipe:
   
   #init fuction to make recipe class
    def __init__(name, category):
        self.name = name
        self.category = category
        self.ingredients = []
        self.intructions = []

    def __add_ingredient(ingredient):
        self.ingredients.append(ingredient)

    def __add_intruction(instuction):
        self.ingredients.append = []

    def _add to db():
        
