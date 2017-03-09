class Truck(object):
	"""docstring for Truck"""
	def __init__(self, year, model, make, miles, wheels, sold_on):

		self.year = year
		self.model = model
		self.make = make
		self.miles = miles
		self.wheels = wheels
		self.sold_on = sold_on
		
	def sale_price(self):
		if self.sold_on is not None:
			return 0.0
		else:
			return float * self.wheels

	def purchase_price(self):
		if self.sold_on is None:
			return 0.0
		else:
			return 10000 - (.10 * self.miles)
