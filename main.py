"""This is a Coffee Maker Application"""
# Imports
from data import menu, resources


def check_resources(ingredients):
    """This function checks if there's enough resources to make the kind of coffee requested"""
    for material in ingredients:
        if ingredients[material] >= resources[material]:
            print(f"The Coffee Maker is out of {material} at the moment.")
            return False
    return True


def coffee(drink):
    """This function returns the kind of coffee the user wants."""
    if drink not in menu:
        print("Invalid coffee request")
    else:
        coffee_req = menu[drink]
        ingredients = coffee_req["ingredients"]
        if check_resources(ingredients):
            bill = menu[drink]["cost"]
            print(f'The {user_drink} price is €{bill:.2f}')
            for material in ingredients:
                resources[material] -= ingredients[material]
            print(f"Order completed, here is your {drink} ☕️. Enjoy!\n")
        else:
            print(f'Unable to {drink}.\n')


turn_off = False
while not turn_off:
    revenue = 0
    # User Prompt
    default = input('\nDo you want a coffee? ').lower()

    if default == 'yes':
        user_drink = input('What would you like? ').lower()
        coffee(user_drink)
    elif default == 'no':
        turn_off = True
        print('Okay.')
    elif default == 'off':
        turn_off = True
        print('The Coffee Maker is off.')
    elif default == 'report':
        print(f'The current resources available are:\n '
              f'Water: {resources["water"]}ml\n '
              f'Milk: {resources["milk"]}ml\n '
              f'Coffee: {resources["coffee"]}g\n '
              f'Total sales: €{revenue:.2f}\n')
    else:
        print('Invalid response.')
