import sqlite3
from recipe import *
from dbfuncs import initialize_database
def main():
    #initialize_database()
    print('\nWelcom to recipeDB! Press tab to view commands')
    while True:
        command = input("Please Enter Command\n")
        command.upper()
        match command:
            case "QUIT":
                return
            case "NEW RECIPE":
                nr = prompt_recipe()
                create_list_of_instuctions(nr)

main()
                