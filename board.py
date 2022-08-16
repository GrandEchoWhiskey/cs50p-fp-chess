from vector import vector as vec
from position import position as pos

WHITE = 0
BLACK = 1

class board:
	
	def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		temp = fen.split(' ')
		self.__pieces = temp[0]
		self.__turn = BLACK if temp[1] == 'b' else WHITE
				
				