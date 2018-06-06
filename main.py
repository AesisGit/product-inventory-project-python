#Actions format for is LETTERNUMBER


from calculation import submit, sell

def current_stock(sums):
    print("*** Current stock is: {}. ***".format(sums))

def try_again():
    print("Please try again. I don't understand.")

def main():
    sums = 0
    userInput = None

    while userInput != "X":
        userInput = input("Choices:\n[A] and amount to [A]dd.\n[S] and amount to [S]ell\n[L] to [L]ist current stock\n[x] for E[x]it.\nEnter command: ")
        userInput  = userInput.upper()
        if userInput[:1] in ['X','L']:
            current_stock(sums)
        elif userInput[:1] == "A":
            sums = submit(userInput, sums)
        elif userInput[:1] == "S":
            sums = sell(userInput, sums)
        else:
            try_again()

if __name__=="__main__":
    main()