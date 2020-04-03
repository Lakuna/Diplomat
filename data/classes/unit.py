from data.classes.diplomat_loadable import DiplomatLoadable
from data.classes.nation import Nation
from data.classes.territory import Territory, WaterTerritory, LandTerritory, HybridTerritory

class Unit(DiplomatLoadable):
	def __init__(self, board, identifier, owner_identifier, location_identifier):
		super().__init__(board, identifier, [identifier])

		self.board.units.append(self)

		if not isinstance(owner_identifier, str):
			raise TypeError('owner_identifier must be a string.')
		if not isinstance(location_identifier, str):
			raise TypeError('location_identifier must be a string.')

		self.owner_identifier = owner_identifier
		self.owner = None

		self.power = 1

		self.location_identifier = location_identifier
		self.location = None
		self.old_location = None

		self.old_name = None

	def set_location(self, location):
		if not isinstance(location, Territory):
			raise TypeError('location must be a Territory.')

		if self.location != None:
			self.location.units.remove(self)
			self.old_location = self.location
		if self.name != None:
			self.old_name = self.name
		self.location = location
		self.location.units.append(self)

	def destroy(self):
		self.board.loadables.pop(self.identifier, None)
		self.board.units.remove(self)
		self.owner.units.remove(self)
		self.location.units.remove(self)

	def movable_territories(self):
		raise NotImplementedError('movable_territories() is not implemented.')

	def set_owner(self, owner):
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')

		if self.owner != None:
			self.owner.territories.remove(self)
		self.owner = owner
		self.owner.units.append(self)

	def view_string(self):
		return str(self) + ': ' + str(self.names) + '\nOwner: ' + str(self.owner) + '\nLocation: ' + str(self.location)

	def init_relationships(self):
		super().init_relationships()

		if not self.owner_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.owner_identifier [' + self.owner_identifier + '].')
		owner = self.board.loadables[self.owner_identifier]
		if not isinstance(owner, Nation):
			raise TypeError('owner must be a Nation.')
		self.set_owner(owner)

		if not self.location_identifier in self.board.loadables:
			raise IndexError('self.board.loadables does not contain self.location_identifier [' + self.location_identifier + '].')

class Army(Unit):
	load_from_query_identifier = 'a'

	def __init__(self, board, identifier, owner_identifier, location_identifier):
		super().__init__(board, identifier, owner_identifier, location_identifier)

		self.convoys = []

	def set_location(self, location):
		if not isinstance(location, LandTerritory):
			raise TypeError('location must be a LandTerritory.')

		super().set_location(location)

		self.name = self.owner.name + ' a ' + self.location.name

	def movable_territories(self):
		adjacent_land = self.location.adjacent_land
		convoy_destinations = []
		for convoy in self.convoys:
			for territory in convoy.location.adjacent_land:
				convoy_destinations.append(territory)
		return adjacent_land + convoy_destinations

	def init_relationships(self):
		super().init_relationships()

		location = self.board.loadables[self.location_identifier]
		if not isinstance(location, LandTerritory):
			raise TypeError('location must be a LandTerritory.')
		self.set_location(location)

	@staticmethod
	def load_from_query(board, identifier, query):
		DiplomatLoadable.load_from_query(board, identifier, query)
		
		# Get owner_identifier.
		if len(query) < 2:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get location_identifier.
		if len(query) < 1:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		location_identifier = query.pop(0)

		return Army(board, identifier, owner_identifier, location_identifier)

class Fleet(Unit):
	load_from_query_identifier = 'f'

	def __init__(self, board, identifier, owner_identifier, location_identifier):
		super().__init__(board, identifier, owner_identifier, location_identifier)

		self.coast = None

	def set_location(self, location):
		super().set_location(location)

		# Set coast.
		if isinstance(self.location, LandTerritory):
			if not self.location.initialized:
				self.location.init_relationships()
			if len(self.location.adjacent_water) < 1:
				raise TypeError('self.location.adjacent_water must contain at least one WaterTerritory if it is a LandTerritory.')
			if self.old_location:
				for coast in self.location.adjacent_water:
					if coast in self.old_location.adjacent_water:
						self.coast = coast
						break
			if self.coast == None:
				self.coast = self.location.adjacent_water[0]

		self.name = self.owner.name + ' f ' + self.location.name

	def movable_territories(self):
		if isinstance(self.location, WaterTerritory) or isinstance(self.location, HybridTerritory):
			adjacent_territories_with_coast = list(filter(lambda territory: len(territory.adjacent_water) > 0, self.location.adjacent_territories))
			return adjacent_territories_with_coast
		if isinstance(self.location, LandTerritory):
			adjacent_territories_on_coast = list(filter(lambda territory: territory in self.coast.adjacent_territories, self.location.adjacent_territories))
			return adjacent_territories_on_coast
		raise TypeError('self.location must be a WaterTerritory, HybridTerritory, or LandTerritory.')

	def convoyable_units(self):
		units = []

		if isinstance(self.location, LandTerritory):
			return units # Can't convoy while landed.

		for unit in self.owner.units:
			if not isinstance(unit, Army):
				continue

			if unit.location in self.location.adjacent_territories:
				units.append(unit)
				continue

			for convoy in unit.convoys:
				if convoy.location in self.location.adjacent_territories:
					units.append(unit)
					continue
		return units

	def init_relationships(self):
		super().init_relationships()

		location = self.board.loadables[self.location_identifier]
		if not isinstance(location, Territory):
			raise TypeError('location must be a Territory.')
		self.set_location(location)

	@staticmethod
	def load_from_query(board, identifier, query):
		DiplomatLoadable.load_from_query(board, identifier, query)
		
		# Get owner_identifier.
		if len(query) < 2:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		owner_identifier = query.pop(0)

		# Get location_identifier.
		if len(query) < 1:
			raise IndexError('There are not enough parts in the query to hold the necessary parameters.')
		location_identifier = query.pop(0)

		return Fleet(board, identifier, owner_identifier, location_identifier)
