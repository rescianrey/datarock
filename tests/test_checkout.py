import unittest

from shoppingcart.checkout import Checkout
from shoppingcart.item import Item
from shoppingcart.discount import Type1
from shoppingcart.pricing_rules import PricingRules

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.catalog = {
            'A': Item('A', 'Apple', 10),
            'B': Item('B', 'Banana', 15),
            'C': Item('C', 'Cherry', 20),
            'D': Item('D', 'Date', 25),
        }
        self.discount = []
        self.pricing_rules = PricingRules(self.catalog, self.discount)

    def test_checkout(self):
        checkout = Checkout(self.pricing_rules)
        checkout.scan('A')
        checkout.scan('B')
        checkout.scan('A')

        self.assertEqual(checkout.total(), 35)

    def test_checkout_with_discount(self):
        discount = Type1(self.catalog['A'], 3, 2)
        self.discount.append(discount)
        self.pricing_rules = PricingRules(self.catalog, self.discount)

        checkout = Checkout(self.pricing_rules)
        checkout.scan('A')
        checkout.scan('A')
        checkout.scan('A')

        self.assertEqual(checkout.total(), 20)


    def test_checkout_with_reset(self):
        checkout = Checkout(self.pricing_rules)
        checkout.scan('A')
        checkout.scan('B')
        checkout.scan('A')

        self.assertEqual(checkout.total(), 35)

        checkout.reset()

        self.assertEqual(checkout.total(), 0)


    def test_checkout_with_remove(self):
        checkout = Checkout(self.pricing_rules)
        checkout.scan('A')
        checkout.scan('B')
        checkout.scan('A')

        self.assertEqual(checkout.total(), 35)

        checkout.remove('A')

        self.assertEqual(checkout.total(), 25)

        checkout.remove('B')

        self.assertEqual(checkout.total(), 10)

        checkout.remove('A')

        self.assertEqual(checkout.total(), 0)



if __name__ == '__main__':
    unittest.main()
