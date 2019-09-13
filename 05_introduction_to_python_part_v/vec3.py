import math

class Vector3:
    """
    A class that represents 3D vectors with x, y and z coordinates
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector3(x=" + str(self.x) + ",y=" + str(self.y) + ",z=" + str(self.z) + ")"

    def __add__(self, other):

        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # python2.7
    def __div__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other):
        """
        computes the distance between the current vector and other vector object

        Args:
            other: another Vector3 object

        Returns:
            the euclidean distance between the current vector and the other vector
        """

        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y ) ** 2 +
                         (self.z - other.z) ** 2)

    def dot(self, other):
        """
        computes the dot product between the current vector and other vector object

        Args:
            other: another Vector3 object

        Returns:
            the dot product between the current vector and the other vector
        """

        return self.x * other.x + self.y * other.x + self.z * other.z

    def negated(self):
        """
         Negates the current vector

         Returns:
             None
        """

        return Vector3(-self.x, -self.y, -self.z)

    def magnitude(self):
        """
        computes the magnitude of the current vector

        Returns:
            The magnitude of the vector
        """

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalize(self):
        """
         Normalizes the current vector

         Returns:
             None
        """


        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        self.z /= mag


