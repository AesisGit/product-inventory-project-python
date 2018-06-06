import calculation

def current_stock(inventory):
    if inventory:
        for oneDict in inventory:
            for k,v in oneDict.items():
                print("{} : {}" .format(k, v))
            print("*" * 10)
            sumOfStock, sumOfValue = calculation.get_current_stock(inventory)

        print("*** Total stock is: {}. ***" .format(sumOfStock))
        print("*** Total stock value: {}. ***".format(sumOfValue))

    else:
        print("Inventory is empty!")

def try_again():
    print("Please try again. I don't understand.")

def main():
    inventory = [{"NAME": "ABC", "NUMBER": 2, "VALUE": 25.0}, {"NAME": "AAA", "NUMBER": 2, "VALUE": 1},
                 {"NAME": "VVV", "NUMBER": 2, "VALUE": 4}]

    while True:
        userInput = input("Choices:\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        userInput  = userInput.upper().split(',')

        if userInput[0] == "X":
            current_stock(inventory)
            print("Good bye !")
            break
        elif userInput[0] == "L":
            current_stock(inventory)

        elif userInput[0] == "A":
            inventory = calculation.add(userInput, inventory)
            print(inventory)
        elif userInput[0] == "S":
            inventory = calculation.sell(userInput, inventory)
        else:
            try_again()

if __name__=="__main__":
    main()