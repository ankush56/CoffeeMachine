# Coffee Machine
# Test
def main():
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

    currentResource = {
        "water": 1000,
        "milk": 1000,
        "coffee": 1000,
        "money": 0
    }

    def check_resource_sufficient(selection):
        for ingredient, amount in MENU[selection]["ingredients"].items():
            if amount > currentResource[ingredient]:
                print("Machine is currently short on supplies to make {0}. Please use another drink".format(selection))
                resource_check_status = False
                return False
            else:
                return True

    def process_coins():
        print("Please insert coins:")
        quarters = input("How many Quarters?")
        dimes = input("How many Dimes?")
        nickels = input("How many Nickels?")
        pennies = input("How many Pennies?")
        total = (float(quarters) * 0.25) + (0.1 * float(dimes)) + (0.05 * float(nickels)) + (float(pennies) * 0.01)
        total = round(total, 2)
        print("Total is {}".format(total))
        return total

    def transaction(total, selection):
        cost = MENU[selection]["cost"]
        if total < cost:
            print("Sorry Thats not enough money, Money refunded")
        else:
            net = total - cost
            net = round(net, 2)
            print("Thank you Here is your change {}".format(net))

    def process_drink(selection):
        for ingredient, amount in MENU[selection]["ingredients"].items():
            currentResource[ingredient] = currentResource[ingredient] - amount

        currentResource["money"] = currentResource["money"] + MENU[selection]["cost"]

    inputPrompt = True

    while inputPrompt:
        selection = input("What would you like? (espresso/latte/cappuccino)?")
        if selection == "espresso" or selection == "latte" or selection == "cappuccino":
            print("You selected {0} Drink".format(selection))
            result = check_resource_sufficient(selection)
            if result:
                total = process_coins()
                transaction(total, selection)
                process_drink(selection)
        elif selection == "report":
            print("Printing Report of current resources")
            print("Water: {} ml".format(currentResource["water"]))
            print("Milk: {} ml".format(currentResource["milk"]))
            print("Coffee: {} g".format(currentResource["coffee"]))
            print("Money: ${}".format(currentResource["money"]))

        elif selection == "off":
            print("Turning machine off")
            quit()
        else:
            print("Not a valid selection, please select again")


if __name__ == "__main__":
    main()

