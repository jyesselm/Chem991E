import unittest

class CountKeyException(Exception):
    pass

def count_key_values(d, keys):
    count = 0

    for k in keys:
        if k not in d:
            raise CountKeyException(k + " not in dictionary!")
        count += d[k]

    return count



class CountKeyUnittest(unittest.TestCase):
    pass



unittest.main()


