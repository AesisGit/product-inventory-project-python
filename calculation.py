import json


def adding_when_item_is_found(oneDict, item_value, item_number):
    # Total value of current item + Total value of added stock of current item - total number of stock item
    oneDict["VALUE"] = (float(oneDict["VALUE"] * oneDict["NUMBER"]) + (float(item_value) * float(item_number))) / (
                oneDict["NUMBER"] + int(item_number))
    oneDict["NUMBER"] += int(item_number)

    return(oneDict["VALUE"], oneDict["NUMBER"])


def adding_item_to_inventory(inventory, item_name, item_value, item_number):
     newItem = {}
     newItem["NAME"] = item_name
     newItem["NUMBER"] = int(item_number)
     newItem["VALUE"] = float(item_value)
     inventory.append(newItem)
     return inventory

def get_item_data_from_user():
    user_input = input("item name, item value, item number")
    user_input = user_input.split(",")
    return user_input[0], user_input[1], user_input[2]

def add(param1):
    inventory = param1
    #format: A,item name, amount, price
    isFound = False
    item_name, item_value, item_number = get_item_data_from_user()
    for one_item in inventory:
        #print(oneDict)
        #If item is found make calculaton to get value of one item and add new stock to inventory stock.
        if item_name == one_item["NAME"]:
            one_item["Value"], one_item["NUMBER"] = adding_when_item_is_found(one_item, item_value, item_number)
            isFound = True

    #If item not found in inventory add it to inventory
    if isFound == False:
        inventory = adding_item_to_inventory(inventory, item_name, item_value, item_number)

    return inventory

def selling_item_still_on_lager(oneDict, wantsToSell):
    oneDict["NUMBER"] = oneDict["NUMBER"] - wantsToSell
    # If amount after subtraction is 0 the value is also 0
    if oneDict["NUMBER"] == 0:
        oneDict["VALUE"] = 0

    return(oneDict["NUMBER"], oneDict["VALUE"])

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
                oneDict["NUMBER"], oneDict["VALUE"] = selling_item_still_on_lager(oneDict, wantsToSell)

            #If amount after subtraction would be bellow 0, make it 0 and tell the user num that can not be subtracted
            elif (currentLager - wantsToSell) < 0:
                oneDict["NUMBER"] = 0
                oneDict["VALUE"] = 0
                print("Subtracted as much as possible\nThere was {0} on lager and you subtracted {1}.\n"
                      "I removed {2} and there is {3} left to be removed".format(currentLager,
                                                                                 wantsToSell, currentLager, (wantsToSell - currentLager)))

    #If the selling item has never been in the warehouse inform the user
   if isFound == False:
       print("Cant find {0}. {0} has never been in the warehouse!".format((userInput[1])))

   return (inventory)



#Calculationg sums of inventory of total stock and total value of all items.
def get_current_stock(inventory):
    sumOfStock = 0
    sumOfValue = 0

    for oneDict in inventory:
        sumOfStock += int(oneDict["NUMBER"])
        sumOfValue += float(oneDict["VALUE"] * oneDict["NUMBER"])

    return (sumOfStock,sumOfValue)



def save_to_file(inventory):
    with open('inventory.inv', 'w') as file:
        json.dump(inventory, file)
        file.close()

def load_from_file():
    with open('inventory.inv', 'r') as file:
        inventory = json.load(file)
    return inventory
