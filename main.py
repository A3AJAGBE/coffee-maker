"""This is a Coffee Maker Application"""
# Imports
from data import menu, resources


def coffee(drink):
    """This function returns the kind of coffee the user wants."""
    if drink not in menu:
        return "Invalid coffee request"
    else:
        print(menu[user_drink])


turn_off = False
while not turn_off:
    # User Prompt
    default = input('Do you want a coffee? ').lower()

    if default == 'yes':
        user_drink = input('What would you like? ').lower()
        make = coffee(user_drink)
    elif default == 'off':
        turn_off = True
        print('The Coffee Maker is off.')
    else:
        print('Invalid response.')


