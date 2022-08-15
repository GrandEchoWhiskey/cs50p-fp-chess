from chess import WHITE, BLACK, Position, Board, Piece, King, Queen, Rook, Bishop, Knight, Pawn
import unittest


class TestSum_Position(unittest.TestCase):

	def test_init(self):
		position = Position('a5')
		self.assertEqual(str(position), 'a5')
		self.assertRaises(TypeError, Position, None)
		self.assertRaises(ValueError, Position, '')
		self.assertRaises(ValueError, Position, 's3')
		self.assertRaises(ValueError, Position, 'c0')
		self.assertRaises(ValueError, Position, '4c')
		self.assertRaises(ValueError, Position, 'a23')
		
	def test_from_tuple(self):
		position = Position.from_tuple((2, 3))
		self.assertEqual(str(position), 'c4')
		self.assertRaises(ValueError, Position.from_tuple, (8, 2))
		self.assertRaises(ValueError, Position.from_tuple, (2, 8))
		self.assertRaises(ValueError, Position.from_tuple, (-1, 0))
		self.assertRaises(ValueError, Position.from_tuple, (0, -1))
		self.assertRaises(ValueError, Position.from_tuple, 'a4')
		self.assertRaises(ValueError, Position.from_tuple, (3, 3, 1))
		
class TestSum_Board(unittest.TestCase):
	def test_color_different(self):
		self.assertEqual(str(Position('a2')), 'a2')

	def test2(self):
		self.assertEqual(Bishop(Position('a2'), WHITE).name, "Bishop")


if __name__ == '__main__':
    unittest.main()