from position import position
from vector import vector

class board:
	"""
	Chess board with movement
	"""
	
	def __init__(self, xsize=8, ysize=8):
		self.__xs = xsize
		self.__ys = ysize
		self.__matrix = self.__setup_matrix()
		self.__ghost = None
	
	@classmethod
	def copy(cls, b):
		obj = cls(b.xsize, b.ysize)
		obj.set_ghost(b.ghost)
		obj.set_list(b.list)
		return obj
	
	def __setup_matrix(self):
		mtx = []
		for _ in range(self.xsize):
			tmp = []
			for _ in range(self.ysize):
				tmp.append(None)
			mtx.append(tmp)
		return mtx
	
	def move(self, from_pos, to_pos):
		self.set(to_pos, self.at(from_pos))
		self.rm(from_pos)
	
	def set(self, pos, obj):
		self.__matrix[pos.x][pos.y]=obj
		obj.set_position(pos)
		
	def rm(self, pos):
		self.__matrix[pos.x][pos.y]=None
		
	def at(self, pos):
		return self.list[pos.x][pos.y]
		
	def is_empty(self, pos):
		return self.list[pos.x][pos.y] is None
		
	def set_ghost(self, obj=None):
		self.__ghost = obj
		
	def set_list(self, matrix):
		if len(matrix) != self.xsize:
			raise IndexError
		for col in matrix:
			if len(col) != self.ysize:
				raise IndexError
		self.__matrix = matrix
		
	@property
	def ghost(self):
		return self.__ghost
				
	@property
	def xsize(self):
		return self.__xs
		
	@property
	def ysize(self):
		return self.__ys
		
	@property
	def list(self):
		return self.__matrix
