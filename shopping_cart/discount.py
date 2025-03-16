class Discount(object):
    def discount_amount(self, cart):
        '''
        Calculate the discount amount.
        cart is a dictionary of items and their quantities.
        '''
        raise NotImplementedError('discount_amount')

    def __str__(self):
        raise NotImplementedError('__str__')

    def __repr__(self):
        return str(self)


class Type1(Discount):
    '''
    This discount is applied when a quantity of items is purchased. When x items are purchased, only y items are paid for.
    '
    '''

    def __init__(self, item_code, item_price, quantity, quantity_paid):
        self.item_code = item_code
        self.quantity = quantity
        self.quantity_paid = quantity_paid
        self.item_price = item_price

    def discount_amount(self, cart):
        if self.item_code in cart:
            discount_multiplier = cart[self.item_code] // self.quantity
            return discount_multiplier * (self.quantity - self.quantity_paid) * self.item_price
        return 0

    def __str__(self):
        return 'Type1(item_code=%s, item_price=%s, quantity=%s, quantity_paid=%s)' % (self.item_code, self.item_price, self.quantity, self.quantity_paid)


class Type2(Discount):
    '''
    This discount is applied when a quantity of items is purchased. When at least x items are purchased, the price of x is reduced.
    '''

    def __init__(self, item_code, quantity, old_price, new_price):
        self.item_code = item_code
        self.quantity = quantity
        self.new_price = new_price
        self.old_price = old_price

    def discount_amount(self, cart):
        if self.item_code in cart and cart[self.item_code] > self.quantity:
            return cart[self.item_code] * (self.old_price - self.new_price)

        return 0

    def __str__(self):
        return 'Type2(item_code=%s, old_price=%s, new_price=%s, quantity=%s)' % (self.item_code, self.old_price, self.new_price, self.quantity)


class Type3(Discount):
    '''
    This discount is applied when an item is purchased, another item is given for free.
    '''

    def __init__(self, item_code, freebie_code, freebie_price):
        self.item_code = item_code
        self.freebie_code = freebie_code
        self.freebie_price = freebie_price

    def discount_amount(self, cart):
        if self.item_code in cart and self.freebie_code in cart:
            return min(cart[self.item_code], cart[self.freebie_code]) * self.freebie_price
        return 0

    def __str__(self):
        return 'Type3(item_code=%s, freebie_code=%s, freebie_price=%s)' % (self.item_code, self.freebie_code, self.freebie_price)
