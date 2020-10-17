# Using instance methods and attributes

class Book:
    def __init__(self, title, pages, author, price):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.__secret = "This is a secret attribute"

    # first argument as the object ("self" is just a convention)
    def setDiscount(self, amount):
        self._discount = amount

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


# create some book instances
b1 = Book("abc", "xyz", 125, 30.99)
b2 = Book("pqr", "lmn", 254, 99.99)

# print the price of book1
print(b1.getPrice())

# try setting the discount
print(b2.getPrice())
b2.setDiscount(0.25)
print(b2.getPrice())

# properties with double underscores are hidden by the interpreter
print(b2._discount)
# print(b2.__secret) # Error
# print(b2._Book__secret) # Prints self.__secret