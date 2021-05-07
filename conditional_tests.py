import unittest
from conditional import *

class TestCases(unittest.TestCase):
	def test_function_names(self):
		max_101(0, 0)
		max_of_three(0, 0, 0)
		rental_late_fee(0)

	def test_max101(self):
		self.assertEqual(max_101(0,1),1)
		self.assertEqual(max_101(1000,134),1000)
		self.assertEqual(max_101(7,2),7)

	def test_max_of_three(self):
		self.assertEqual(max_of_three(7,2,8),8)
		self.assertEqual(max_of_three(7,2,3),7)
		self.assertEqual(max_of_three(7,2,1),7)
		self.assertEqual(max_of_three(7,2,0),7)


	def rental_late_fee(self):
		self.assertEqual(rental_late_fee(7),5)
		self.assertAlmostEqual(rental_late_fee(166),100)
		self.assertAlmostEqual(rental_late_fee(16),7)
		self.assertAlmostEqual(rental_late_fee(26),19)




# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

