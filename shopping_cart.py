# link up the two classes
from product import Product

class ShoppingCart:

    """ A class representing a simple shopping cart that can store products """

    def __init__(self, products):
        self.products = products

    def __str__(self):
        str_list = ""
        for index, product in enumerate(self.products):
            if index == 0:
                str_list += "Your Cart:\n* {}".format(product.name)
            else:
                str_list += "\n* {}".format(product.name)
        return str_list

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)

    def total_price_before_tax(self):
        total_before_tax = 0
        for product in self.products:
            total_before_tax += product.base_price
        return total_before_tax

    def total_price_after_tax(self):
        total_after_tax = 0
        for product in self.products:
            total_after_tax += product.total_price()
        return total_after_tax

    def most_expensive_product(self):
        max_price = 0
        max_product = None
        for product in self.products:
            if product.total_price() > max_price:
                max_price = product.total_price()
                max_product = product
        return max_product

# instantiating a shopping cart, initializing and printing it
eggs = Product("eggs", 3, 0.10) # total price = 3.3
milk = Product("milk", 2, 0.13) # total price = 2.26
bacon = Product("bacon", 5, 0.05) # total price = 5.25
product_list = [eggs, milk, bacon]
cart = ShoppingCart(product_list)
print(cart)

# adding 2 more products
butter = Product("butter", 1, 0.13) # total price = 1.13
tuna = Product("tuna", 9, 0.13) # total price = 10.17
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
