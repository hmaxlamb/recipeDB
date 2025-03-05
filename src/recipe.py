

class Recipe:
   
   #init fuction to make recipe class
    def __init__(name, category, *args):
        self.name = name
        self.category = category
        self.ingredients = []
        for arg in args:
            self.ingredients.append(arg)

