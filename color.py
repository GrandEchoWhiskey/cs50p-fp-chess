class TurnError(Exception):
	def __str__(self):
		return 'Player can\'t move this turn'
	
def debug(out_func=print):
	def log(func):
		def run(*args, **kwargs):
			out_func("Started debugging:", str(func.__name__))
			try:
				r=func(*args, **kwargs)
			except Exception as _e:
				out_func("Error in function:", str(func.__name__), '\n', _e.__class__.__name__ + ':', _e)
				return None
				
			out_func("End of function")
			return r
			
		return run
	return log
	
@debug()
def fun(s):
	print(s)
	raise TurnError
	
fun('x')