import sqlite3
from dbfuncs import initialize_database
def main():
    initialize_database()
    print('\nWelcom to recipeDB! Press tab to view commands')
    while True:
        command = input()
        match command:
            "quit":
                return