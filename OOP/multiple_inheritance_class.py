# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "Good Day"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "Gutten Tag"
        self.name = "Class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


# create the class and call showname()
c = C()
print(C.__mro__)
c.showprops()