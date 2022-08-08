print('Chess Engine created by: Eric Wolf')

WHITE = 0
BLACK = 1

class Position:
    """
    Postioning on board and vector math
    """
    __alpha:str = "abcdefgh"
    __numbr:str = "12345678"

    def __init__(self, square:str) -> None:
        self.__pos:tuple = self.__from_str(square)

    def __from_str(self, string) -> tuple:
        try:
            return tuple((self.__alpha.index(string[0]), self.__numbr.index(string[1])))

        except:
            raise ValueError

    def __str__(self) -> str:
        return self.__alpha[self.__pos[0]] + self.__numbr[self.__pos[1]]

    def __eq__(self, other) -> bool:
        return self.position == other.position

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @classmethod
    def from_tuple(cls, t:tuple):
        if len(t) != 2:
            raise ValueError
        if t[0] > 8 or t[0] < 1:
            raise ValueError
        if t[1] > 8 or t[1] < 1:
            raise ValueError
        return cls(cls.__alpha[t[0]] + cls.__numbr[t[1]])

    def at(self, vector:tuple):
        try:
            if len(vector) != 2:
                raise ValueError
            return self.__class__.from_tuple((self.position[0] + vector[0], self.position[1] + vector[1]))
        except:
            return None

    @property
    def position(self) -> tuple:
        return self.__pos


class Board:
    """
    Board - All needed information about the board state - such as the board itself, 
    current colors turn, casteling rights, en passant, halfmoves made and the full moves
    """
    def __init__(self, fen:str="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") -> None:
        try:
            self.__board:dict = self.__from_fen(fen.split(' ')[0])
            self.__turn:bool = BLACK if fen.split(' ')[1] == 'b' else WHITE
            self.__castle_rights:str = fen.split(' ')[2]
            self.__en_passant:str = fen.split(' ')[3]
            self.__half_moves:int = int(fen.split(' ')[4])
            self.__full_moves:int = int(fen.split(' ')[5])
            self.__history:list = []
        except:
            return ValueError

    def __remove_castle(self, char:str) -> None:
        self.__castle_rights = self.__castle_rights.replace(char, '')
        if not len(self.__castle_rights):
            self.__castle_rights = '-'

    def __set_en_passant(self, square:str='-') -> None:
        self.__en_passant = square

    def __swap_turn(self):
        self.__turn = BLACK if self.__turn == WHITE else WHITE

    def play(self, from_str:str, to_str:str) -> bool:
        if not self.board[from_str]:
            return False
        if self.turn != self.board[from_str].color:
            return False

    def __is_draw_rounds(self) -> bool:
        if self.__half_moves >= 100:
            return True
        return False

    @property
    def fen(self) -> str:
        res:str = ""
        for y in range(8):
            for x in range(8):
                if self.__board[str(Position.from_tuple((x, 7-y)))]:
                    res += str(self.__board[str(Position.from_tuple((x, 7-y)))])
                else:
                    res += ' '
            res += '/' if y < 7 else ''
        for i in range(8, 0):
            res = res.replace(' ' * i, int(i))
        res += ' ' + ('b' if self.__turn == BLACK else 'w') + ' ' + self.__castle_rights + \
            ' ' + self.__en_passant + ' ' + str(self.__half_moves) + ' ' + str(self.__full_moves)
        return res

    def __from_fen(self, short_fen) -> dict:
        res:dict = {}
        for i in range(8, 0):
            short_fen = short_fen.replace(str(i), ' ' * i)
        for y, row in enumerate(short_fen.split('/')):
            for x, piece in enumerate(row):
                cls = Piece.child(piece)
                if not cls:
                    self.__board[str(Position.from_tuple((x, 7-y)))] = None
                    continue
                color = BLACK if piece.islower() else WHITE
                self.__board[str(Position.from_tuple((x, 7-y)))] = cls(Position.from_tuple((x, 7-y)), color)
        return res

    @property
    def turn(self) -> bool:
        return self.__turn
    
    @property
    def board(self) -> dict:
        return self.__board

    @property
    def castle_rights(self) -> str:
        return self.__castle_rights

    @property
    def en_passant(self) -> Position:
        return Position(self.__en_passant)


class Piece:
    def __init__(self, position:Position, color:bool) -> None:
        self.__position:Position = position
        self.__color:bool = color

    @classmethod
    def child(cls, c:str):
        if c.lower() == 'k':
            return King
        if c.lower() == 'q':
            return Queen
        if c.lower() == 'r':
            return Rook
        if c.lower() == 'n':
            return Knight
        if c.lower() == 'b':
            return Bishop
        if c.lower() == 'p':
            return Pawn
        return None

    @property
    def position(self) -> Position:
        return self.__position

    @property
    def color(self) -> bool:
        return self.__color

    @property
    def name(self) -> str:
        return self.__class__.__name__


class King(Piece):
    def __str__(self) -> str:
        return 'k' if self.color == BLACK else 'K'

    def moves(self, board:Board) -> list:
        res:list = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x or y):
                    continue
                if piece := board.board[str(self.position.at((x, y)))]:
                    if piece.color == self.color:
                        continue
                res += self.position.at((x, y))
        return res


class Rook(Piece):
    def __str__(self) -> str:
        return 'r' if self.color == BLACK else 'R'

    def moves(self, board:Board) -> list:
        res:list = []

        for t in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for xy in range(1, 8):
                if piece := board.board[str(self.position.at((xy * t[0], xy * t[1])))]:
                    if piece.color == self.color:
                        break
                    res += self.position.at((xy * t[0], xy * t[1]))
                    break
                res += self.position.at((xy * t[0], xy * t[1]))

        return res


class Bishop(Piece):
    def __str__(self) -> str:
        return 'b' if self.color == BLACK else 'B'

    def moves(self, board:Board) -> list:
        res:list = []

        for t in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for xy in range(1, 8):
                if piece := board.board[str(self.position.at((xy * t[0], xy * t[1])))]:
                    if piece.color == self.color:
                        break
                    res += self.position.at((xy * t[0], xy * t[1]))
                    break
                res += self.position.at((xy * t[0], xy * t[1]))

        return res


class Queen(Rook, Bishop):
    def __str__(self) -> str:
        return 'q' if self.color == BLACK else 'Q'

    def moves(self, board:Board) -> list:
        rook_moves:list = Rook.moves(self, board)
        bishop_moves:list = Bishop.moves(self, board)
        return rook_moves.extend(bishop_moves)


class Knight(Piece):
    def __str__(self) -> str:
        return 'n' if self.color == BLACK else 'N'

    def moves(self, board:Board) -> list:
        res:list = []

        for i in [-2, 2]:
            for j in [-1, 1]:
                if piece := board.board[str(self.position.at((i, j)))]:
                    if piece.color == self.color:
                        continue
                res += self.position.at((i, j))

        for i in [-2, 2]:
            for j in [-1, 1]:
                if piece := board.board[str(self.position.at((j, i)))]:
                    if piece.color == self.color:
                        continue
                res += self.position.at((j, i))

        return res


class Pawn(Piece):
    def __str__(self) -> str:
        return 'p' if self.color == BLACK else 'P'

    def moves(self, board:Board) -> list:
        res:list = []

        y_vector:int = 1 if self.color == WHITE else -1
        if not (piece1 := board.board[str(self.position.at((0, y_vector)))]):
            if piece2 := board.board[str(self.position.at((0, y_vector)))]:

        return res