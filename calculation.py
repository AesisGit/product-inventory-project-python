def submit(userInput,sum):
    sum+=int(userInput[1:])
    return sum

def sell(userInput,sum):
    sum-=int(userInput[1:])
    return sum



#Calculationg sums of inventory of total stock and total value of all items.
def get_current_stock(inventory):
    sumOfStock = 0
    sumOfValue = 0

    for oneDict in inventory:
        sumOfStock += int(oneDict["NUMBER"])
        sumOfValue += float(oneDict["VALUE"] * oneDict["NUMBER"])

    return (sumOfStock,sumOfValue)