import unittest
import calculation

class AddingTestCase(unittest.TestCase):

    def test_adding_when_item_is_found(self):
        oneDictValue, oneDictNumber = calculation.adding_when_item_is_found({'NAME': 'ITEM1', 'NUMBER': 10, 'VALUE': 10}, ['A', 'ITEM1', '2', '10'])
        self.assertEqual(oneDictValue, 10.0)
        self.assertEqual(oneDictNumber, 12)


