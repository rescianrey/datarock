from shoppingcart.discount import Type1, Type2, Type3
from shoppingcart.item import Item

import unittest

class DiscountTest(unittest.TestCase):
    def test_discount_type1(self):
        item = Item('A', 'Apple', 10)
        discount = Type1(item, 3, 2)

        # No discount
        self.assertEqual(discount.discount_amount({'A': 2}), 0)

        # With discount
        self.assertEqual(discount.discount_amount({'A': 3}), 10)
        self.assertEqual(discount.discount_amount({'A': 4}), 10)
        self.assertEqual(discount.discount_amount({'A': 5}), 10)
        self.assertEqual(discount.discount_amount({'A': 6}), 20)


    def test_discount_type2(self):
        item = Item('A', 'Apple', 10)
        discount = Type2(item, 3, 5)

        # No discount
        self.assertEqual(discount.discount_amount({'A': 2}), 0)
        self.assertEqual(discount.discount_amount({'A': 3}), 0)

        # With discount
        self.assertEqual(discount.discount_amount({'A': 4}), 20)

    def test_discount_type3(self):
        item = Item('A', 'Apple', 10)
        freebie = Item('B', 'Banana', 5)
        discount = Type3(item, freebie)

        # No discount
        self.assertEqual(discount.discount_amount({'B': 2}), 0)

        # With discount
        self.assertEqual(discount.discount_amount({'A': 3, 'B': 3}), 15)
        self.assertEqual(discount.discount_amount({'A': 4, 'B': 3}), 15)
        self.assertEqual(discount.discount_amount({'A': 3, 'B': 4}), 15)
        self.assertEqual(discount.discount_amount({'A': 2, 'B': 3}), 10)

if __name__ == '__main__':
    unittest.main()
