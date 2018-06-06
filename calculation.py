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

def sell(userInput,inventory):
   isFound = False
   for oneDict in inventory:
       #Find the item to subtract
       if userInput[1] == oneDict["NAME"]:
            isFound = True
            currentLager = oneDict["NUMBER"]
            wantsToSell = int(userInput[2])

            #If amount after subtraction is >= 0
            if currentLager - wantsToSell >= 0:
                oneDict["NUMBER"] = oneDict["NUMBER"] - wantsToSell
                #If amount after subtraction is 0 the value is also 0
                if oneDict["NUMBER"] == 0:
                    oneDict["VALUE"] = 0
            #If amount after subtraction would be bellow 0, make it 0 and tell the user num that can not be subtracted
            elif (currentLager - wantsToSell) < 0:
                oneDict["NUMBER"] = 0
                oneDict["VALUE"] = 0
                print("Subtracted as much as possible\nThere was {0} on lager and you subtracted {1}.\n"
                      "I removed {2} and there is {3} left to be removed".format(currentLager,
                                                                                 wantsToSell,currentLager, (wantsToSell - currentLager)))

    #If the selling item has never been in the warehouse inform the user
   if isFound == False:
       print("Cant find {0}. {0} has never been in the warehouse!".format((userInput[1])))

   return inventory



#Calculationg sums of inventory of total stock and total value of all items.
def get_current_stock(inventory):
    sumOfStock = 0
    sumOfValue = 0

    for oneDict in inventory:
        sumOfStock += int(oneDict["NUMBER"])
        sumOfValue += float(oneDict["VALUE"] * oneDict["NUMBER"])

    return (sumOfStock,sumOfValue)