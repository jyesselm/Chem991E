class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length


def example_1():
    rect = Rectangle(5.0, 4.0)
    print(rect.width)
    print(rect.length)


def example_2():
    rect = Rectangle(5.0, 4.0)
    print(rect.area())


def example_3():
    rect = Rectangle(5.0, 4.0)
    rect.width = 10.0
    print(rect.area())

