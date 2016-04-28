#Test suite for super_sum
from unittest import TestCase
from super_sum import super_sum

class  SuperSumTestCase(TestCase):
	"""Test Case for super_sum."""

	#test empty input
	def test_empty_input(self):
		self.assertEqual(super_sum(), 0)

		#Test sum of integers
	def test_sum_of_integers(self):
		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 20, 30), 100)

		#Test sum of numbers in a lisrt
	def test_sum_of_items_in_one_list(self):
		self.assertEqual(super_sum([1, 2, 3]), 6)

		#Tesy sum of a string
	def test_string_input_returns(self):
		self.assertEqual(super_sum('string'), 0)