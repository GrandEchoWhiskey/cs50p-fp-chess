from enum import Enum
from copy import deepcopy

class Color(Enum):
    WHITE = 0
    BLACK = 1


class Position():

    def __init__(self, x_index:int, y_index:int):
        self.__x_index = self.__validate(x_index)
        self.__y_index = self.__validate(y_index)

    def __eq__(self, other):
        if self.xIndex != other.xIndex:
            return False
        if self.yIndex != other.yIndex:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{chr(ord('a')+self.xIndex)}{str(1+self.yIndex)}"

    @classmethod
    def neighbor(cls, obj, x=0, y=0):
        try:
            return cls(obj.xIndex + x, obj.yIndex + y)
        except:
            return None

    @classmethod
    def from_chars(cls, xPos:str, yPos:str):
        xnames = [chr(x) for x in range(ord('a'), ord('h') + 1)]
        ynames = [str(y) for y in range(1, 9)]
        if xPos not in xnames:
            raise ValueError
        if yPos not in ynames:
            raise ValueError
        return cls(xnames.index(xPos), ynames.index(yPos))

    @classmethod
    def from_str(cls, string:str):
        if len(string) != 2:
            raise ValueError
        return cls.from_chars(string[0], string[1])

    @classmethod
    def __validate(cls, index:int):
        if index not in range(8):
            raise ValueError
        return index

    @property
    def xIndex(self):
        return self.__x_index

    @property
    def yIndex(self):
        return self.__y_index

    @property
    def xName(self):
        return [chr(x) for x in range(ord('a'), ord('h') + 1)][self.xIndex]

    @property
    def yName(self):
        return [str(y) for y in range(1, 9)][self.yIndex]


class Board:
    def __init__(self):
        self.__pieces:list = []
        self.setup()

    def setup(self):

        # Kings
        self.__pieces.append(King(Position.from_str('e1'), Color.WHITE))
        self.__pieces.append(King(Position.from_str('e8'), Color.BLACK))

        # Queens
        self.__pieces.append(Queen(Position.from_str('d1'), Color.WHITE))
        self.__pieces.append(Queen(Position.from_str('d8'), Color.BLACK))

        # Rooks
        for i in ['a', 'h']:
            self.__pieces.append(Rook(Position.from_chars(i, '1'), Color.WHITE))
            self.__pieces.append(Rook(Position.from_chars(i, '8'), Color.BLACK))

        # Knights
        for i in ['b', 'g']:
            self.__pieces.append(Knight(Position.from_chars(i, '1'), Color.WHITE))
            self.__pieces.append(Knight(Position.from_chars(i, '8'), Color.BLACK))

        # Bishops
        for i in ['c', 'f']:
            self.__pieces.append(Bishop(Position.from_chars(i, '1'), Color.WHITE))
            self.__pieces.append(Bishop(Position.from_chars(i, '8'), Color.BLACK))

        # Pawns
        for i in range(ord('a'), ord('h') + 1):
            self.__pieces.append(Pawn(Position.from_chars(chr(i), '2'), Color.WHITE))
            self.__pieces.append(Pawn(Position.from_chars(chr(i), '7'), Color.BLACK))

    def __str__(self):
        res = ''
        for item in self.__pieces:
            res += str(item.position) + '-' + str(item) + ',' #TODO: fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        return res
    
    @property
    def pieces(self):
        return self.__pieces


class Game: #Game mechnics like movement
    def __init__(self):
        pass


class Piece:
    def __init__(self, position:Position, color:Color):
        self.__position:Position = position
        self.__color:Color = color
        self.__has_moved = False

    def __str__(self):
        return ('black_' if self.color == Color.BLACK else 'white_') + self.name.lower()

    @property
    def name(self):
        return 'Unnamed'

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color


class King(Piece):
    def __init__(self, position:Position, color:Color):
        super().__init__(position, color)
        self.__in_check = False
    
    @property
    def name(self):
        return 'King'

    def moves(self, board_state):
        actions = self.__moves_base()

    def __moves_base(self, actions=[]):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x and y):
                    continue
                actions.append(pos)
        return actions


class Queen(Piece):

    @property
    def name(self):
        return 'Queen'


class Rook(Piece):

    @property
    def name(self):
        return 'Rook'


class Bishop(Piece):

    @property
    def name(self):
        return 'Bishop'


class Knight(Piece):

    @property
    def name(self):
        return 'Knight'


class Pawn(Piece):
    
    @property
    def name(self):
        return 'Pawn'

