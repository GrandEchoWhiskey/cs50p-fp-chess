class vector:
	"""
	2DVectors: float and int only accepted
	"""
	
	def __init__(self, x, y):
		if type(x) not in [int, float]:
			raise TypeError
		if type(y) not in [int, float]:
			raise TypeError
		self.__x = x
		self.__y = y
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
		
	def __ne__(self, other):
		return not self.__eq__(other)
		
	def __add__(self, other):
		return type(self)(self.x+other.x, self.y+other.y)
		
	def __sub__(self, other):
		return type(self)(self.x-other.x, self.y-other.y)
		
	def __mul__(self, other):
		return type(self)(self.x*other.x, self.y*other.y)
		
	def __pow__(self, other):
		return type(self)(self.x**other.x, self.y**other.y)
	
	def __truediv__(self, other):
		return type(self)(self.x/other.x, self.y/other.y)
	
	def __floordiv__(self, other):
		return type(self)(self.x//other.x, self.y//other.y)
		
	def __mod__(self, other):
		return type(self)(self.x%other.x, self.y%other.y)
		
	def __str__(self):
		return '<'+str(self.x)+';'+str(self.y)+'>'
	
	def __get__(self, obj, objtype):
		return (self.x, self.y)
	
	@classmethod
	def tuple(cls, t:tuple):
		
		if len(t) != 2:
			raise ValueError
		
		return cls(t[0], t[1])
		
	@property
	def as_tuple(self):
		return (self.x, self.y)

	@property
	def x(self):
		return self.__x
		
	@property
	def y(self):
		return self.__y

