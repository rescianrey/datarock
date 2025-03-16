from checkout import Checkout
from item import Item
from discount import Type1, Type2, Type3
from pricing_rules import PricingRules


def main():
#       SKU	Name	Price
#   ipd	Super iPad	$549.99
#   mbp	MacBook Pro	$1399.99
#   atv	Apple TV	$109.50
#   vga	VGA adapter	$30.00

    items = [
        Item('ipd', 'Super iPad', 549.99),
        Item('mbp', 'MacBook Pro', 1399.99),
        Item('atv', 'Apple TV', 109.50),
        Item('vga', 'VGA adapter', 30.00)
    ]
#we're going to have a 3 for 2 deal on Apple TVs. For example, if you buy 3 Apple TVs, you will pay the price of 2 only (type 1)
#the brand new Super iPad will have a bulk discounted applied, where the price will drop to $499.99 each, if someone buys more than 4 (type 2)
#we will bundle in a free VGA adapter free of charge with every MacBook Pro sold (type 3)
    discounts = [
        Type1('atv', 109.50, 3, 2),
        Type2('ipd', 4, 549.99, 499.99),
        Type3('mbp', 'vga', 30.00)
    ]
    
    catalog = {}
    for item in items:
        catalog[item.code] = item
    pricing_rules = PricingRules(catalog, discounts)
    print(pricing_rules)

    # sample checkout
    checkout = Checkout(pricing_rules)
    checkout.scan('atv')
    checkout.scan('atv')
    checkout.scan('atv')
    checkout.scan('vga')
    print(checkout.total())


    checkout.reset()
    checkout.scan('atv')
    checkout.scan('ipd')
    checkout.scan('ipd')
    checkout.scan('atv')
    checkout.scan('ipd')
    checkout.scan('ipd')
    checkout.scan('ipd')
    print(checkout.total())


    checkout.reset()
    checkout.scan('mbp')
    checkout.scan('vga')
    checkout.scan('ipd')
    print(checkout.total())

if __name__ == "__main__":
    main()



