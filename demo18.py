def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print average([20, 30, 70])
    42.0
    """
    return sum(values, 0.0) / len(values)

#import doctest
#doctest.testmod()

#if __name__ == '__main__':
    #print average([20, 30, 70])

import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main()




