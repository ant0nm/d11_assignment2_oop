class TaxManager:

    """ A class that manages different tax rates """

    def __init__(self, taxes):
        self.taxes = taxes

    def getRate(self, type):
        return self.taxes[type]
