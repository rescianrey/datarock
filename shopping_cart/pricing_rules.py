class PricingRules(object):
    def __init__(self, catalogue, discounts):
        self.catalogue = catalogue
        self.discounts = discounts

    def __str__(self):
        return 'PricingRules(catalogue=%s, discounts=%s)' % (self.items, self.discounts)
