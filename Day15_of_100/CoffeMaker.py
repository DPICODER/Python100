# Define the menu items with their respective ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 180,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 110,
    }
}

# Track the profit earned
profit = 0

# Available resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Check if there are sufficient resources to make the ordered drink
def is_sufficient_resource(order_ingredients):
    """Returns True when order can be Processed or False if Insufficient Resource"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# Process money inserted by the user
def process_money():
    """Returns the total calculated money inserted"""
    print("Insert Money")
    total = int(input("how many 10's   :")) * 10
    total += int(input("how many 20's  : ")) * 20
    total += int(input("how many 50's  : ")) * 50
    total += int(input("how many 100's  : ")) * 100
    print(total)
    return total


# Check if the transaction is successful
def is_transaction_successful(money, drink_cost):
    """Returns True when Payment is Accepted, or False if money is Insufficient"""
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is Change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry Insufficient Money. Money Refunded")
        return False


# Deduct resources used for the order
def deduct_resources(drink_name, order_ingredients):
    """Deducts the ingredients used for the order from the available resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is Your Drink {drink_name} ☕")


# Main loop for user interaction
is_on = True
while is_on:
    choice = input("What would you like? (espresso / latte / cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":  # Gives a resources Report to the user
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : {profit}")
    else:
        drink = MENU[choice]
        if is_sufficient_resource(drink['ingredients']):
            print(f"Pay the Amount for {choice} of Rupees : {drink['cost']}")
            payment = process_money()
            if is_transaction_successful(payment, drink['cost']):
                deduct_resources(choice, drink['ingredients'])
