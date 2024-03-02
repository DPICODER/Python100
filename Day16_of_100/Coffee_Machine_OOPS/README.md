# Coffee Machine Simulator

This Python project simulates the operations of a coffee machine where users can select from a menu of drinks, make payments, and receive their beverages. The program keeps track of resources, handles payments, and provides reports of the machine's status.

## Components

### 1. CoffeeMachine Class

The `CoffeeMachine` class represents the main interface for users to interact with the coffee machine. It handles user input, displays the menu, and manages the overall operation of the machine.

### 2. CoffeeMaker Class

The `CoffeeMaker` class models the machine that makes the coffee. It manages resources such as water, milk, and coffee, checks resource sufficiency for making drinks, and prepares beverages.

### 3. MenuItem Class

The `MenuItem` class defines each drink available on the menu. It includes attributes such as the name of the drink, its ingredients, and the cost.

### 4. Menu Class

The `Menu` class represents the menu of drinks available in the coffee machine. It stores a list of `MenuItem` objects and provides methods to access and find drinks from the menu.

### 5. MoneyMachine Class

The `MoneyMachine` class handles payment processing for the coffee machine. It processes coins inserted by the user, calculates the total payment received, and provides change if necessary.

## Usage

1. **Starting the Coffee Machine**: Run the Python script to start the coffee machine simulator.

    ```bash
    python coffee_machine.py
    ```

2. **Choosing a Drink**: Users can choose from available drinks listed in the menu (espresso, latte, cappuccino).

3. **Making Payments**: After selecting a drink, users can insert coins to pay for the beverage. The machine calculates the total payment and provides change if needed.

4. **Viewing Reports**: Users can request a report to view the current status of available resources and profits earned by the machine.

5. **Turning Off the Machine**: To turn off the machine, users can input "off" at any time.

## Dependencies

- Python 3.x
- [prettytable](https://pypi.org/project/prettytable/) (for creating formatted tables)

## Contributing

Contributions to improve and expand the functionality of this coffee machine simulator are welcome. Feel free to fork the repository, make changes, and submit pull requests.

