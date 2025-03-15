import sqlite3
from recipe import *
from dbfuncs import initialize_database
def main():
    initialize_database()
    print('\nWelcom to recipeDB! Press tab to view commands')
    while True:
        command = input("Please Enter Command")