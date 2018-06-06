def add(userInput,inventory):

    for oneDict in inventory:
        if userInput[1] == oneDict["NAME"]:
            #Total value of current item + Total value of added stock of current item - total number of stock item
            oneDict["VALUE"] = (float(oneDict["VALUE"] * oneDict["NUMBER"]) + (float(userInput[2]) * float(userInput[3]))) / (oneDict["NUMBER"] + int(userInput[2]))
            print("{}".format(oneDict["VALUE"]))
            oneDict["NUMBER"] += int(userInput[2])
            print("{}".format(oneDict["NUMBER"]))

    return inventory

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