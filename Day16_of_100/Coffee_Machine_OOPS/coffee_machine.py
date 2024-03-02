from menu import MENU
# import random


class CoffeeMachine:
    # Available resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    showMenu = MENU


    is_on = True


    while is_on:
        choice = input("What would you like? (espresso / latte / cappuccino) : ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print("Report")
            print(f"Water :  {resources['water']}")
            print(f"Water :  {resources['milk']}")
            print(f"Water :  {resources['coffee']}")
            # is_on = False
        else:
            print(choice)



