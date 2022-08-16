from vector import vector

class position(vector):
	
	__alpha = 'abcdefgh'
	__nums = '12345678'
	
	def __init__(self, x, y):
		if type(x) != int or type(y) != int:
			raise TypeError
		if x >= len(self.__alpha) or y >= len(self.__nums) or x < 0 or y < 0:
			raise ValueError
		super().__init__(x, y)
	
	def __str__(self):
		return self.__alpha[self.x] + self.__nums[self.y]
	
	@classmethod
	def str(cls, s:str):
		
		if len(s) != 2:
			raise ValueError
			
		if not (s[0] in cls.__alpha and s[1] in cls.__nums):
			raise ValueError
			
		return cls(cls.__alpha.index(s[0]), cls.__nums.index(s[1]))
		
	@classmethod
	def alpha(cls):
		return cls.__alpha
		
	@classmethod
	def nums(cls):
		return cls.__nums
		
p=position.tuple((3,8))
print(str(p.as_tuple))