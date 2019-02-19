from tax import TaxManager

class Product:

    """ A class representing a product that can be purchased """

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def __str__(self):
        return "Product: {}".format(self.name)

    def total_price(self):
        return round(self.base_price * (1 + self.tax_rate), 2)

# testing out the Product class
taxes = TaxManager({"standard": 0.13, "tax exempt": 0.05, "imported": 0.18})
eggs = Product("eggs", 3, taxes.getRate("standard"))
print(eggs)
print(eggs.total_price())
