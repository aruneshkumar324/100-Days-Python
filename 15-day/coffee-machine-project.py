from data import MENU, resources

loop = True
while loop:

    # DATA STATUS
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # COMPARE DATA
    def compare(coffee_type):
        milk = MENU[coffee_type]["ingredients"]["milk"]
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        cost = MENU[coffee_type]["cost"]

        print("Please insert coins.")
        total = int(input(f"How many quarters?: ")) * 0.25
        total += int(input(f"How many dimes?: ")) * 0.1
        total += int(input(f"How many nickles?: ")) * 0.05
        total += int(input(f"How many pennies?: ")) * 0.01

        if total >= cost:
            if resources_water >= water:
                if resources_coffee >= coffee:
                    if resources_milk >= milk:
                        print(f"Here is ${round(total - cost, 2)} in change. ")
                        print("Here is your espresso ☕. Enjoy! ")
                        resources["water"] -= water
                        resources["milk"] -= milk
                        resources["coffee"] -= coffee
                        resources["Money"] += cost
                    else:
                        print("Sorry, there not enough milk.")
                else:
                    print("Sorry, there not enough coffee.")
            else:
                print("Sorry, there not enough water.")
        else:
            print("Sorry that's not enough money. Money refunded.")

    if user_input == "off":
        loop = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['Money']}")
    elif user_input == "espresso":
        compare("espresso")
    elif user_input == "latte":
        compare("latte")
    elif user_input == "cappuccino":
        compare("cappuccino")


'''     ANGELA SOLUTION

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(Input("how many quarters?: ")) * 0.25
    total += int(Input("how many dimes?: ")) * 0.1
    total += int(Input("how many nickles?: ")) * 0.05
    total += int(Input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = Input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


'''