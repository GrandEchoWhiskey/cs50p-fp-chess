class vector:
	
	def __init__(self, x, y):
		if x.__class__ not in [int, float]:
			raise ValueError
		if y.__class__ not in [int, float]:
			raise ValueError
		self.__x = x
		self.__y = y
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
		
	def __ne__(self, other):
		return not self.__eq__(other)
		
	def __add__(self, other):
		return self.__class__(self.x+other.x, self.y+other.y)
		
	def __sub__(self, other):
		return self.__class__(self.x-other.x, self.y-other.y)
		
	def __mul__(self, other):
		return self.__class__(self.x*other.x, self.y*other.y)
		
	def __pow__(self, other):
		return self.__class__(self.x**other.x, self.y**other.y)
	
	def __truediv__(self, other):
		return self.__class__(self.x/other.x, self.y/other.y)
	
	def __floordiv__(self, other):
		return self.__class__(self.x//other.x, self.y//other.y)
		
	def __mod__(self, other):
		return self.__class__(self.x%other.x, self.y%other.y)
		
	def __str__(self):
		return '<'+str(self.x)+';'+str(self.y)+'>'
		
	@classmethod
	def from_tuple(cls, _tuple:tuple):
		if len(_tuple) != 2:
			raise ValueError
		return cls(_tuple[0], _tuple[1])
		
	@property
	def t(self):
		return (self.x, self.y)
		
	@property
	def x(self):
		return self.__x
		
	@property
	def y(self):
		return self.__y
		
v = vector.from_tuple((2, 1))
c = v/vector(-1, 2)
print(str(c))
		