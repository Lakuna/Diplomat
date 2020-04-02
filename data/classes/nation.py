from data.classes.diplomat_loadable import DiplomatLoadable

class Nation(DiplomatLoadable):
	def __init__(self, identifiers, board):
		super().__init__(board)

		if not isinstance(identifiers, list):
			raise TypeError('identifiers must be a list.')
		for identifier in identifiers:
			if not isinstance(identifier, str):
				raise TypeError('identifiers must contain only strings.')
		if len(identifiers) < 1:
			raise IndexError('identifiers must contain at least one string.')

		self.identifiers = identifiers
		self.identifier = self.identifiers[0]

		self.places = []
		self.units = []

	def init_relationships(self):
		pass
