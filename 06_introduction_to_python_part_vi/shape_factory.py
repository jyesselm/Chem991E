import random
import math


class Shape(object):
    def __init__(self):
        pass

    def shape_type(self):
        # return a string of what type of shape this is "circle", "square"
        pass

    def area(self):
        # returns area
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def shape_type(self):
        """returns a string version of the class name

        Returns:
            a string with the name of the class

        """
        return "circle"

    def area(self):
        """computes the area of the shape

        Returns:
            returns a number which is the computed value of the shape

        """
        return self.radius*self.radius*math.pi


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def shape_type(self):
        """returns a string version of the class name

        Returns:
              a string with the name of the class

          """
        return "square"

    def area(self):
        """computes the area of the shape

        Returns:
            returns a number which is the computed value of the shape

               """
        return self.length*self.length


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def shape_type(self):
        """returns a string version of the class name

        Returns:
              a string with the name of the class

          """
        return "rectangle"

    def area(self):
        """computes the area of the shape

        Returns:
            returns a number which is the computed value of the shape

        """
        return self.width*self.height


class ShapeFactory(object):
    def get_shape(self, name):
        """returns a shape object with the class name equal to the supplied name

        Args:
            name: the name of the class type, e.g. "circle", "square", "rectange"

        Returns:
            returns a shape object

        """

        if name == "circle":
            return Circle(random.randint(1, 10))

        elif name == "square":
            return Square(random.randint(1, 10))

        elif name == "rectangle":
            return Rectangle(random.randint(1, 10), random.randint(1, 10))

    def get_random_shape(self):
        """returns a random shape object

        Returns:
            returns a shape object

        """

        shape_name = random.choice(["circle", "square", "rectangle"])
        return self.get_shape(shape_name)















