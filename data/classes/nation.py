from data.classes.diplomat_loadable import DiplomatLoadable

class Nation(DiplomatLoadable):
	load_from_query_identifier = 'n'

	def __init__(self, board, identifier, names, productive_territory_identifiers):
		super().__init__(board, identifier, names)

		self.board.nations.append(self)

		if not isinstance(productive_territory_identifiers, list):
			raise TypeError('productive_territory_identifiers must be a list.')
		for identifier in productive_territory_identifiers:
			if not isinstance(identifier, str):
				raise TypeError('productive_territory_identifiers must contain only strings.')

		self.productive_territory_identifiers = productive_territory_identifiers
		self.productive_territories = []
		self.territories = []

		self.units = []

	def view_string(self):
		return_string = str(self) + ': ' + str(self.names) + '\nProductive territories:'
		for productive_territory in self.productive_territories:
			return_string += ',\t' + str(productive_territory)
		return_string += '\nTerritories:'
		for territory in self.territories:
			return_string += ',\t' + str(territory)
		return_string += '\nUnits:'
		for unit in self.units:
			return_string += ',\t' + str(unit)
		return return_string

	def init_relationships(self):
		super().init_relationships()

		for identifier in self.productive_territory_identifiers:
			if not identifier in self.board.loadables:
				raise IndexError('self.board.loadables does not contain identifier [' + identifier + '].')
			productive_territory = self.board.loadables[identifier]
			self.productive_territories.append(productive_territory)

	@staticmethod
	def load_from_query(board, identifier, query):
		DiplomatLoadable.load_from_query(board, identifier, query)

		# Get names.
		if len(query) < 6:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		names = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			if current != '-':
				names.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		# Get productive_territory_identifiers.
		if len(query) < 3:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		productive_territory_identifiers = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			if current != '-':
				productive_territory_identifiers.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		return Nation(board, identifier, names, productive_territory_identifiers)
