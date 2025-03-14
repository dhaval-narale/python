import sys

# Coffee Machine Menu
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

# Initial profit and resources available in the machine
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources for the chosen drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:  # Fixed `>=` issue
            print(f"​Sorry, there is not enough {item}.")
            return False
    return True

def process_coin():
    """Processes inserted coins and returns total money inserted."""
    print("Please insert coins.")
    
    if sys.stdin.isatty():  # Interactive mode
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
    else:  # Non-interactive mode (Jenkins)
        total = 5.0  # Insert default sufficient amount
        print("Inserted $5.0 (Auto Mode)")
    
    return total    

def is_transaction_successful(money_received, drink_cost):
    """Checks if the transaction is successful."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients and serves the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Coffee Machine Loop
is_on = True

while is_on:
    if sys.stdin.isatty():  # Interactive mode
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    else:  # Non-interactive mode (Jenkins)
        choice = "latte"
        print("Auto-selected: latte")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources.get('milk', 0)}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink_name=choice, order_ingredients=drink['ingredients'])
    else:
        print("Invalid choice, please select a valid option.")
