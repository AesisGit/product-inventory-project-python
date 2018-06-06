#Actions format for is LETTERNUMBER


from calculation import submit, sell

def current_stock(inventory):
    if inventory:
        for oneDict in inventory:
            for k,v in oneDict.items():
                print("{} : {}" .format(k,v))
            print("*" *10)

    else:
        print("Inventory is empty!")

def try_again():
    print("Please try again. I don't understand.")

def main():
    inventory = [{"NAME": "ABC", "NUMBER": 21, "VALUE": 50.0}, {"NAME": "AAA", "NUMBER": 2, "VALUE": 4.3},
                 {"NAME": "VVV", "NUMBER": 2, "VALUE": 4}]

    while True:
        userInput = input("Choices:\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        userInput  = userInput.upper().split(',')

        if userInput[0] == "X":
            print("Good bye !")
            break
        elif userInput[0] == 'X':
            current_stock(sums)
        elif userInput[0] == "L":
            current_stock(inventory)

        elif userInput[0] == "A":
            sums = submit(userInput, sums)
        elif userInput[0] == "S":
            sums = sell(userInput, sums)
        else:
            try_again()

if __name__=="__main__":
    main()