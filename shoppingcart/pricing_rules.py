class PricingRules(object):
    '''
    Pricing rules. Contains a catalogue of items and a list of discounts.
    '''
    def __init__(self, catalogue, discounts):
        self.catalogue = catalogue
        self.discounts = discounts

    def __str__(self):
        return 'PricingRules(catalogue=%s, discounts=%s)' % (self.catalogue, self.discounts)
