import unittest
import calculation

class AddingTestCase(unittest.TestCase):

    def test_adding_when_item_is_found(self):
        oneDictValue, oneDictNumber = calculation.adding_when_item_is_found({'NAME': 'ITEM1', 'NUMBER': 10, 'VALUE': 10}, ['A', 'ITEM1', '2', '10'])
        self.assertEqual(oneDictValue, 10.0)
        self.assertEqual(oneDictNumber, 12)


    def test_adding_item_to_inventory(self):
        inventory = calculation.adding_item_to_inventory(['A', 'ITEM3', '3', '10'], [{'NAME': 'ITEM1', 'NUMBER': 11, 'VALUE': 50}, {'NAME': 'ITEM2', 'NUMBER': 2, 'VALUE': 4.3}])
        self.assertEqual(inventory, [{'NAME': 'ITEM1', 'NUMBER': 11, 'VALUE': 50}, {'NAME': 'ITEM2', 'NUMBER': 2, 'VALUE': 4.3}, {'NAME': 'ITEM3', 'NUMBER': 3, 'VALUE': 10.0}])
"""
def adding_item_to_inventory(userInput, inventory):
    newItem = {}
    newItem["NAME"] = userInput[1]
    newItem["NUMBER"] = int(userInput[2])
    newItem["VALUE"] = float(userInput[3])
    inventory.append(newItem)

    return inventory
"""