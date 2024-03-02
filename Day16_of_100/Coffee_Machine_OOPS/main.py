from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
sys_menu = Menu()

is_on = True

while is_on:

    options = sys_menu.get_items()
    choice = input(f"Choice : {options}")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = sys_menu.find_drink(choice)

        # print(coffee_maker.is_resource_sufficient(drink))
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) :
            coffee_maker.make_coffee(order=drink)


