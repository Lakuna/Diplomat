import random
from os import system, name
# TODO - Move classes and methods into other files as appropriate.

class Map():
	def __init__(self):
		original_territories = {
			'Ankara': Territory('Ankara', ['ANK'], True, False, True, ['Constantinople', 'Black Sea', 'Armenia', 'Smyrna']),
			'Belgium': Territory('Belgium', ['BEL'], True, False, True, ['English Channel', 'Picardy', 'North Sea', 'Holland', 'Ruhr', 'Burgundy']),
			'Berlin': Territory('Berlin', ['BER'], True, False, True, ['Kiel', 'Baltic Sea', 'Prussia', 'Munich', 'Silesia']),
			'Brest': Territory('Brest', ['BRE'], True, False, True, ['English Channel', 'Mid-Atlantic Ocean', 'Gascony', 'Paris', 'Picardy']),
			'Budapest': Territory('Budapest', ['BUD'], True, False, True, ['Trieste', 'Vienna', 'Galicia', 'Rumania', 'Serbia']),
			'Bulgaria': Territory('Bulgaria', ['BUL'], True, False, True, ['Serbia', 'Rumania', 'Black Sea', 'Constantinople', 'Aegean Sea', 'Greece']),
			'Constantinople': Territory('Constantinople', ['CON'], True, True, True, ['Bulgaria', 'Black Sea', 'Ankara', 'Smyrna', 'Aegean Sea']),
			'Denmark': Territory('Denmark', ['DEN'], True, True, True, ['Heligoland Bight', 'North Sea', 'Skagerrack', 'Baltic Sea', 'Kiel', 'Sweden']),
			'Edinburgh': Territory('Edinburgh', ['EDI'], True, False, True, ['Clyde', 'Norwegian Sea', 'North Sea', 'Yorkshire', 'Liverpool']),
			'Greece': Territory('Greece', ['GRE'], True, False, True, ['Albania', 'Serbia', 'Bulgaria', 'Aegean Sea', 'Ionian Sea']),
			'Holland': Territory('Holland', ['HOL'], True, False, True, ['North Sea', 'Heligoland Bight', 'Kiel', 'Ruhr', 'Belgium']),
			'Kiel': Territory('Kiel', ['KIE'], True, False, True, ['Holland', 'Heligoland Bight', 'Denmark', 'Baltic Sea', 'Berlin', 'Munich', 'Ruhr']),
			'Liverpool': Territory('Liverpool', ['LVP', 'LIVP', 'LPL'], True, False, True, ['Clyde', 'North Atlantic Ocean', 'Edinburgh', 'Yorkshire', 'Wales', 'Irish Sea']),
			'London': Territory('London', ['LON'], True, False, True, ['Wales', 'Yorkshire', 'North Sea', 'English Channel']),
			'Marseilles': Territory('Marseilles', ['MAR', 'MARS'], True, False, True, ['Spain', 'Gascony', 'Burgundy', 'Gulf of Lyon', 'Piedmont']),
			'Moscow': Territory('Moscow', ['MOS'], True, False, True, ['Saint Petersburg', 'Sevastopol', 'Ukraine', 'Warsaw', 'Livonia']),
			'Munich': Territory('Munich', ['MUN'], True, False, True, ['Ruhr', 'Kiel', 'Berlin', 'Silesia', 'Bohemia', 'Tyrolia', 'Burgundy']),
			'Naples': Territory('Naples', ['NAP'], True, False, True, ['Tyrrhenian Sea', 'Rome', 'Apulia', 'Ionian Sea']),
			'Norway': Territory('Norway', ['NOR', 'NWY', 'NORW'], True, False, True, ['Skagerrack', 'North Sea', 'Norwegian Sea', 'Barents Sea', 'Sweden', 'Finland', 'Saint Petersburg']),
			'Paris': Territory('Paris', ['PAR'], True, False, True, ['Brest', 'Picardy', 'Burgundy', 'Gascony']),
			'Portugal': Territory('Portugal', ['POR'], True, False, True, ['Mid-Atlantic Ocean', 'Spain']),
			'Rome': Territory('Rome', ['ROM'], True, False, True, ['Tuscany', 'Venice', 'Apulia', 'Naples', 'Tyrrhenian Sea']),
			'Rumania': Territory('Rumania', ['RUH'], True, False, True, ['Budapest', 'Sevastopol', 'Black Sea', 'Bulgaria', 'Serbia', 'Galicia', 'Ukraine']),
			'Saint Petersburg': Territory('Saint Petersburg', ['STP', 'St. Petersburg'], True, False, True, ['Gulf of Bothnia', 'Finland', 'Norway', 'Barents Sea', 'Moscow', 'Livonia']),
			'Serbia': Territory('Serbia', ['SER'], True, False, True, ['Albania', 'Trieste', 'Budapest', 'Rumania', 'Bulgaria', 'Greece']),
			'Sevastopol': Territory('Sevastopol', ['SEV'], True, False, True, ['Ukraine', 'Moscow', 'Armenia', 'Black Sea', 'Rumania']),
			'Smyrna': Territory('Smyrna', ['SMY'], True, False, True, ['Constantinople', 'Ankara', 'Armenia', 'Syria', 'Eastern Mediterranean', 'Aegean Sea']),
			'Spain': Territory('Spain', ['SPA'], True, False, True, ['Portugal', 'Mid-Atlantic Ocean', 'Gascony', 'Marseilles', 'Gulf of Lyon', 'Western Mediterranean']),
			'Sweden': Territory('Sweden', ['SWE'], True, False, True, ['Norway', 'Finland', 'Gulf of Bothnia', 'Baltic Sea', 'Denmark', 'Skagerrack']),
			'Trieste': Territory('Trieste', ['TRI'], True, False, True, ['Venice', 'Tyrolia', 'Vienna', 'Budapest', 'Serbia', 'Albania', 'Adriatic Sea']),
			'Tunis': Territory('Tunis', ['TUN', 'Tunisia'], True, False, True, ['North Africa', 'Western Mediterranean', 'Tyrrhenian', 'Ionian Sea']),
			'Venice': Territory('Venice', ['VEN'], True, False, True, ['Piedmont', 'Tyrolia', 'Trieste', 'Adriatic Sea', 'Apulia', 'Rome', 'Tuscany']),
			'Vienna': Territory('Vienna', ['VIE'], True, False, True, ['Tyrolia', 'Bohemia', 'Galicia', 'Budapest', 'Trieste']),
			'Warsaw': Territory('Warsaw', ['WAR'], True, False, True, ['Silesia', 'Prussia', 'Livonia', 'Moscow', 'Ukraine', 'Galicia']),
			'Clyde': Territory('Clyde', ['CLY'], True, False, False, ['North Atlantic', 'Norwegian Sea', 'Edinburgh', 'Liverpool']),
			'Yorkshire': Territory('Yorkshire', ['YOR', 'York', 'Yonkers'], False, True, False, ['Edinburgh', 'North Sea', 'London', 'Wales', 'Liverpool']),
			'Wales': Territory('Wales', ['WAL'], True, False, False, ['Irish Sea', 'Liverpool', 'Yorkshire', 'London', 'English Channel']),
			'Picardy': Territory('Picardy', ['PIC'], True, False, False, ['Brest', 'English Channel', 'Belgium', 'Burgundy', 'Paris']),
			'Gascony': Territory('Gascony', ['GAS'], True, False, False, ['Brest', 'Paris', 'Burgundy', 'Marseilles', 'Spain', 'Mid-Atlantic Ocean']),
			'Burgundy': Territory('Burgundy', ['BUR'], True, False, False, ['Paris', 'Picardy', 'Belgium', 'Ruhr', 'Munich', 'Marseilles', 'Gascony']),
			'North Africa': Territory('North Africa', ['NAF', 'NORA'], True, False, False, ['Mid-Atlantic Ocean', 'Western Mediterranean', 'Tunis']),
			'Ruhr': Territory('Ruhr', ['RUH'], True, False, False, ['Belgium', 'Holland', 'Kiel', 'Munich', 'Burgundy']),
			'Prussia': Territory('Prussia', ['PRU'], True, False, False, ['Berlin', 'Baltic Sea', 'Livonia', 'Warsaw', 'Silesia']),
			'Silesia': Territory('Silesia', ['SIL'], True, False, False, ['Munich', 'Berlin', 'Prussia', 'Warsaw', 'Galicia', 'Bohemia']),
			'Piedmont': Territory('Piedmont', ['PIE'], True, False, False, ['Marseilles', 'Tyrolia', 'Venice', 'Tuscany', 'Gulf of Lyon']),
			'Tuscany': Territory('Tuscany', ['TUS'], True, False, False, ['Gulf of Lyon', 'Piedmont', 'Venice', 'Rome', 'Tyrrhenian Sea']),
			'Apulia': Territory('Apulia', ['APU'], True, False, False, ['Venice', 'Adriatic Sea', 'Ionian Sea', 'Naples', 'Rome']),
			'Tyrolia': Territory('Tyrolia', ['TYR', 'TYL', 'TRL'], True, False, False, ['Piedmont', 'Munich', 'Bohemia', 'Vienna', 'Trieste', 'Venice']),
			'Galicia': Territory('Galicia', ['GAL'], True, False, False, ['Bohemia', 'Silesia', 'Warsaw', 'Ukraine', 'Rumania', 'Budapest', 'Vienna']),
			'Bohemia': Territory('Bohemia', ['BOH'], True, False, False, ['Munich', 'Silesia', 'Galicia', 'Vienna', 'Tyrolia']),
			'Finland': Territory('Finland', ['FIN'], True, False, False, ['Sweden', 'Norway', 'Saint Petersburg', 'Gulf of Bothnia']),
			'Livonia': Territory('Livonia', ['LVN', 'LIVO', 'LVO', 'LVA'], True, False, False, ['Gulf of Bothnia', 'Saint Petersburg', 'Moscow', 'Warsaw', 'Prussia', 'Baltic Sea']),
			'Ukraine': Territory('Ukraine', ['UKR'], True, False, False, ['Warsaw', 'Moscow', 'Sevastopol', 'Rumania', 'Galicia']),
			'Albania': Territory('Albania', ['ALB'], True, False, False, ['Adriatic Sea', 'Trieste', 'Serbia', 'Greece', 'Ionian Sea']),
			'Armenia': Territory('Armenia', ['ARM'], True, False, False, ['Ankara', 'Black Sea', 'Syria', 'Smyrna', 'Sevastopol']),
			'Syria': Territory('Syria', ['SYR'], True, False, False, ['Eastern Mediterranean', 'Smyrna', 'Armenia']),
			'North Atlantic Ocean': Territory('North Atlantic Ocean', ['NAO', 'North Atlantic'], False, True, False, ['Clyde', 'Liverpool', 'Irish Sea', 'Mid-Atlantic Ocean', 'Norwegian Sea']),
			'Mid-Atlantic Ocean': Territory('Mid-Atlantic Ocean', ['MAO', 'Mid Atlantic Ocean', 'Mid Atlantic', 'MID', 'MAT'], False, True, False, ['North Atlantic Ocean', 'Irish Sea', 'English Channel', 'Brest', 'Gascony', 'Spain', 'Portugal', 'North Africa', 'Western Mediterranean']),
			'Norwegian Sea': Territory('Norwegian Sea', ['NWG', 'NorwSea', 'NRG', 'Norwegian'], False, True, False, ['North Atlantic Ocean', 'Barents Sea', 'Norway', 'North Sea', 'Edinburgh', 'Clyde']),
			'North Sea': Territory('North Sea', ['NTH', 'NorSea', 'NTS'], False, True, False, ['Norwegian Sea', 'Norway', 'Skagerrack', 'Denmark', 'Heligoland Bight', 'Holland', 'Belgium', 'English Channel', 'London', 'Yorkshire', 'Edinburgh']),
			'English Channel': Territory('English Channel', ['ENG', 'English', 'Channel', 'ECH'], False, True, False, ['Mid-Atlantic Ocean', 'Irish Sea', 'Wales', 'London', 'Belgium', 'Picardy', 'Brest', 'North Sea']),
			'Irish Sea': Territory('Irish Sea', ['IRI', 'Irish'], False, True, False, ['Mid-Atlantic Ocean', 'North Atlantic Ocean', 'Liverpool', 'Wales', 'English Channel']),
			'Heligoland Bight': Territory('Heligoland Bight', ['HEL', 'Heligoland'], False, True, False, ['North Sea', 'Denmark', 'Kiel', 'Holland']),
			'Skagerrack': Territory('Skagerrack', ['SKA'], False, True, False, ['North Sea', 'Norway', 'Sweden', 'Denmark']),
			'Baltic Sea': Territory('Baltic Sea', ['BAL', 'Baltic'], False, True, False, ['Denmark', 'Sweden', 'Gulf of Bothnia', 'Livonia', 'Prussia', 'Berlin', 'Kiel']),
			'Gulf of Bothnia': Territory('Gulf of Bothnia', ['BOT', 'GOB', 'BOTH', 'GulfOfB', 'Bothnia'], False, True, False, ['Sweden', 'Finland', 'Saint Petersburg', 'Livonia', 'Baltic Sea']),
			'Barents Sea': Territory('Barents Sea', ['BAR', 'Barents'], False, True, False, ['Norway', 'Norwegian Sea', 'Saint Petersburg']),
			'Western Mediterranean': Territory('Western Mediterranean', ['WES', 'WMED', 'West', 'Western', 'WestMed', 'WMS', 'WME', 'West Mediterranean'], False, True, False, ['Spain', 'Mid-Atlantic Ocean', 'North Africa', 'Tunis', 'Tyrrhenian', 'Gulf of Lyon']),
			'Gulf of Lyon': Territory('Gulf of Lyon', ['LYO', 'GOL', 'GulfOfL', 'Lyon'], False, True, False, ['Spain', 'Marseilles', 'Piedmont', 'Tuscany', 'Tyrrhenian Sea', 'Western Mediterranean']),
			'Tyrrhenian Sea': Territory('Tyrrhenian Sea', ['TYS', 'TYRR', 'Tyrrhenian', 'TYN', 'TYH'], False, True, False, ['Gulf of Lyon', 'Tuscany', 'Rome', 'Naples', 'Ionian Sea', 'Tunis', 'Western Mediterranean']),
			'Ionian Sea': Territory('Ionian Sea', ['ION', 'Ionian'], False, True, False, ['Tunis', 'Tyrrhenian Sea', 'Naples', 'Apulia', 'Adriatic Sea', 'Albania', 'Greece', 'Aegean Sea', 'Eastern Mediterranean']),
			'Adriatic Sea': Territory('Adriatic Sea', ['ADR', 'Adriatic'], False, True, False, ['Venice', 'Trieste', 'Albania', 'Ionian Sea', 'Apulia']),
			'Aegean Sea': Territory('Aegean Sea', ['AEG', 'Aegean'], False, True, False, ['Ionian Sea', 'Greece', 'Bulgaria', 'Constantinople', 'Smyrna', 'Eastern Mediterranean']),
			'Eastern Mediterranean': Territory('Eastern Mediterranean', ['EAS', 'EMED', 'EAST', 'Eastern', 'EastMed', 'EMS', 'EME', 'East Mediterranean'], False, True, False, ['Ionian Sea', 'Aegean Sea', 'Smyrna', 'Syria']),
			'Black Sea': Territory('Black Sea', ['BLA', 'Black'], False, True, False, ['Bulgaria', 'Rumania', 'Sevastopol', 'Armenia', 'Ankara', 'Constantinople']),
		}
		self.territories = {} # TODO: Just make all the references lowercase so you don't have to do this.
		for territory in original_territories.values():
			self.territories[simplify_string(territory.name)] = territory
			for abbreviation in territory.abbreviations:
				self.territories[simplify_string(abbreviation)] = territory

		self.nations = {
			'italy': Nation('Italy'),
			'austriahungary': Nation('Austria-Hungary'),
			'russia': Nation('Russia'),
			'turkey': Nation('Turkey'),
			'england': Nation('England'),
			'france': Nation('France'),
			'germany': Nation('Germany')
		}

		self.season = 'spring'

	def __str__(self):
		return 'Territories and abbreviations: ' + ''.join(list(map(lambda territory: territory + ' (' + self.territories[territory].name + '), ', self.territories))) + '\nNations: ' + ''.join(list(map(lambda nation: nation + ', ', self.nations)))

	def standard_setup(self):
		self.territories['piedmont'].set_owner(self.nations['italy'])
		self.territories['venice'].set_owner(self.nations['italy'])
		self.territories['tuscany'].set_owner(self.nations['italy'])
		self.territories['rome'].set_owner(self.nations['italy'])
		self.territories['apulia'].set_owner(self.nations['italy'])
		self.territories['naples'].set_owner(self.nations['italy'])
		self.territories['tyrrheniansea'].set_owner(self.nations['italy'])
		Unit(False, self.nations['italy'], self.territories['rome'])
		Unit(False, self.nations['italy'], self.territories['venice'])
		Unit(True, self.nations['italy'], self.territories['naples'])
		self.nations['italy'].finalize_starting_territory()

		self.territories['tyrolia'].set_owner(self.nations['austriahungary'])
		self.territories['bohemia'].set_owner(self.nations['austriahungary'])
		self.territories['galicia'].set_owner(self.nations['austriahungary'])
		self.territories['vienna'].set_owner(self.nations['austriahungary'])
		self.territories['trieste'].set_owner(self.nations['austriahungary'])
		self.territories['budapest'].set_owner(self.nations['austriahungary'])
		Unit(False, self.nations['austriahungary'], self.territories['vienna'])
		Unit(False, self.nations['austriahungary'], self.territories['budapest'])
		Unit(True, self.nations['austriahungary'], self.territories['trieste'])
		self.nations['austriahungary'].finalize_starting_territory()

		self.territories['finland'].set_owner(self.nations['russia'])
		self.territories['saintpetersburg'].set_owner(self.nations['russia'])
		self.territories['livonia'].set_owner(self.nations['russia'])
		self.territories['moscow'].set_owner(self.nations['russia'])
		self.territories['warsaw'].set_owner(self.nations['russia'])
		self.territories['ukraine'].set_owner(self.nations['russia'])
		self.territories['sevastopol'].set_owner(self.nations['russia'])
		Unit(False, self.nations['russia'], self.territories['moscow'])
		Unit(False, self.nations['russia'], self.territories['warsaw'])
		Unit(True, self.nations['russia'], self.territories['saintpetersburg'])
		Unit(True, self.nations['russia'], self.territories['sevastopol'])
		self.nations['russia'].finalize_starting_territory()

		self.territories['constantinople'].set_owner(self.nations['turkey'])
		self.territories['ankara'].set_owner(self.nations['turkey'])
		self.territories['armenia'].set_owner(self.nations['turkey'])
		self.territories['smyrna'].set_owner(self.nations['turkey'])
		self.territories['syria'].set_owner(self.nations['turkey'])
		self.territories['easternmediterranean'].set_owner(self.nations['turkey'])
		Unit(False, self.nations['turkey'], self.territories['constantinople'])
		Unit(False, self.nations['turkey'], self.territories['smyrna'])
		Unit(True, self.nations['turkey'], self.territories['ankara'])
		self.nations['turkey'].finalize_starting_territory()

		self.territories['clyde'].set_owner(self.nations['england'])
		self.territories['edinburgh'].set_owner(self.nations['england'])
		self.territories['liverpool'].set_owner(self.nations['england'])
		self.territories['yorkshire'].set_owner(self.nations['england'])
		self.territories['wales'].set_owner(self.nations['england'])
		self.territories['london'].set_owner(self.nations['england'])
		self.territories['irishsea'].set_owner(self.nations['england'])
		Unit(False, self.nations['england'], self.territories['liverpool'])
		Unit(True, self.nations['england'], self.territories['edinburgh'])
		Unit(True, self.nations['england'], self.territories['london'])
		self.nations['england'].finalize_starting_territory()

		self.territories['gascony'].set_owner(self.nations['france'])
		self.territories['brest'].set_owner(self.nations['france'])
		self.territories['picardy'].set_owner(self.nations['france'])
		self.territories['paris'].set_owner(self.nations['france'])
		self.territories['burgundy'].set_owner(self.nations['france'])
		self.territories['marseilles'].set_owner(self.nations['france'])
		Unit(False, self.nations['france'], self.territories['paris'])
		Unit(False, self.nations['france'], self.territories['marseilles'])
		Unit(True, self.nations['france'], self.territories['brest'])
		self.nations['france'].finalize_starting_territory()

		self.territories['ruhr'].set_owner(self.nations['germany'])
		self.territories['kiel'].set_owner(self.nations['germany'])
		self.territories['berlin'].set_owner(self.nations['germany'])
		self.territories['prussia'].set_owner(self.nations['germany'])
		self.territories['munich'].set_owner(self.nations['germany'])
		self.territories['silesia'].set_owner(self.nations['germany'])
		Unit(False, self.nations['germany'], self.territories['berlin'])
		Unit(False, self.nations['germany'], self.territories['munich'])
		Unit(True, self.nations['germany'], self.territories['kiel'])
		self.nations['germany'].finalize_starting_territory()

	def resolve_turn(self):
		pass # TODO - Resolve convoy -> move -> support -> conflicts -> add/remove cities (Fall) -> add/remove units (Fall) -> switch season

class Territory():
	def __init__(self, name, abbreviations, is_land, is_water, is_supply_center, adjacent_territory_names):
		self.name = name
		self.abbreviations = abbreviations
		self.is_land = is_land
		self.is_water = is_water
		self.is_supply_center = is_supply_center
		self.adjacent_territory_names = adjacent_territory_names
		self.owner = None
		self.units = []

	def finalize_adjacencies(self):
		self.adjacent_territories = list(map(lambda territory_name: game_map.territories[simplify_string(territory_name)], list(filter(lambda adjacent_territory_name: simplify_string(adjacent_territory_name) in game_map.territories, self.adjacent_territory_names))))
		self.adjacent_water = list(filter(lambda territory: territory.is_water, self.adjacent_territories))
		self.adjacent_land = list(filter(lambda territory: territory.is_land, self.adjacent_territories))

	def __str__(self):
		return_string = 'Territory ' + self.name + '\nAbbreviations: ' + ''.join(list(map(lambda abbreviation: abbreviation + ', ', self.abbreviations))) + '\n'
		if self.is_land:
			return_string = return_string + 'Land\n'
		if self.is_water:
			return_string = return_string + 'Water\n'
		if self.is_supply_center:
			return_string = return_string + 'Supply center\n'
		return_string = return_string + 'Adjacent territories: ' + ''.join(list(map(lambda adjacent_territory: adjacent_territory.name + ', ', self.adjacent_territories))) + '\n'
		if self.owner != None:
			return_string = return_string + 'Owner: ' + self.owner.name + '\n'
		if len(self.units) > 0:
			return_string = return_string + 'Units: ' + ''.join(list(map(lambda unit: unit.identifier() + ', ', self.units))) + '\n'
		return return_string

	def set_owner(self, player):
		if self.owner != None:
			self.owner.territories.pop(self.name, None)
		self.owner = player
		self.owner.territories.append(self)

	def is_landlocked(self):
		return bool(len(list(filter(lambda adjacent_territory: adjacent_territory.is_water, self.adjacent_territories))))

class Nation():
	def __init__(self, name):
		self.name = name
		self.territories = []
		self.units = []
		self.productive_territories = []
		self.player_type = 'ai'

	def __str__(self):
		return 'Nation ' + self.name + '\nTerritories: ' + ''.join(list(map(lambda territory: territory.name + ', ', self.territories))) + '\nUnits: ' + ''.join(list(map(lambda unit: unit.identifier() + ', ', self.units))) + '\nProductive territories: ' + ''.join(list(map(lambda territory: territory.name + ', ', self.productive_territories)))

	def finalize_starting_territory(self):
		self.productive_territories = list(filter(lambda territory: territory.is_supply_center, self.territories))

	def maximum_units(self):
		return len(list(filter(lambda territory: territory.is_supply_center, self.territories)))

	def automatic_turn(self):
		pass # TODO - For AI players. Equal chance for each individual action. Convoy only if allied land unit is adjacent. Support only if allied land unit is moving into adjacent.

class Unit():
	def __init__(self, is_navy, owner, territory):
		self.is_navy = is_navy
		self.owner = owner
		self.owner.units.append(self)
		self.last_territory = None
		self.territory = territory
		self.territory.units.append(self)
		self.power = 1
		self.action = 'hold'
		self.action_target = None
		self.convoys = []

	def __str__(self):
		if self.is_navy:
			return_string = 'Navy '
		else:
			return_string = 'Army '
		return_string = return_string + self.territory.name + '\nOwner: ' + self.owner.name + '\n'
		if self.last_territory:
			return_string = return_string + 'Last territory: ' + self.last_territory.name + '\n'
		return_string = return_string + 'Identifier: ' + self.identifier()
		if self.action_target != None:
			return_string = return_string + '\nCurrent action: ' + self.action + ' to\n---' + self.action_target + '\n---'
		return_string = return_string + '\nAvailable movement targets: ' + ''.join(list(map(lambda territory: territory.name + ', ', self.available_movement_targets())))
		return return_string

	def identifier(self):
		if self.is_navy:
			return 'N ' + self.territory.abbreviations[0]
		else:
			return 'A ' + self.territory.abbreviations[0]

	def move_to(self, territory):
		self.action = 'move'
		self.action_target = territory

	def support_to(self, unit):
		self.action = 'support'
		self.action_target = unit

	def convoy_to(self, unit):
		self.action = 'convoy'
		self.action_target = unit

	def resolve_action(self):
		if self.action == 'move':
			self.last_territory = self.territory
			self.territory.units.pop(self, None)
			self.territory = self.action_target
			self.territory.units.append(self)
			if self.is_navy == False:
				while self.territory.is_land == False:
					self.territory.units.pop(self, None)
					self.territory = random.choice(self.available_movement_targets())
					self.territory.units.append(self)
		elif self.action == 'support':
			if self.action_target.territory in self.available_movement_targets():
				self.action_target.power = self.action_target.power + 1
				self.power = self.power - 1
		elif self.action == 'convoy':
			self.action_target.convoys.append(self)
		self.action = 'hold'
		self.action_target = None
		self.convoys = []

	def available_movement_targets(self):
		if self.is_navy:
			if self.territory.is_water:
				return self.territory.adjacent_territories
			else:
				movement_targets = self.territory.adjacent_water + list(filter(lambda land_territory: True if self.last_territory in land_territory.adjacent_water else False, self.territory.adjacent_land))
				if self.last_territory == None:
					return movement_targets
				else:
					return movement_targets.append(self.last_territory)
		else:
			return self.territory.adjacent_land + list(filter(lambda water_territory: not set(self.convoys).isdisjoint(water_territory.units), self.territory.adjacent_water)) + list(territory for territory in [convoy.adjacent_land for convoy in self.convoys])

class Command():
	def __init__(self, help_string, action):
		self.help_string = help_string
		self.action = action

	def action(self, query):
		self.action(query)

def simplify_string(string):
	return ''.join(list([character for character in string if character.isalpha()])).lower()

def help_command(query):
	if len(query) == 1:
		print('Key: LITERAL (Required) [Optional]\nWhen referring to the name of a unit, use the name of the territory it\'s on.\n')
		for command in commands.values():
			print(command.help_string)
	elif query[1] in commands:
		print(commands[query[1]].help_string)
	else:
		print('Unknown command \'' + query[1] + '\'.')

def view_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if len(query) < 2:
		print(commands['view'].help_string)
	elif query[1] == 'map':
		print(game_map) # TODO - show image representation of map on view map.
	elif len(query) < 3:
		print(commands['view'].help_string)
	elif query[1] == 'territory':
		if query[2] in game_map.territories:
			print(game_map.territories[query[2]])
		else:
			print('Unknown territory \'' + query[2] + '\'.')
	elif query[1] == 'nation':
		if query[2] in game_map.nations:
			print(game_map.nations[query[2]])
		else:
			print('Unknown nation \'' + query[2] + '\'.')
	elif query[1] == 'unit':
		if query[2] in game_map.territories:
			if len(game_map.territories[query[2]].units) > 0:
				for unit in game_map.territories[query[2]].units:
					print(unit)
			else:
				print(game_map.territories[query[2]].name + ' doesn\'t contain a unit.')
		else:
			print('Unknown territory \'' + query[2] + '\'.')
	else:
		print(commands['view'].help_string)

def new_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if in_game:
		if len(query) < 3:
			print(commands['new'].help_string)
		elif len(player_nation.units) >= player_nation.maximum_units():
			print('Already at maximum units.')
		else:
			if query[1] in player_nation.territories:
				if game_map.territories[query[1]] in player_nation.productive_territories:
					if query[2] == 'yes':
						if not game_map.territories[query[1]].is_landlocked():
							Unit(True, player_nation, game_map.territories[query[1]])
						else:
							print('Navies must be placed on a coast.')
					elif query[2] == 'no':
						Unit(False, player_nation, game_map.territories[query[1]])
					else:
						print(commands['new'].help_string)
				else:
					print(game_map.territories[query[1]].name + ' is not a productive territory for your nation.')
			else:
				print('Unknown/uncontrolled territory \'' + query[1] + '\'.')
	else:
		if len(query) < 4:
			print(commands['new'].help_string)
		else:
			if query[1] in game_map.territories:
				if query[2] in game_map.nations:
					if query[3] == 'yes':
						Unit(True, game_map.nations[query[2]], game_map.territories[query[1]])
					elif query[3] == 'no':
						Unit(False, game_map.nations[query[2]], game_map.territories[query[1]])
					else:
						print(commands['new'].help_string)
				else:
					print('Unknown nation \'' + query[2] + '\'.')
			else:
				print('Unknown territory \'' + query[1] + '\'.')

def modify_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if len(query) < 4:
		print(commands['modify'].help_string)
	elif query[1] == 'map':
		pass # TODO
	elif query[1] == 'territory':
		pass # TODO
	elif query[1] == 'unit':
		pass # TODO
	else:
		print(commands['modify'].help_string)

	print('Modify.') # TODO - For map, season should be modifiable.

def destroy_command(query):
	if game_map == None:
		print('There is no map.')
		return

	# TODO - While in-game, disallow other actions while current units > max units. Disable if current units < max units. Only allow own units.
	print('Destroy.') # TODO

def move_command(query):
	if game_map == None:
		print('There is no map.')
		return

	print('Move.') # TODO - Restrict unit actions from within function.

def new_map_command(query):
	global game_map
	game_map = Map()
	for territory in game_map.territories.values():
		territory.finalize_adjacencies()

def standardize_command(query):
	if game_map == None:
		print('There is no map.')
		return

	game_map.standard_setup()

def start_command(query):
	if game_map == None:
		print('There is no map.')
		return

	global player_nation
	global in_game
	global commands
	if len(query) < 2:
		print(commands['start'].help_string)
	else:
		if query[1] in game_map.nations:
			player_nation = game_map.nations[query[1]]
			player_nation.player_type = 'human'
			for nation in game_map.nations.values():
				nation.finalize_starting_territory()
			in_game = True
			commands = game_commands
		else:
			print('Unknown nation \'' + query[1] + '\'.')

def iterate_command(query):
	if game_map == None:
		print('There is no map.')
		return

	print('Iterate.') # TODO - Return projected rankings, best alliance for target nation, and moveset of fastest win for target nation.

def clear_command(query):
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def convoy_command(query):
	if game_map == None:
		print('There is no map.')
		return

	print('Convoy.') # TODO

def support_command(query):
	if game_map == None:
		print('There is no map.')
		return

	print('Support.') # TODO

def end_command(query):
	if game_map == None:
		print('There is no map.')
		return

	global player_nation
	global in_game
	global commands
	player_nation.player_type = 'ai'
	player_nation = None
	in_game = False
	commands = setup_commands

def resolve_command(query):
	if game_map == None:
		print('There is no map.')
		return

	print('Resolve.') # TODO

print('Diplomat v1.0 by Travis Martin.')
print('Type \'help\' for a list of commands.')

help_string = 'Type \'help\' for a list of commands.'
setup_commands = {
	'help': Command('HELP [Command name]\t\t\t\tGives information about commands.', help_command),
	'newmap': Command('NEWMAP\t\t\t\t\t\tStarts a new game with an empty map.', new_map_command),
	'standardize': Command('STANDARDIZE\t\t\t\t\tSets up the map like a standard game of Diplomacy.', standardize_command),
	'view': Command('VIEW (MAP/TERRITORY/NATION/UNIT) (Name)\t\tGives information about a territory, nation, or unit, or the map (leave name blank).', view_command),
	'new': Command('NEW (Territory) (Nation) (Is Navy YES/NO)\tAdds a unit to a territory.', new_command),
	'destroy': Command('DESTROY (Name)\t\t\t\t\tDestroys a unit.', destroy_command),
	'modify': Command('MODIFY (MAP/TERRITORY/UNIT) (Name) (Parameter)\tModifies a specific parameter of a territory or unit.', modify_command),
	'start': Command('START (Nation)\t\t\t\t\tStarts playing a game as the selected nation.', start_command),
	'iterate': Command('ITERATE (Iterations) [Nation]\t\t\tAutomatically plays several games of Diplomacy from the current map state. Shows projections for selected nation.', iterate_command),
	'clear': Command('CLEAR\t\t\t\t\t\tClears the screen.', clear_command),
	'exit': Command('EXIT\t\t\t\t\t\tExits the program.', lambda query: None)
}
game_commands = {
	'help': Command('HELP [Command name]\t\t\t\tGives information about commands.', help_command),
	'view': Command('VIEW (MAP/TERRITORY/NATION/UNIT) (Name)\t\tGives information about a territory, nation, or unit, or the map (leave name blank).', view_command),
	'new': Command('NEW (Territory) (Is Navy YES/NO)\t\tAdds a unit to a territory.', new_command),
	'destroy': Command('DESTROY (Name)\t\t\t\t\tDestroys a unit.', destroy_command),
	'move': Command('MOVE (Starting territory) (Destination)\t\tMoves a unit from one territory to another.', move_command),
	'convoy': Command('CONVOY (Unit) (Target territory)\t\tSets a naval unit as convoying.', convoy_command),
	'support': Command('SUPPORT (Unit) (Target territory)\t\tSets a unit as supporting.', support_command),
	'end': Command('END\t\t\t\t\t\tStops playing the current game.', end_command),
	'resolve': Command('RESOLVE\t\t\t\t\t\tResolves the current turn.', resolve_command),
	'clear': Command('CLEAR\t\t\t\t\t\tClears the screen.', clear_command),
	'exit': Command('EXIT\t\t\t\t\t\tExits the program.', lambda query: None)
}
commands = setup_commands

in_game = False
player_nation = None
game_map = None

command = [None]
while command[0] != 'exit':
	command = list(map(lambda word: simplify_string(word), input('>').split()))

	if len(command) == 0:
		print(help_string)
		command = [None] # So that the loop doesn't throw an error.
	elif command[0] in commands:
		commands[command[0]].action(command)
	else:
		print(help_string)
