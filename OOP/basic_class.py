# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
book1 = Book("Hardy Boys")
book2 = Book("Nancy Drew")

# TODO: print the class and property
print(book1)
print(book1.title)
