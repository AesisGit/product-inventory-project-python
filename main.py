import calculation
from constants import HELP_TEXT, GOOD_BYE_TEXT, TRY_AGAIN_TEXT
import sys

def current_stock(param1):
    """
    Goal: Display total number and total value of inventory
    Story: Function takes inventory parameter, does calculations and prints stock and value
    :param inventory: list of dictionaries containing stock info
    :return: N
    """
    inventory = param1
    if inventory:
        for item in inventory:
            for k, v in item.items():
                print("{} : {}" .format(k, v))
            print("*" * 10)
            stock_total, stock_value = calculation.get_current_stock(inventory)

        print("*** Total stock items: {}. ***" .format(stock_total))
        print("*** Total stock value: {}$. ***".format(stock_value))
    else:
        print("Inventory is empty!")

def display_on_screen(**kwargs):
    """
    Goal: Display text on screen
    Story: Taking in kwargs params that holds a constant text and displaying and printing it out
    :param kwargs: String stored in costants
    :return: N
    """
    try:
        text = kwargs["param1"]
    except KeyError as e:
        print(e)
    else:
        print(text)

def main():
    """
    Goal: Main function that manages calculations.
    Story: inventory is loaded at the start. Depending on user input neccecary acions are called. All actions are store
    in commands var.
    :return: N
    """
    inventory = calculation.load_from_file()
    commands = [
        {"X": {
            "call_function": display_on_screen,
            "function_input": GOOD_BYE_TEXT,
            "break_command": "break_command"
        }
        },
        {"H": {
            "call_function": display_on_screen,
            "function_input": HELP_TEXT
        }},
        {"L": {
            "call_function": current_stock,
            "function_input": inventory
        }},
        {"A": {
            "call_function":  calculation.add,
            "function_input": inventory
        }},
        {"S": {
            "call_function": calculation.sell,
            "function_input": inventory
        }},
    ]



    while True:
        user_input = input("Choices:\n[H] for [H]elp on information how to Add or Sell items.\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        user_input = user_input.upper()

        for command in commands:
            if user_input in command:
                called_command = command[user_input]
                function_to_call = called_command["call_function"]
                function_to_call(param1=called_command["function_input"])
                calculation.save_to_file(inventory)
                if "break_command" in called_command:
                    sys.exit()
            else:
                params = {
                    "param1": TRY_AGAIN_TEXT
                }
                display_on_screen(**params)

if __name__=="__main__":
    main()