class Board:
	def __init__(self, name):
		if not isinstance(name, str):
			raise TypeError('name must be a string.')

		self.name = name
		self.loadables = {}
		self.nations = []
		self.places = []
		self.units = []

	def __str__(self):
		return self.name
