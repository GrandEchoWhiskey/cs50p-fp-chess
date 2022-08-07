from enum import Enum
from copy import deepcopy as copy
print('Chess Engine created by: Eric Wolf')

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8

WHITE = 0
BLACK = 1

KING = 'k'
QUEEN = 'q'
ROOK = 'r'
KNIGHT = 'n'
BISHOP = 'b'
PAWN = 'p'

def next_to(pos:tuple, x:int=0, y:int=0) -> tuple:
    try:
        if len(pos) != 2:
            raise ValueError
        if pos[0]+x > 8 or pos[0]+x < 1:
            raise ValueError
        if pos[1]+y > 8 or pos[1]+y < 1:
            raise ValueError
        return (pos[0]+x, pos[1]+y)
    except:
        raise ValueError

def next_to(pos:tuple, vec:tuple) -> tuple:
    try:
        if len(pos) != 2:
            raise ValueError
        if len(vec) != 2:
            raise ValueError
        if pos[0]+vec[0] > 8 or pos[0]+vec[0] < 1:
            raise ValueError
        if pos[1]+vec[1] > 8 or pos[1]+vec[1] < 1:
            raise ValueError
        return (pos[0]+vec[0], pos[1]+vec[1])
    except:
        raise ValueError

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


class Piece:
    def __init__(self, color:Color):
        self.__color:Color = color
        self.__has_moved = False

    def __str__(self):
        return ('black_' if self.color == Color.BLACK else 'white_') + self.name.lower()


    @classmethod
    def child(cls, char):
        while case := char.lower(): # older version of python match not supported TODO
            if case == 'k':
                return King
            if case == 'q':
                return Queen
            if case == 'r':
                return Rook
            if case == 'n':
                return Knight
            if case == 'b':
                return Bishop
            if case == 'p':
                return Pawn
            return None

    @property
    def fen_char(self):
        return ' '

    @property
    def name(self):
        return "Unnamed"

    @property
    def color(self):
        return self.__color

    @property
    def has_moved(self):
        return self.__has_moved


class King(Piece):
    
    @property
    def fen_char(self):
        return 'k' if self.color == Color.BLACK else 'K'

    @property
    def name(self):
        return "King"

    def moves(self, board, position:Position):
        moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x and y):
                    continue
                pos = Position.neighbor(position, x, y)
                if not pos:
                    continue
                if not board.pieces[str(pos)]:
                    continue
                if board.pieces[str(pos)].color == self.color:
                    continue
                broke = False
                for coord in board.pieces.keys():
                    if board.pieces[coord].name == "King":
                        continue
                    if pos in board.pieces[coord].moves and board.pieces[coord].color != self.color:
                        broke = True
                        break
                if broke:
                    continue
                moves.append(pos)

        for x in range(2, 8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            broke = False
            for coord in board.pieces.keys():
                if not board.pieces[coord]:
                    continue
                if board.pieces[coord].color != self.color:
                    continue
                if board.pieces[coord].name == "King":
                    continue
                if pos in board.pieces[coord].moves(board, Position.from_str(coord)):
                    broke = True
                    break
            if broke:
                break
            if board.pieces[str(pos)].name == "Rook" and board.pieces[str(pos)].color == self.color:
                moves.append(Position.neighbor(position, x=2))

        for x in range(-2, -8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            broke = False
            for coord in board.pieces.keys():
                if pos in board.pieces[coord].moves and board.pieces[coord].color != self.color:
                    broke = True
                    break
            if broke:
                break
            if board.pieces[str(pos)].name == "Rook" and board.pieces[str(pos)].color == self.color \
                and not (self.has_moved or board.pieces[str(pos)].has_moved):
                moves.append(Position.neighbor(position, x=-2))
        
        return moves



class Queen(Piece):

    @property
    def fen_char(self):
        return 'q' if self.color == Color.BLACK else 'Q'

    @property
    def name(self):
        return "Queen"

    def moves(self, board, position:Position):
        moves = []

        for x in range(1, 8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for x in range(-1, -8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for y in range(1, 8):
            pos = Position.neighbor(position, y=y)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        for y in range(-1, -8):
            pos = Position.neighbor(position, y=y)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=xy, y=xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=-xy, y=xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=-xy, y=-xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        for xy in range(1, 8):
            pos = Position.neighbor(position, x=xy, y=-xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        return moves



class Rook(Piece):

    @property
    def fen_char(self):
        return 'r' if self.color == Color.BLACK else 'R'

    @property
    def name(self):
        return "Rook"

    def moves(self, board, position:Position):
        moves = []

        for x in range(1, 8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for x in range(-1, -8):
            pos = Position.neighbor(position, x=x)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for y in range(1, 8):
            pos = Position.neighbor(position, y=y)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        for y in range(-1, -8):
            pos = Position.neighbor(position, y=y)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        return moves


class Knight(Piece):

    @property
    def fen_char(self):
        return 'n' if self.color == Color.BLACK else 'N'

    @property
    def name(self):
        return "Knight"

    def moves(self, board, position:Position):
        moves = []

        for x in [-1, 1]:
            for y in [-2, 2]:
                pos = Position.neighbor(position, x=x, y=y)
                if not pos:
                    continue
                if board.pieces[str(pos)] != None:
                    if board.pieces[str(pos)].color == self.color:
                        continue
                moves.append(pos)

        for y in [-1, 1]:
            for x in [-2, 2]:
                pos = Position.neighbor(position, x=x, y=y)
                if not pos:
                    continue
                if board.pieces[str(pos)] != None:
                    if board.pieces[str(pos)].color == self.color:
                        continue
                moves.append(pos)

        return moves


class Bishop(Piece):

    @property
    def fen_char(self):
        return 'b' if self.color == Color.BLACK else 'B'

    @property
    def name(self):
        return "Bishop"

    def moves(self, board, position:Position):
        moves = []

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=xy, y=xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=-xy, y=xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)

        for xy in range(1, 8):
            pos = Position.neighbor(position, x=-xy, y=-xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        for xy in range(1, 8):
            pos = Position.neighbor(position, x=xy, y=-xy)
            if not pos:
                break
            if board.pieces[str(pos)] != None:
                if board.pieces[str(pos)].color == self.color:
                    break
                moves.append(pos)
                break
            moves.append(pos)
        
        return moves


class Pawn(Piece):

    @property
    def fen_char(self):
        return 'p' if self.color == Color.BLACK else 'P'

    @property
    def name(self):
        return "Pawn"

    def moves(self, board, position:Position):
        moves = []

        # 1 forward if empty, 2 forward if on 2nd and 7th row and empty
        pos = Position.neighbor(position, y=1 if self.color == Color.WHITE else -1)
        if not board.pieces[str(pos)]:
            moves.append(pos)
            if (position.yIndex == 1 and self.color == Color.WHITE) or \
                (position.yIndex == 6 and self.color == Color.BLACK):
                    pos = Position.neighbor(position, y=2 if self.color == Color.WHITE else -2)
                    if not board.pieces[str(pos)]:
                        moves.append(pos)

        # Beating other pieces
        for x in [-1, 1]:
            try:
                pos = Position.neighbor(position, x=x, y=1 if self.color == Color.WHITE else -1)
                if board.pieces[str(pos)]:
                    if board.pieces[str(pos)].color != self.color:
                        moves.append(pos)
            except:
                continue
             
        # En passant
        if not board.last_moved:
            return moves

        for x in [-1, 1]:
            if (position.yIndex == 4 and self.color == Color.WHITE) or \
                (position.yIndex == 3 and self.color == Color.BLACK):
                
                if board.last_moved['to'] == pos and board.last_moved['obj'].name == "Pawn" and \
                    board.last_moved['obj'].color != self.color and \
                        board.last_moved['from'] == Position.neighbor(pos, x=x, y=-2 if self.color == Color.WHITE else 2):
                            moves.append(Position.neighbor(position, x=x, y=1 if self.color == Color.WHITE else -1))

        return moves


class Board:
    def __init__(self, pieces:dict={}):
        if not len(pieces.keys()):
            pieces = self.default
        self.__pieces:dict = {str(Position(x, y)): \
            None if str(Position(x,y)) not in pieces.keys() else pieces[str(Position(x,y))] \
                for x in range(8) for y in range(8)}
        self.__last_moved = None

    @property
    def fen(self):
        res = ''
        for y in range(8):
            for x in range(8):
                if not self.pieces[str(Position(x, 7-y))]:
                    res += ' '
                    continue
                p:Piece = self.pieces[str(Position(x, 7-y))]
                char = p.fen_char if p.color == Color.BLACK else p.fen_char.upper()
                res += char
            res += '/' if y < 7 else ''

        for i in range(8, 0, -1):
            res = res.replace(' ' * i, str(i))

        return res

    @property
    def default(self):
        res = {
            'a1': Rook(Color.WHITE),
            'b1': Knight(Color.WHITE),
            'c1': Bishop(Color.WHITE),
            'd1': Queen(Color.WHITE),
            'e1': King(Color.WHITE),
            'f1': Bishop(Color.WHITE),
            'g1': Knight(Color.WHITE),
            'h1': Rook(Color.WHITE),
            'a8': Rook(Color.BLACK),
            'b8': Knight(Color.BLACK),
            'c8': Bishop(Color.BLACK),
            'd8': Queen(Color.BLACK),
            'e8': King(Color.BLACK),
            'f8': Bishop(Color.BLACK),
            'g8': Knight(Color.BLACK),
            'h8': Rook(Color.BLACK)
        }
        for i in range(8):
            res[str(Position(i, 1))] = Pawn(Color.WHITE)
            res[str(Position(i, 6))] = Pawn(Color.BLACK)
        return res

    @classmethod
    def from_fen(cls, fen:str="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        res:str = copy(fen)

        if len(res.split('/')) != 8:
            raise ValueError

        for i in range(1, 9):
            res = res.replace(str(i), ' ' * i)

        for row in res.split('/'):
            if len(row) != 8:
                raise ValueError
            
        for letter in res.replace(' ', '').replace('/', '').lower():
            if letter not in "kqrnbp":
                raise ValueError

        pieces:dict = {}

        for i, y in enumerate(res.split('/')):
            for j, x in enumerate(y):

                if x == ' ':
                    pieces[str(Position(j, 7-i))] = None
                    continue

                color = Color.BLACK if x.islower() else Color.WHITE
                piece = Piece.child(x)

                pieces[str(Position(j, 7-i))] = piece(color)

        return cls(pieces)

    def move(self, from_pos:Position, to_pos:Position):
        piece = self.__pieces[str(from_pos)]
        self.__pieces[str(from_pos)] = None
        self.__pieces[str(to_pos)] = piece
        self.__last_moved = {'from': from_pos, 'to': to_pos, 'obj': piece}

    def replace(self, on_pos:Position, new_piece:Piece):
        self.__pieces[str(on_pos)] = new_piece

    def remove(self, on_pos:Position):
        self.replace(on_pos, None)
    
    @property
    def pieces(self):
        return self.__pieces

    @property
    def last_moved(self):
        return self.__last_moved


class Game:
    def __init__(self, board=Board(), at_turn=Color.WHITE):
        self.__board_state = board
        self.__at_turn = at_turn
        self.__history = []

    @classmethod
    def from_fen(cls, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"):
        splitted = fen.split(' ')
        if len(splitted) < 1:
            return ValueError
        if len(splitted) < 2:
            splitted.append('w')
        cls(Board.from_fen(splitted[0]), Color.BLACK if splitted[1] == 'b' else Color.WHITE)

    def round(self, _from, _to):
        #try:
        if not self.board.pieces[_from]:
            return False
        if self.board.pieces[_from].color != self.at_turn:
            return False
        for pkey in self.board.pieces.keys():
            # Find king and check if in check
            if not self.board.pieces[pkey]:
                continue

            if self.board.pieces[pkey].color == self.at_turn and \
                self.board.pieces[pkey].name == "King":
                if self.in_check(pkey, self.at_turn) and _from != pkey:
                    return False
            # Check for king movement 
            if Position.from_str(_to) in self.board.pieces[pkey].moves(self.board, Position.from_str(pkey)):
                if self.board.pieces[pkey].name == "King":
                    for x in [-2, 2]:
                        if Position.neighbor(Position.from_str(_from), x=x) == Position.from_str(_to):
                            # Find Rook
                            for p in range(8*(x//2)):
                                if self.board.pieces[str(Position.neighbor(Position.from_str(_from), x=p))].name == 'Rook':
                                    self.board.move(Position.neighbor(Position.from_str(_from), x=p), Position.neighbor(Position.from_str(_from), x=(x//2)))
                                    self.move(_from, _to)
                                    return True
                if self.board.pieces[pkey].name == "Pawn":
                    for x in [-1, 1]:
                        if self.board.pieces[str(Position.neighbor(Position.from_str(_from), x=x))]:
                            if self.board.pieces[str(Position.neighbor(Position.from_str(_from), x=x))].color != self.board.pieces[_from].color:
                                self.board.remove(Position.neighbor(Position.from_str(_from), x=x))
                                self.move(_from, _to)
                                return True
                self.move(_from, _to)
                return True
        return False
        #except:
            #return ValueError

    def move(self, _from:str, _to:str):
        try:
            if Position.from_str(_to) in self.board.pieces[_from].moves(self.board, Position.from_str(_from)) and self.board.pieces[_from].color == self.at_turn:
                self.board.move(Position.from_str(_from), Position.from_str(_to))
                self.__at_turn = Color.BLACK if self.at_turn == Color.WHITE else Color.WHITE
                return True
        except:
            raise ValueError
        return False

    def moves_for(self, _pos:str):
        moves = []
        try:
            for move in self.board.pieces[_pos].moves():
                moves.append(str(move))
        except:
            raise ValueError
        return moves

    def in_check(self, _pos:str, color):
        #try:
        for pkey in self.board.pieces.keys():
            if not self.board.pieces[pkey]:
                continue
            if color != self.board.pieces[pkey].color:
                if Position.from_str(_pos) in self.board.pieces[pkey].moves(self.board, Position.from_str(pkey)):
                    return True
        #except:
            #raise ValueError
        return False

    @property
    def at_turn(self):
        return self.__at_turn

    @property
    def board(self):
        return self.__board_state
