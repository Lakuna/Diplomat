class DiplomatViewable:
	def __init__(self, names):
		if not isinstance(names, list):
			raise TypeError('names must be a list.')
		for name in names:
			if not isinstance(name, str):
				raise TypeError('names must contain only strings.')
		if len(names) < 0:
			raise IndexError('names must contain at least one string.')

		self.names = names
		self.name = names[0]

	def __str__(self):
		return self.name

	def view_string(self):
		return str(self)
