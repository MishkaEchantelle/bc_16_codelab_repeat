import unittest
from primeNumbers import primeNumbers

class TestSolution(unittest.TestCase):
	"""docstring for TestSolution"""
	def test_negative(self):
		self.assertFalse(primeNumbers (num = 0),)
	def test_alphabet(self):
		self.assertTrue(type, int)
	def test_one(self):
		self.assertFalse(primeNumbers (num =1),)
	def test_string(self):
		self.assertTrue(type, int)
	def test_notOne(self):
		self.assertFalse(primeNumbers (num =1),)

if __name__ == '__main__':
	unittest.main()