"""This is a Coffee Maker Application"""
# Imports
import os

from data import menu, resources
from logo import logo

revenue = 0
print(logo)


def check_resources(ingredients):
    """This function checks if there's enough resources to make the kind of coffee requested."""
    for material in ingredients:
        if ingredients[material] >= resources[material]:
            print(f"The Coffee Maker is out of {material} at the moment.")
            return False
    return True


def process_coins():
    """This functions process the coins inserted"""
    print("COINS only should be inserted into the coffee maker.")
    coins = int(input("How many Two Euros? ")) * 2
    coins += int(input("How many One Euro? ")) * 1
    coins += int(input("How many Fifty Cent? ")) * 0.50
    return coins


def check_transaction(coins_received, drink_cost):
    """This function check if the coins inserted is sufficient or not."""
    if coins_received >= drink_cost:
        global revenue
        revenue += drink_cost
        change = round(coins_received - drink_cost, 2)
        print(f"Your change is: €{change:.2f}, making your coffee...")
        return True
    else:
        print("The payment is incomplete, you have been refunded!\n")
        return False


def coffee(drink):
    """This function returns the kind of coffee the user wants."""
    if drink not in menu:
        print("Unknown to Coffee Maker\n")
    else:
        coffee_req = menu[drink]
        ingredients = coffee_req["ingredients"]
        if check_resources(ingredients):
            bill = menu[drink]["cost"]
            print(f'The {user_drink} price is €{bill:.2f}')
            payment = process_coins()
            if check_transaction(payment, bill):
                for material in ingredients:
                    resources[material] -= ingredients[material]
                print(f"Coffee is ready, here is your {drink} ☕️. Enjoy!\n")
        else:
            print(f'Unable to make {drink}.\n')


def clear():
    """This function clears the console."""
    os.system('clear')


turn_off = False
while not turn_off:

    # User Prompt
    default = input('Do you want a coffee? ').lower()

    clear()
    print(logo)

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
        print(f'Coffee Maker Report:\n '
              f'Water: {resources["water"]}ml\n '
              f'Milk: {resources["milk"]}ml\n '
              f'Coffee: {resources["coffee"]}g\n '
              f'Total sales: €{revenue:.2f}\n')
    else:
        print('Invalid response.\n')
