from chess import Color, Position
import unittest


class TestSum_Color(unittest.TestCase):

    def test_color_different(self):
        self.assertNotEqual(Color.WHITE, Color.BLACK)


class TestSum_Position(unittest.TestCase):

    def test_init(self):
        pos = Position(0, 7)
        self.assertEqual(pos._Position__x_index, 0)
        self.assertEqual(pos._Position__y_index, 7)

    def test_init_valueerror(self):
        self.assertRaises(ValueError, Position, -1, 0)
        self.assertRaises(ValueError, Position, 0, -1)
        self.assertRaises(ValueError, Position, 9, 0)
        self.assertRaises(ValueError, Position, 0, 9)

    def test_from_chars(self):
        pos = Position.from_chars('a', '4')
        self.assertEqual(pos._Position__x_index, 0)
        self.assertEqual(pos._Position__y_index, 3)

    def test_from_chars_valueerror(self):
        self.assertRaises(ValueError, Position.from_chars, '', '3')
        self.assertRaises(ValueError, Position.from_chars, 'b', '')
        self.assertRaises(ValueError, Position.from_chars, '4', 'c')
        self.assertRaises(ValueError, Position.from_chars, 'h', '0')
        self.assertRaises(ValueError, Position.from_chars, 'i', '1')
        self.assertRaises(ValueError, Position.from_chars, 'a', '9')

    def test_from_str(self):
        pos = Position.from_str('d4')
        self.assertEqual(pos._Position__x_index, 3)
        self.assertEqual(pos._Position__y_index, 3)

    def test_from_str_valueerror(self):
        self.assertRaises(ValueError, Position.from_str, '')
        self.assertRaises(ValueError, Position.from_str, 'c')
        self.assertRaises(ValueError, Position.from_str, '1')
        self.assertRaises(ValueError, Position.from_str, 'cd')
        self.assertRaises(ValueError, Position.from_str, '32')
        self.assertRaises(ValueError, Position.from_str, 'h0')
        self.assertRaises(ValueError, Position.from_str, 'i1')
        self.assertRaises(ValueError, Position.from_str, 'a9')
        self.assertRaises(ValueError, Position.from_str, 'c 2')
        self.assertRaises(ValueError, Position.from_str, 'c2 ')
        self.assertRaises(ValueError, Position.from_str, ' c2')

    def test_str(self):
        pos = Position.from_str('a4')
        self.assertEqual(str(pos), 'a4')

    def test_equal(self):
        pos1 = Position.from_str('b2')
        pos2 = Position.from_str('b2')
        pos3 = Position.from_str('c3')
        self.assertEqual(pos1 == pos2, True)
        self.assertEqual(pos1 == pos3, False)

    def test_not_equal(self):
        pos1 = Position.from_str('c3')
        pos2 = Position.from_str('b2')
        pos3 = Position.from_str('c3')
        self.assertEqual(pos1 != pos2, True)
        self.assertEqual(pos1 != pos3, False)

    def test_validate_index(self):
        self.assertEqual(Position._Position__validate(0), 0)
        self.assertEqual(Position._Position__validate(7), 7)
        self.assertRaises(ValueError, Position._Position__validate, -1)
        self.assertRaises(ValueError, Position._Position__validate, 9)

    def test_names(self):
        pos = Position.from_str('a2')
        self.assertEqual(pos.xName, 'a')
        self.assertEqual(pos.yName, '2')

    def test_neighbor(self):
        pos1 = Position.from_str('a1')
        pos2 = Position.from_str('h8')
        self.assertEqual(Position.neighbor(pos1, y=1), Position.from_str('a2'))
        self.assertEqual(Position.neighbor(pos1, x=2, y=1), Position.from_str('c2'))
        self.assertEqual(Position.neighbor(pos1, y=-1), None)
        self.assertEqual(Position.neighbor(pos2, x=-1, y=-1), Position.from_str('g7'))
        self.assertEqual(Position.neighbor(pos2, x=1, y=1), None)
        

class TestSum_Board(unittest.TestCase):
    
    def blank(self):
        pass

if __name__ == '__main__':
    unittest.main()