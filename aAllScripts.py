import os
import pygame

#Code to import

import Eva
import Evan
import Quentin

def main():
    print("\n\n\nHello! This is a compilation of all of the code made throughout the trimester, sorted by person.")
    print("In order to select a person to see their code, type in the number corrisponding to them, and hit RETURN.\n")
    while True:
        p = input("Input the name of the student you would like to see, with the first letter capitalized (ex. Rey not rey) >>> ")
        try:
            func = __import__(p)
            func.main()
            break
        except:
            print("Something failed, either the formatting was bad, the name was misspelled, or that isn't a student. Please try again.")
main()