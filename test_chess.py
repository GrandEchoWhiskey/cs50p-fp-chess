from chess import Color, Position, Board, King, Queen, Rook, Knight, Bishop, Pawn
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
        self.assertRaises(ValueError, Position._Position__validate, 8)

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

    def test_init(self):
        board1 = Board()
        board2 = Board({'e1': King(Color.WHITE), 'd2': Pawn(Color.WHITE)})
        self.assertEqual(board1._Board__pieces['a2'].color, Color.WHITE)
        self.assertEqual(board1._Board__pieces['a2'].name, "Pawn")
        self.assertEqual(board1._Board__pieces['a2'].color, Color.WHITE)
        self.assertEqual(board1._Board__pieces['a2'].name, "Pawn")
        self.assertEqual(board1._Board__pieces['d4'], None)
        self.assertEqual(board2._Board__pieces['e1'].color, Color.WHITE)
        self.assertEqual(board2._Board__pieces['e1'].name, "King")
        self.assertEqual(board2._Board__pieces['d2'].color, Color.WHITE)
        self.assertEqual(board2._Board__pieces['d2'].name, "Pawn")
        self.assertEqual(board2._Board__pieces['a8'], None)

    def test_from_fen(self):
        board = Board.from_fen()
        self.assertEqual(board._Board__pieces['e1'].color, Color.WHITE)
        self.assertEqual(board._Board__pieces['e1'].name, "King")
        self.assertEqual(board._Board__pieces['d8'].color, Color.BLACK)
        self.assertEqual(board._Board__pieces['d8'].name, "Queen")
        self.assertEqual(board._Board__pieces['d2'].color, Color.WHITE)
        self.assertEqual(board._Board__pieces['d2'].name, "Pawn")
        self.assertEqual(board._Board__pieces['c8'].color, Color.BLACK)
        self.assertEqual(board._Board__pieces['c8'].name, "Bishop")
        self.assertEqual(board._Board__pieces['a8'].color, Color.BLACK)
        self.assertEqual(board._Board__pieces['a8'].name, "Rook")
        self.assertEqual(board._Board__pieces['b1'].color, Color.WHITE)
        self.assertEqual(board._Board__pieces['b1'].name, "Knight")
        self.assertRaises(ValueError, Board.from_fen, "rnbqkbnr/pp1ppppp/8/2p5/4P3/6N2/PPPP1PPP/RNBQKB1R") #Invalid 6N2 -> 9
        self.assertRaises(ValueError, Board.from_fen, "rnbqkbnr/pp1ppppp/8/2p5/4C3/5N2/PPPP1PPP/RNBQKB1R") #Invalid 4C3 -> C
        self.assertRaises(ValueError, Board.from_fen, "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R/4B3") #Invalid 4B3 -> 9

    def test_fen(self):
        board1 = Board.from_fen()
        board2 = Board.from_fen("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")
        self.assertEqual(board1.fen, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        self.assertEqual(board2.fen, "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")

    def test_move(self):
        board = Board.from_fen()
        board.move(Position.from_str('e2'), Position.from_str('e4'))
        board.move(Position.from_str('e7'), Position.from_str('e5'))
        board.move(Position.from_str('g1'), Position.from_str('f3'))
        board.move(Position.from_str('b8'), Position.from_str('c6'))
        board.move(Position.from_str('f1'), Position.from_str('c4'))
        self.assertEqual(board.fen, "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R")

    def test_replace(self):
        board = Board({'e8': Pawn(Color.WHITE)})
        board.replace(Position.from_str('e8'), Queen(Color.WHITE))
        self.assertEqual(board.fen, "4Q3/8/8/8/8/8/8/8")


class TestSum_Piece(unittest.TestCase):

    def test_pawn_moves(self):

        # 2nd and 7th row
        board = Board()
        self.assertEqual(len(board.pieces['e2'].moves(board, Position.from_str('e2'))), 2)
        self.assertEqual(len(board.pieces['e7'].moves(board, Position.from_str('e7'))), 2)

        # En Passant
        board1 = Board({'e5':Pawn(Color.WHITE), 'd7':Pawn(Color.BLACK)})
        board2 = Board({'e4':Pawn(Color.BLACK), 'd2':Pawn(Color.WHITE)})
        board3 = Board({'e4':Pawn(Color.BLACK), 'd2':Pawn(Color.BLACK)})
        board1.move(Position.from_str('d7'), Position.from_str('d5'))
        board2.move(Position.from_str('d2'), Position.from_str('d4'))
        board3.move(Position.from_str('d2'), Position.from_str('d4')) # Theoretical
        self.assertEqual(len(board1.pieces['e5'].moves(board1, Position.from_str('e5'))), 2)
        self.assertEqual(len(board1.pieces['d5'].moves(board1, Position.from_str('d5'))), 1)
        self.assertEqual(len(board2.pieces['e4'].moves(board2, Position.from_str('e4'))), 2)
        self.assertEqual(len(board3.pieces['e4'].moves(board3, Position.from_str('e4'))), 1)
        


if __name__ == '__main__':
    unittest.main()