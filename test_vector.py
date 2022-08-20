import unittest
from vector import vector

class TestSum_Vector(unittest.TestCase):
	
	def test_init(self):
		v = vector(3.53, -2)
		self.assertEqual(v.x, 3.53)
		self.assertEqual(v.y, -2)
		self.assertRaises(TypeError, vector, 'not.int', 'or float')
		
	def test_eq(self):
		v = vector(2, 4)
		self.assertTrue(v == vector(2, 4))
		self.assertFalse(v == vector(9, 1))
		
	def test_ne(self):
		v = vector(4, 3)
		self.assertTrue(v != vector(2, 5))
		self.assertFalse(v != vector(4, 3))
		
	def test_add(self):
		v1 = vector(3, 5)
		v2 = vector(2, -1)
		self.assertEqual(v1+v2, vector(5, 4))
		
	def test_sub(self):
		v1 = vector(5, 2)
		v2 = vector(2, 4)
		self.assertEqual(v1-v2, vector(3, -2))
		
	def test_mul(self):
		v1 = vector(2, -1)
		v2 = vector(4, 2)
		self.assertEqual(v1*v2, vector(8, -2))
		
	def test_pow(self):
		v1 = vector(2, -2)
		v2 = vector(4, 2)
		self.assertEqual(v1**v2, vector(16, 4))
		
	def test_truediv(self):
		v1 = vector(6, 4)
		v2 = vector(3, 5)
		self.assertEqual(v1/v2, vector(2, 0.8))
		
	def test_floordiv(self):
		v1 = vector(6, 4)
		v2 = vector(3, 5)
		self.assertEqual(v1//v2, vector(2, 0))
		
	def test_mod(self):
		v1 = vector(15, 11)
		v2 = vector(10, 3)
		self.assertEqual(v1%v2, vector(5, 2))
		
	def test_str(self):
		self.assertIsInstance(str(vector(3, 4)), str)
		
	def test_tuple(self):
		v = vector.tuple((3, 5))
		self.assertEqual(v, vector(3, 5))
		self.assertRaises(ValueError, vector.tuple, (3, 5, 9))
		
	def test_get(self):
		class tmp:
			v = vector(3, 4)
		self.assertEqual(tmp.v, (3, 4))
		self.assertRaises(Ty
		
	def test_hash(self):
		pass
		
		
if __name__ == "__main__":
	unittest.main()