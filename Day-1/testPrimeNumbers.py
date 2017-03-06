import unittest
from primeNumbers import primeNumbers

class TestSolution(unittest.TestCase):
	"""docstring for TestSolution"""
	def test_negative(self):
		self.assertFalse(primeNumbers (num = 0),)
	def test_alphabet(self):
		self.assertTrue(type, int)