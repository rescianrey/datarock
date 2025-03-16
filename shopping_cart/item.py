class Item(object):
    '''
    Item in the catalogue.
    '''
    def __init__(self, code, name, price):
        self.price = price
        self.name = name
        self.code = code

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

