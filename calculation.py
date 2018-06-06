def add(userInput,inventory):
    #format: A,item name, amount, price
    isFound = False

    for oneDict in inventory:
        #If item is found make calculaton to get value of one item and add new stock to inventory stock.
        if userInput[1] == oneDict["NAME"]:
            isFound = True
            #Total value of current item + Total value of added stock of current item - total number of stock item
            oneDict["VALUE"] = (float(oneDict["VALUE"] * oneDict["NUMBER"]) + (float(userInput[2]) * float(userInput[3]))) / (oneDict["NUMBER"] + int(userInput[2]))
            oneDict["NUMBER"] += int(userInput[2])

    #If item not found in inventory add it to inventory
    if isFound == False:
        newItem = {}
        newItem["NAME"] = userInput[1]
        newItem["NUMBER"] = userInput[2]
        newItem["VALUE"] = userInput[3]
        inventory.append(newItem)

    return inventory

def sell(userInput,sum):
    sum -= int(userInput[1:])
    return sum



#Calculationg sums of inventory of total stock and total value of all items.
def get_current_stock(inventory):
    sumOfStock = 0
    sumOfValue = 0

    for oneDict in inventory:
        sumOfStock += int(oneDict["NUMBER"])
        sumOfValue += float(oneDict["VALUE"] * oneDict["NUMBER"])

    return (sumOfStock,sumOfValue)