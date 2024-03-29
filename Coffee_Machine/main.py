# Coffee Machine Program Requirements

#TODO #0
# 1. Download the menu and resources from the starting replit code.

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
    "money": 0
}

#TODO #1 -done
# 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

def prompt_user():
    return input(" What would you like? (espresso/latte/cappuccino): ")

#TODO #2 - done
# 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

def turn_off():
    print("Turning off the coffee machine.")
    exit()

#TODO #3
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

def print_report():
    print("Current Resources:")
    for resource, quantity in resources.items():
        if resource == "money":
            print(f"{resource.capitalize()}: ${quantity}")
        else:
            unit = "ml" if resource in ["water", "milk"] else "g"
            print(f"{resource.capitalize()}: {quantity}{unit}")


#TODO #4
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def check_resources_sufficient(drink):
    for ingredient, quantity in MENU[drink]["ingredients"].items():
        if resources.get(ingredient, 0) < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

#TODO #5
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins():
    quarters = int(input("Please insert coins.\nhow many quarters?: "))
    dimes = int(input( "How many dimes?: "))
    nickles = int(input( "How many nickles?: "))
    pennies = int(input( "How many pennies?: "))
    total = ((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
    return total
# process_coins()

#TODO #6
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def check_transaction_successful(drink,total):
    cost = MENU[drink]["cost"]
    if cost > total:
        print("Sorry that is not enough money. Money refunded")
        return False
    elif cost < total:
        change = total - cost
        print(f"Here is ${round(change,2)} dollars in change.")
    resources["money"] += cost  # Update machine profit
    return True


#TODO #7
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

def make_coffee(drink):
    for ingredient, quantity in MENU[drink]["ingredients"].items():
        resources[ingredient] -= quantity
    print(f"Here is your {drink}. Enjoy!")

def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        user_choice = prompt_user()
        if user_choice == "off":
            turn_off()
        elif user_choice == "report":
            print_report()
        elif user_choice in MENU:
            if check_resources_sufficient(user_choice):
                total_amount = process_coins()
                if check_transaction_successful(user_choice, total_amount):
                    make_coffee(user_choice)
        else:
            print("Invalid choice. Please try again.")

coffee_machine()
