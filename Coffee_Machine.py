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

# Function to check if there are sufficient resources for the chosen drink
def is_resource_sufficient(order_ingredients):
    # Loop through each ingredient required for the drink
    for item in order_ingredients:
        # Check if the required amount is more than the available amount
        if order_ingredients[item] >= resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# Function to process coin input and calculate the total money inserted
def process_coin():
    print("Please insert coins.")
    # Ask user for the number of each type of coin and calculate total
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total    

# Function to check if the transaction is successful
def is_transaction_succesful(money_received, drink_cost):
    # Check if the money received is enough to cover the cost of the drink
    if money_received >= drink_cost:
        # Calculate and return the change if any
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Update the profit
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee by deducting the required ingredients from the resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Variable to keep the coffee machine running
is_on = True

# Main loop to run the coffee machine
while is_on:
    # Ask the user what they would like
    choice = input("What would you like? (espresso/latte/cappuccino):")
    
    # Turn off the machine if the user types "off"
    if choice == "off":
        is_on = False
    
    # Print a report of the resources and profit if the user types "report"
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney: {profit}")
    
    # Process the chosen drink
    else:
        drink = MENU[choice]
        # Check if there are sufficient resources to make the drink
        if is_resource_sufficient(drink['ingredients']):
            # Process coins and check if the transaction is successful
            payment = process_coin()
            if is_transaction_succesful(payment, drink['cost']):
                # Make the coffee
                make_coffee(drink_name=choice, order_ingredients=drink['ingredients'])
