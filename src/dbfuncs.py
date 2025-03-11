import sqlite3

def initialize_database():
    #Creats database / Connnection
    conn = sqlite3.connect("recipe_database.db")
    cur = conn.cursor()

    cur.execute(
        """CREAT TABLE IF NOT EXIST Recipe (
        ID INTEGER PRIMARY KEY ASC, 
        Name VARCHAR(60) UNIQUE,
        Catagory VARCHAR(20),
        );
        """
        )


    conn.close()