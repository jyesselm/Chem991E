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
    def test_standard(self):
        d = {'test' : 1, 'test2' : 2}
        count = count_key_values(d,['test', 'test2'])
        self.assertEqual(count, 3)

    def test_error(self):
        d = {'test': 1, 'test2': 2}
        with self.assertRaises(CountKeyException):
            count = count_key_values(d, ['test', 'test1'])


unittest.main()


