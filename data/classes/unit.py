from data.classes.diplomat_loadable import DiplomatLoadable
from data.classes.nation import Nation
from data.classes.place import WaterTerritory, LandTerritory, HybridTerritory, Coast

class Unit(DiplomatLoadable):
	def __init__(self, owner_identifier, location_identifier, board):
		super().__init__(board)

		if not isinstance(owner_identifier, str):
			raise TypeError('owner_identifier must be a string.')
		if not isinstance(location_identifier, str):
			raise TypeError('location_identifier must be a string.')

		self.owner_identifier = owner_identifier
		self.owner = None

		self.action = None
		self.action_target = None

		self.power = 1

		self.location_identifier = location_identifier
		self.location = None
		self.old_location = None

		self.identifier = None
		self.old_identifier = None

	def __str__(self):
		return self.identifier

	def move_to(self, location):
		raise NotImplementedError('move_to is not implemented.')

	def movable_territories(self):
		raise NotImplementedError('movable_territories is not implemented.')

	def switch_owner(self, owner):
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')

		if self.owner != None:
			self.owner.places.remove(self)
		self.owner = owner

	def init_relationships(self):
		if not self.owner_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.owner_identifier [' + self.owner_identifier + '].')
		owner = self.board.loadables[self.owner_identifier]
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')
		self.switch_owner(owner)

		if not self.location_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.location_identifier [' + self.location_identifier + '].')

class Army(Unit):
	load_from_query_identifier = 'a'

	def __init__(self, owner_identifier, location_identifier, board):
		super().__init__(owner_identifier, location_identifier, board)

		self.convoys = []

	def move_to(self, location):
		if not isinstance(location, LandTerritory):
			raise TypeError('location must be a LandTerritory.')

		if self.location != None:
			self.old_location = self.location
		if self.identifier != None:
			self.old_identifier = self.identifier
		self.location = location
		self.identifier = self.owner.identifier + ' a ' + self.location.identifier

	def movable_territories(self):
		adjacent_land = self.location.adjacent_land
		convoy_destinations = list(territory for territory in [convoy.location.adjacent_land for convoy in self.convoys])
		return adjacent_land + convoy_destinations

	def init_relationships(self):
		super().init_relationships()

		location = self.board.loadables[self.location_identifier]
		if not isinstance(location, LandTerritory):
			raise TypeError('location must be a LandTerritory.')
		self.location = location

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO

class Fleet(Unit):
	load_from_query_identifier = 'f'

	def move_to(self, location):
		if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
			raise TypeError('location must be a WaterTerritory, HybridTerritory, or Coast.')

		if self.location != None:
			self.old_location = self.location
		if self.identifier != None:
			self.old_identifier = self.identifier
		self.location = location
		self.identifier = self.owner.identifier + ' f ' + self.location.identifier

	def movable_territories(self):
		if isinstance(self.location, WaterTerritory) or isinstance(self.location, HybridTerritory):
			return self.location.adjacent_territories
		elif isinstance(self.location, Coast):
			adjacent_territories_on_coast = list(filter(lambda territory: territory in self.location.territory.adjacent_territories, self.location.adjacent_territories))
			return adjacent_territories_on_coast
		else:
			raise TypeError('self.location must be a WaterTerritory, HybridTerritory, or Coast.')

	def init_relationships(self):
		super().init_relationships()

		location = self.board.loadables[self.location_identifier]
		if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
			raise TypeError('location must be a WaterTerritory, HybridTerritory, or Coast.')
		self.location = location

	def load_from_query(self, query):
		super().load_from_query(query)
		# TODO
