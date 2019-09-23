import unittest

class ListAddException(Exception):
    pass

def list_addition(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ListAddException("lists are not the same length")

    list_3 = []
    for i in range(len(list_1)):
        list_3.append(list_1[i] + list_2[i])

    return list_3


class ListAdditionUnittest(unittest.TestCase):
    def test_standard(self):
        l1 = [0, 2, 2]
        l2 = [2, 1, 1]
        l3 = list_addition(l1, l2)
        self.assertListEqual(l3, [2, 3, 3])

    def test_equal_length(self):
        l1 = [0, 2, 2, 2]
        l2 = [0, 2]
        with self.assertRaises(ListAddException):
            list_addition(l1, l2)


unittest.main()