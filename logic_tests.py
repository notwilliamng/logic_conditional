import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        is_even(0)
        in_an_interval(0)

    def test_is_even(self):
    	self.assertAlmostEqual(is_even(5), False)
    	self.assertAlmostEqual(is_even(79), False)
    	self.assertAlmostEqual(is_even(56), True)

    def test_in_an_interval(self):
    	self.assertEqual(in_an_interval(5),True)
    	self.assertEqual(in_an_interval(49),True)
    	self.assertEqual(in_an_interval(7),True)
    	self.assertEqual(in_an_interval(100),False)
    	self.assertEqual(in_an_interval(11),False)
    	self.assertEqual(in_an_interval(60),True)
    	self.assertEqual(in_an_interval(100000),False)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

