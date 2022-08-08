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
    def __init__(self, fen:str="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") -> None: #board color_to_move casteling_rights en_passant half_moves full_moves
        self.__board:dict = self.__from_fen(fen.split(' ')[0])
        self.__turn:bool = BLACK if fen.split(' ')[1] == 'b' else WHITE
        self.__castle_rights:str = fen.split(' ')[2]
        self.__en_passant:str = fen.split(' ')[3]
        self.__half_moves:int = int(fen.split(' ')[4])
        self.__full_moves:int = int(fen.split(' ')[5])

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
        res += ' ' + ('b' if self.__turn == BLACK else 'w')
        return res #TODO

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


class Piece:
    def __init__(self, position:Position, color:int) -> None:
        self.__position = position
        self.__color = color

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
    def color(self):
        return self.__color

    @property
    def name(self):
        return self.__class__.__name__

class King(Piece):
    def __str__(self):
        return 'k' if self.color == BLACK else 'K'

class Queen(Piece):
    def __str__(self):
        return 'q' if self.color == BLACK else 'Q'

class Rook(Piece):
    def __str__(self):
        return 'r' if self.color == BLACK else 'R'

class Knight(Piece):
    def __str__(self):
        return 'n' if self.color == BLACK else 'N'

class Bishop(Piece):
    def __str__(self):
        return 'b' if self.color == BLACK else 'B'

class Pawn(Piece):
    def __str__(self):
        return 'p' if self.color == BLACK else 'P'