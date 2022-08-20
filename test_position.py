import unittest
from position import position
from vector import vector

class TestSum_Position(unittest.TestCase):
	
	def test_init(self):
		p = position(3, 5)
		self.assertEqual(p.as_tuple, (3, 5))
		self.assertRaises(TypeError, positiom)

if __name__ == "__main__":
	unittest.main()