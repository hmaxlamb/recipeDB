import sqlite3

def initialize_database():
    #Creats database / Connnection
    conn = sqlite3.connect("recipe_database.db")
    cursor = conn.cursor()

    conn.close()