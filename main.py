"""This is a Coffee Maker Application"""
# Imports
from data import menu, resources


def coffee(drink):
    """This function returns the kind of coffee the user wants."""
    if drink not in menu:
        return "Invalid coffee request"
    else:
        print(menu[user_drink])


# User Prompt
user_drink = input('What would you like? ')
make = coffee(user_drink)



