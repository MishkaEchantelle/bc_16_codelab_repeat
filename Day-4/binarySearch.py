class BinarySearch(object):
	"""docstring for BinarySearch"""
	def __init__(self, length, step):
		super(BinarySearch, self).__init__()
		
		self.length = len(self)

		for x in range(1, length+1):
			self.append(x * step)
		
