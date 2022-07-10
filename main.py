import os
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

run_program = True


# Function to compare resources required with resources in machine
def are_resources_sufficient(order_ingredients):
    """Returns True or False based on if there is enough resources to make order"""
    enough_resources = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. ")
            enough_resources = False
    return enough_resources


# Function to process coins
def process_coins():
    """Returns total calculated from coins inserted"""
    # Process Expenses
    print("Please insert coins.")
    # Input payment
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    p = int(input("How many pennies? "))
    # Input payment
    quarters = (0.25 * q)
    dimes = 0.10 * d
    nickles = 0.05 * n
    pennies = 0.01 * p
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee (drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ☕ ")




while run_program:
    # Start
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # Process User Input
    if user_input == "off":
        run_program = False
    elif user_input == "report":
        print(resources)
        print(f"Money : ${money}")
    # Determine if resources are adequate
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = MENU[user_input]
        if are_resources_sufficient(drink["ingredients"]):
            # Verify amount paid
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])

