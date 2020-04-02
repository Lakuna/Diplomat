from data.classes.diplomat_loadable import DiplomatLoadable
from data.classes.nation import Nation

class Place(DiplomatLoadable):
	def __init__(self, identifiers, owner_identifier, adjacent_territory_codes, board):
		super().__init__(board)

		if not isinstance(identifiers, list):
			raise TypeError('identifiers must be a list.')
		for identifier in identifiers:
			if not isinstance(identifier, str):
				raise TypeError('identifiers must contain only strings.')
		if len(identifiers) < 1:
			raise IndexError('identifiers must contain at least one string.')
		if not isinstance(owner_identifier, str):
			raise TypeError('owner_identifier must be a string.')
		if not isinstance(adjacent_territory_codes, list):
			raise TypeError('adjacent_territory_codes must be a list.')
		for code in adjacent_territory_codes:
			if not isinstance(code, str):
				raise TypeError('adjacent_territory_codes must contain only strings.')
		if len(adjacent_territory_codes) < 1:
			raise IndexError('adjacent_territory_codes must contain at least one string.')

		self.identifiers = identifiers
		self.identifier = self.identifiers[0]

		self.owner_identifier = owner_identifier
		self.owner = None

		self.adjacent_territory_codes = adjacent_territory_codes
		self.adjacent_territories = []
		self.adjacent_land = []
		self.adjacent_water = []

	def switch_owner(self, owner):
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')

		if self.owner != None:
			self.owner.places.remove(self)
		self.owner = owner

	def init_relationships(self):
		for code in self.adjacent_territory_codes:
			if not code in self.board.loadables:
				raise IndexError('self.board.loadables does not contain code [' + code + '].')
			territory = self.board.loadables[code]
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
		self.switch_owner(owner)

class Territory(Place):
	pass

class WaterTerritory(Territory):
	load_from_query_identifier = 'w'

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO

class LandTerritory(Territory):
	load_from_query_identifier = 'l'

	def __init__(self, identifiers, owner_identifier, adjacent_territory_codes, board):
		super().__init__(identifiers, owner_identifier, adjacent_territory_codes, board)

		self.coasts = []

	def switch_owner(self, owner):
		if self.owner != None:
			for coast in self.coasts:
				self.owner.places.remove(coast)

		super().switch_owner(owner)

		for coast in self.coasts:
			self.owner.places.append(coast)

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO

class HybridTerritory(LandTerritory):
	load_from_query_identifier = 'h'

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO

class Coast(Place):
	load_from_query_identifier = 'c'

	def __init__(self, identifiers, territory_code, adjacent_territory_codes, board):
		super().__init__(identifiers, adjacent_territory_codes, board)

		if not isinstance(territory_code, str):
			raise TypeError('territory_code must be a string.')

		self.territory_code = territory_code
		self.territory = None

	def switch_owner(self, owner):
		self.territory.switch_owner(owner)

	def init_relationships(self):
		if not self.territory_code in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.territory_code [' + self.territory_code + '].')

		self.territory = self.board.loadables(self.territory_code)
		self.territory.coasts.append(self)

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO
