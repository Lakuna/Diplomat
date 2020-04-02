from data.classes.diplomat_loadable import DiplomatLoadable
from data.classes.nation import Nation

class Place(DiplomatLoadable):
	def __init__(self, board, identifier, names, owner_identifier, adjacent_territory_identifiers):
		super().__init__(board, identifier)

		self.board.places.append(self)

		if not isinstance(names, list):
			raise TypeError('names must be a list.')
		for name in names:
			if not isinstance(name, str):
				raise TypeError('names must contain only strings.')
		if len(names) < 1:
			raise IndexError('names must contain at least one string.')
		if not isinstance(owner_identifier, str):
			raise TypeError('owner_identifier must be a string.')
		if not isinstance(adjacent_territory_identifiers, list):
			raise TypeError('adjacent_territory_identifiers must be a list.')
		for identifier in adjacent_territory_identifiers:
			if not isinstance(identifier, str):
				raise TypeError('adjacent_territory_identifiers must contain only strings.')
		if len(adjacent_territory_identifiers) < 1:
			raise IndexError('adjacent_territory_identifiers must contain at least one string.')

		self.names = names
		self.name = self.names[0]

		self.owner_identifier = owner_identifier
		self.owner = None

		self.adjacent_territory_identifiers = adjacent_territory_identifiers
		self.adjacent_territories = []
		self.adjacent_land = []
		self.adjacent_water = []

	def __str__(self):
		return self.name

	def set_owner(self, owner):
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')

		if self.owner != None:
			self.owner.places.remove(self)
		self.owner = owner

	def init_relationships(self):
		for identifier in self.adjacent_territory_identifiers:
			if not identifier in self.board.loadables:
				raise IndexError('self.board.loadables does not contain identifier [' + identifier + '].')
			territory = self.board.loadables[identifier]
			if not isinstance(territory, Territory):
				raise TypeError('territory must be a Territory.')
			self.adjacent_territories.append(territory)

		self.adjacent_land = list(filter(lambda territory: isinstance(territory, LandTerritory) or isinstance(territory, HybridTerritory), self.adjacent_territories))
		self.adjacent_water = list(filter(lambda territory: isinstance(territory, WaterTerritory) or isinstance(territory, HybridTerritory), self.adjacent_territories))

		if not self.owner_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.owner_identifier [' + self.owner_identifier + '].')
		owner = self.board.loadables[self.owner_identifier]
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')
		self.set_owner(owner)

class Territory(Place):
	pass

class WaterTerritory(Territory):
	load_from_query_identifier = 'w'

	@staticmethod
	def load_from_query(board, identifier, query):
		super().load_from_query(board, identifier, query)
		
		# Get names.
		if len(query) < 7:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		names = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			names.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		# Get owner_identifier.
		if len(query) < 4:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get adjacent_territory_identifiers.
		if len(query) < 3:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		adjacent_territory_identifiers = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			adjacent_territory_identifiers.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		return WaterTerritory(board, identifier, names, owner_identifier, adjacent_territory_identifiers)

class LandTerritory(Territory):
	load_from_query_identifier = 'l'

	def __init__(self, board, identifier, names, owner_identifier, adjacent_territory_identifiers):
		super().__init__(board, identifier, names, owner_identifier, adjacent_territory_identifiers)

		self.coasts = []

	def set_owner(self, owner):
		if self.owner != None:
			for coast in self.coasts:
				self.owner.places.remove(coast)

		super().set_owner(owner)

		for coast in self.coasts:
			self.owner.places.append(coast)

	@staticmethod
	def load_from_query(board, identifier, query):
		super().load_from_query(board, identifier, query)
		
		# Get names.
		if len(query) < 7:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		names = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			names.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		# Get owner_identifier.
		if len(query) < 4:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get adjacent_territory_identifiers.
		if len(query) < 3:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		adjacent_territory_identifiers = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			adjacent_territory_identifiers.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		return LandTerritory(board, identifier, names, owner_identifier, adjacent_territory_identifiers)

class HybridTerritory(LandTerritory):
	load_from_query_identifier = 'h'

	@staticmethod
	def load_from_query(board, identifier, query):
		super().load_from_query(board, identifier, query)
		
		# Get names.
		if len(query) < 7:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		names = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			names.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		# Get owner_identifier.
		if len(query) < 4:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get adjacent_territory_identifiers.
		if len(query) < 3:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		adjacent_territory_identifiers = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			adjacent_territory_identifiers.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		return HybridTerritory(board, identifier, names, owner_identifier, adjacent_territory_identifiers)

class Coast(Place):
	load_from_query_identifier = 'c'

	def __init__(self, board, identifier, names, owner_identifier, territory_identifier, adjacent_territory_identifiers):
		super().__init__(board, identifier, names, owner_identifier, adjacent_territory_identifiers)

		if not isinstance(territory_identifier, str):
			raise TypeError('territory_identifier must be a string.')

		self.territory_identifier = territory_identifier
		self.territory = None

	def set_owner(self, owner):
		self.territory.set_owner(owner)

	def init_relationships(self):
		if not self.territory_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.territory_identifier [' + self.territory_identifier + '].')

		self.territory = self.board.loadables[self.territory_identifier]
		self.territory.coasts.append(self)

	@staticmethod
	def load_from_query(board, identifier, query):
		super().load_from_query(board, identifier, query)
		
		# Get names.
		if len(query) < 8:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		names = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			names.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		# Get owner_identifier.
		if len(query) < 5:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get territory_identifier.
		if len(query) < 4:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		territory_identifier = query.pop(0)

		# Get adjacent_territory_identifiers.
		if len(query) < 3:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		if query[0] != '[':
			raise SyntaxError('Expected an opening bracket.')
		query.pop(0)
		adjacent_territory_identifiers = []
		current = query.pop(0)
		while current != ']' and len(query) > 0:
			adjacent_territory_identifiers.append(current)
			current = query.pop(0)
		if current != ']':
			raise SyntaxError('Expected a closing bracket.')

		return Coast(board, identifier, names, owner_identifier, territory_identifier, adjacent_territory_identifiers)
