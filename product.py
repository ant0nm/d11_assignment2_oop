class Product:

    """ A class representing a product that can be purchased """

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def __str__(self):
        return "Product: {}\tBase Price: {}\tTax Rate: {}".format(self.name, self.base_price, self.tax_rate)

    def total_price(self):
        return round(self.base_price * (1 + self.tax_rate), 2)

# testing out the Product class
eggs = Product("eggs", 3, 0.10)
print(eggs)
print(eggs.total_price())
