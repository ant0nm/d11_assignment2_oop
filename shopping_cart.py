# link up the two classes
from product import Product
from tax import TaxManager

class ShoppingCart:

    """ A class representing a simple shopping cart that can store products """

    def __init__(self, products):
        self.products = products

    def __str__(self):
        str_list = ""
        str_list += "Your Cart:\n"
        for product, num in self.products.items():
            str_list += "* {}: {}\n".format(product.name, num)
        return str_list

    def add(self, product):
        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = 1

    def remove(self, product):
        if product in self.products:
            self.products[product] -= 1
        else:
            self.products.pop(product)

    def total_price_before_tax(self):
        total_before_tax = 0
        for product, num in self.products.items():
            total_before_tax += product.base_price * num
        return total_before_tax

    def total_price_after_tax(self):
        total_after_tax = 0
        for product, num in self.products.items():
            total_after_tax += product.total_price() * num
        return total_after_tax

    def most_expensive_product(self):
        max_price = 0
        max_product = None
        for product in self.products.keys():
            if product.total_price() > max_price:
                max_price = product.total_price()
                max_product = product
        return max_product

# create a tax manager
taxes = TaxManager({"standard": 0.13, "tax exempt": 0.05, "imported": 0.18})

# instantiating a shopping cart, initializing and printing it
eggs = Product("eggs", 3, taxes.getRate("standard")) # total price = 3.3
milk = Product("milk", 2, taxes.getRate("standard")) # total price = 2.26
bacon = Product("bacon", 5, taxes.getRate("tax exempt")) # total price = 5.25
product_list = {eggs: 1, milk: 2, bacon: 3}
cart = ShoppingCart(product_list)
print(cart)

# adding 2 more products
butter = Product("butter", 1, taxes.getRate("standard")) # total price = 1.13
tuna = Product("tuna", 9, taxes.getRate("imported")) # total price = 10.17
cart.add(butter)
cart.add(tuna)
print()
print(cart)

# removing 1 product
cart.remove(milk)
print()
print(cart)

# total price of cart before tax
print()
print("The total price of your cart BEFORE TAX is: {}".format(cart.total_price_before_tax()))

# total price of cart after tax
# expecting $19.85
print()
print("The total price of your cart AFTER TAX is: {}".format(cart.total_price_after_tax()))

# get the most expensive product in the cart
max_price_product = cart.most_expensive_product()
print()
print("Most expensive product in the cart:")
print(max_price_product)
