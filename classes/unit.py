from nation import Nation
from territory import Territory, WaterTerritory, LandTerritory, HybridTerritory
from coast import Coast

def Unit:
	def __init__(self, is_fleet, owner, location):
		if not isinstance(is_fleet, bool):
			return 'is_fleet must be a boolean.'
		if not isinstance(owner, Nation):
			return 'owner must be a nation.'
		if is_fleet:
			if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
				return 'location must be a water territory, hybrid territory, or coast.'
		else:
			if not isinstance(location, LandTerritory):
				return 'location must be a land territory'

		self.is_fleet = is_fleet
		self.owner = owner
		self.location = None
		self.old_location = None
		self.identifier = None
		self.old_identifier = None
		self.action = None
		self.action_target = None
		self.convoys = []
		self.power = 1
		self.move_to(location)

	def __str__(self):
		return identifier

	def move_to(self, location):
		if is_fleet:
			if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
				return 'location must be a water territory, hybrid territory, or coast.'
		else:
			if not isinstance(location, LandTerritory):
				return 'location must be a land territory.'

		if self.location != None:
			self.old_location = self.location
		if self.identifier != None:
			self.old_identifier = self.identifier
		self.location = location
		type_letter = 'n' if is_fleet else 'a'
		self.identifier = self.owner.identifier + ' ' + type_letter + ' ' + self.location.identifier

	def movable_territories(self):
		if self.is_fleet:
			if isinstance(self.location, Territory):
				adjacent_territories = self.location.adjacent_territories
				return adjacent_territories
			else:
				# On a coast.
				adjacent_territories_on_coast = list(filter(lambda territory: territory in self.location.territory.adjacent_territories(), self.location.territories()))
				return adjacent_territories_on_coast
		else:
			adjacent_land = self.location.adjacent_land()
			convoy_destinations = list(territory for territory in [convoy.location.adjacent_land() for convoy in self.convoys])
			return adjacent_land + convoy_destinations

def Army(Unit):
	def __init__(self, owner, location):
		if not isinstance(owner, Nation):
			return 'owner must be a nation.'
		if not isinstance(location, LandTerritory):
			return 'location must be a land territory'

		self.is_fleet = False
		self.owner = owner
		self.location = None
		self.old_location = None
		self.identifier = None
		self.old_identifier = None
		self.action = None
		self.action_target = None
		self.convoys = []
		self.power = 1
		self.move_to(location)

	def move_to(self, location):
		if not isinstance(location, LandTerritory):
			return 'location must be a land territory.'

		if self.location != None:
			self.old_location = self.location
		if self.identifier != None:
			self.old_identifier = self.identifier
		self.location = location
		self.identifier = self.owner.identifier + ' a ' + self.location.identifier

	def movable_territories(self):
		adjacent_land = self.location.adjacent_land()
		convoy_destinations = list(territory for territory in [convoy.location.adjacent_land() for convoy in self.convoys])
		return adjacent_land + convoy_destinations

def Fleet(Unit):
	def __init__(self, owner, location):
		if not isinstance(owner, Nation):
			return 'owner must be a nation.'
		if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
			return 'location must be a water territory, hybrid territory, or coast.'

		self.is_fleet = True
		self.owner = owner
		self.location = None
		self.old_location = None
		self.identifier = None
		self.old_identifier = None
		self.action = None
		self.action_target = None
		self.convoys = []
		self.power = 1
		self.move_to(location)

	def move_to(self, location):
		if not (isinstance(location, WaterTerritory) or isinstance(location, HybridTerritory) or isinstance(location, Coast)):
			return 'location must be a water territory, hybrid territory, or coast.'

		if self.location != None:
			self.old_location = self.location
		if self.identifier != None:
			self.old_identifier = self.identifier
		self.location = location
		self.identifier = self.owner.identifier + ' n ' + self.location.identifier

	def movable_territories(self):
		if isinstance(self.location, Territory):
			adjacent_territories = self.location.adjacent_territories
			return adjacent_territories
		else:
			# On a coast.
			adjacent_territories_on_coast = list(filter(lambda territory: territory in self.location.territory.adjacent_territories(), self.location.territories()))
			return adjacent_territories_on_coast
