#!/usr/bin/python3

def encryption_lock():
    first_code = input("Enter your code first time:")
    second_code = input("Enter your code second time:")

    if (first_code == second_code):
        first_code = None
        print("Congratulations, you gave a good code ! \n")
    else:
        print("Sorry, you made a mistake ! \n")
    return 0

encryption_lock()
