from collections import defaultdict

class Checkout(object):
    def __init__(self, pricing_rules):
        self.cart = defaultdict(int)
        self.pricing_rules = pricing_rules

    def scan(self, item):
        '''
        Scan an item.
        '''
        self.cart[item] += 1

    def remove(self, item):
        '''
        Remove an item.
        '''
        if item in self.cart:
            self.cart[item] -= 1

    def total(self):
        '''
        Calculate the total price.
        '''
        total = 0
        print('Cart | Quantity')
        for item in self.cart:
            print('%s | %s' % (item, self.cart[item]))
            total += self.pricing_rules.catalogue[item].price * self.cart[item]

        for discount in self.pricing_rules.discounts:
            if discount.discount_amount(self.cart) > 0:
                print('Discount applied: %s' % discount)
                total -= discount.discount_amount(self.cart)
        return total

    def reset(self):
        '''
        Reset the cart.
        '''
        self.cart = defaultdict(int)


