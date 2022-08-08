from operator import pos
import chess
import unittest


class TestSum_Color(unittest.TestCase):

    def test_color_different(self):
        self.assertEqual(str(chess.Position('a2')), 'a2')

    def test2(self):
        self.assertEqual(chess.Bishop(chess.Position('a2')).name, "Bishop")


if __name__ == '__main__':
    unittest.main()