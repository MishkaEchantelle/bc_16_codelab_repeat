class BinarySearch(object):
	"""docstring for BinarySearch"""
	def __init__(self, a, b):
		super(BinarySearch, self).__init__()
		
		self.a = len(self)
		
		for x in range(1, a+1):
			self.append(x * b)
		
