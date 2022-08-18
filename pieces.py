from vector import vector
from position import position
from board import board

BLACK = 1
WHITE = 0

class piece:
	
	def __init__(self, color):
		self._color = color
		self._position:position
		
	def __str__(self):
		return ''
		
	def _color_char(self, char):
		return char.lower() if self.color == BLACK else char.upper()
		
	@property
	def color(self):
		return self._color
		
	@property
	def position(self):
		return self._position
		
	def set_position(self, position):
		self._position = position
		
class king(piece):
	
	def __str__(self):
		return self._color_char('k')
		
	def moves(self, b:board):
		
		actions=[]
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue
				try:
					t_vec = vector(i, j)
					t_pos = self._position + t_vec
					if not b.is_empty(t_pos):
						if b.at(t_pos).color == self.color:
							continue
						actions.append(str(t_pos))
				except:
					continue
					
				for action in actions:
					
				
		return actions
	
class rook(piece):
	
	def __str__(self):
		return self._color_char('r')
	
	def moves(self, b:board):
		
		actions=[]
		for t in [vector(1,0), vector(0,1), vector(-1,0), vector(0,-1)]:
			for j in range(1, 8):
				last = False
				try:
					t_vec = t * vector(j,j)
					t_pos = self._position + t_vec
					if not b.is_empty(t_pos):
						if b.at(t_pos).color == self.color:
							break
						last = True
					actions.append(str(t_pos))
					if last: break
				except:
					break
		return actions
	
	
class bishop(piece):
	
	def __str__(self):
		return self._color_char('b')
	
	def moves(self, b:board):
		
		actions=[]
		for t in [vector(1,1), vector(-1,1), vector(-1,-1), vector(1,-1)]:
			for j in range(1, 8):
				last = False
				try:
					t_vec = t * vector(j,j)
					t_pos = self._position + t_vec
					if not b.is_empty(t_pos):
						if b.at(t_pos).color == self.color:
							break
						last = True
					actions.append(str(t_pos))
					if last: break
				except:
					break
		return actions
	
	
class queen(rook, bishop):
	
	def __str__(self):
		return self._color_char('q')
	
	def moves(self, b:board):
		
		actions = rook.moves(self, b)
		actions.extend(bishop.moves(self, b))
		return actions
	
	
class knight(piece):
	
	def __str__(self):
		return self._color_char('n')
		
	def moves(self, b:board):
			
		actions = []
		for i in [-2, 2]:
			for j in [-1, 1]:
				for v in [vector(i, j), vector(j, i)]:
					try:
						t_pos = self._position + v
						if not b.is_empty(t_pos):
							if b.at(t_pos).color == self.color:
								continue
						actions.append(str(t_pos))
					except:
						continue
		return actions
	
class pawn(piece):
	
	def __str__(self):
		return self._color_char('p')
		
	def moves(self, b:board):
		
		actions = []
		direct = 1 if self.color == WHITE else -1
		
		for x in [-1, 1]:
			try:
				t_pos = self._position + vector(x, direct)
				if not b.is_empty(t_pos):
					if b.at(t_pos).color != self.color:
						actions.append(str(t_pos))
				if b.ghost == t_pos:
					actions.append(str(t_pos))
			except:
				continue
				
		for y in [1*direct, 2*direct]:
			try:
				t_pos = self._position + vector(0, y)
				if not b.is_empty(t_pos):
					break
				actions.append(str(t_pos))
				if self.position.y > 1 and self.color == WHITE:
					 break
				if self.position.y < 6 and self.color == BLACK:
					 break
			except:
				break
				
		return actions
				
b=board()
b.set(position.str('d2'), pawn(BLACK))
b.set(position.str('c1'), knight(WHITE))
b.set(position.str('e3'), queen(BLACK))
print(b.at(position.str('d2')).moves(b))