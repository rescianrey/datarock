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

    def __init__(self, item, quantity, quantity_paid):
        self.item = item
        self.quantity = quantity
        self.quantity_paid = quantity_paid

    def discount_amount(self, cart):
        if self.item.code in cart:
            discount_multiplier = cart[self.item.code] // self.quantity
            return discount_multiplier * (self.quantity - self.quantity_paid) * self.item.price
        return 0

    def __str__(self):
        return 'Type1(item_code=%s, item_price=%s, quantity=%s, quantity_paid=%s)' % (self.item.code, self.item.price, self.quantity, self.quantity_paid)


class Type2(Discount):
    '''
    This discount is applied when a quantity of items is purchased. When at least x items are purchased, the price of x is reduced.
    '''

    def __init__(self, item, quantity, new_price):
        self.item = item
        self.quantity = quantity
        self.new_price = new_price

    def discount_amount(self, cart):
        if self.item.code in cart and cart[self.item.code] > self.quantity:
            return cart[self.item.code] * (self.item.price - self.new_price)

        return 0

    def __str__(self):
        return 'Type2(item_code=%s, old_price=%s, new_price=%s, quantity=%s)' % (self.item.code, self.item.price, self.new_price, self.quantity)


class Type3(Discount):
    '''
    This discount is applied when an item is purchased, another item is given for free.
    '''

    def __init__(self, item, freebie):
        self.item = item    
        self.freebie = freebie

    def discount_amount(self, cart):
        if self.item.code in cart and self.freebie.code in cart:
            return min(cart[self.item.code], cart[self.freebie.code]) * self.freebie.price
        return 0

    def __str__(self):
        return 'Type3(item_code=%s, freebie_code=%s, freebie_price=%s)' % (self.item.code, self.freebie.code, self.freebie.price)
