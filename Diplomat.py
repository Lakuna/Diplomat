class Map():
	def __init__(self):
		self.territories = {
			'Ankara': Territory('Ankara', ['ANK'], True, False, True, ['Constantinople', 'Black Sea', 'Armenia', 'Smyrna']),
			'Belgium': Territory('Belgium', ['BEL'], True, False, True, ['English Channel', 'Picardy', 'North Sea', 'Holland', 'Ruhr', 'Burgundy']),
			'Berlin': Territory('Berlin', ['BER'], True, False, True, ['Kiel', 'Baltic Sea', 'Prussia', 'Munich', 'Silesia']),
			'Brest': Territory('Brest', ['BRE'], True, False, True, ['English Channel', 'Mid-Atlantic Ocean', 'Gascony', 'Paris', 'Picardy']),
			'Budapest': Territory('Budapest', ['BUD'], True, False, True, ['Trieste', 'Vienna', 'Galicia', 'Rumania', 'Serbia']),
			'Bulgaria': Territory('Bulgaria', ['BUL'], True, False, True, ['Serbia', 'Rumania', 'Black Sea', 'Constantinople', 'Aegean Sea', 'Greece']),
			'Constantinople': Territory('Constantinople', ['CON'], True, True, True, ['Bulgaria', 'Black Sea', 'Ankara', 'Smyrna', 'Aegean Sea']),
			'Denmark': Territory('Denmark', ['DEN'], True, True, True, ['Heligoland Bight', 'North Sea', 'Skagerrack', 'Baltic Sea', 'Kiel']),
			'Edinburgh': Territory('Edinburgh', ['EDI'], True, False, True, ['Clyde', 'Norwegian Sea', 'North Sea', 'Yorkshire']),
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
			'Armenia': Territory('Armenia', ['ARM'], True, False, False, ['Ankara', 'Black Sea', 'Syria', 'Smyrna']),
			'Syria': Territory('Syria', ['SYR'], True, False, False, ['Eastern Mediterranean', 'Smyrna', 'Armenia']),
			'North Atlantic Ocean': Territory('North Atlantic Ocean', ['NAO', 'North Atlantic'], False, True, False, ['Clyde', 'Liverpool', 'Irish Sea', 'Mid-Atlantic Ocean', 'Norwegian Sea']),
			'Mid-Atlantic Ocean': Territory('Mid-Atlantic Ocean', ['MAO', 'Mid Atlantic Ocean', 'Mid Atlantic', 'MID', 'MAT'], False, True, False, ['North Atlantic Ocean', 'Irish Sea', 'English Channel', 'Brest', 'Gascony', 'Spain', 'Portugal', 'North Africa']),
			'Norwegian Sea': Territory('Norwegian Sea', ['NWG', 'NorwSea', 'NRG', 'Norwegian'], False, True, False, ['North Atlantic Ocean', 'Barents Sea', 'Norway', 'North Sea', 'Edinburgh', 'Clyde']),
			'North Sea': Territory('North Sea', ['NTH', 'NorSea', 'NTS'], False, True, False, ['Norwegian Sea', 'Norway', 'Skagerrack', 'Denmark', 'Heligoland Bight', 'Holland', 'Belgium', 'English Channel', 'London', 'Yorkshire', 'Edinburgh']),
			'English Channel': Territory('English Channel', ['ENG', 'English', 'Channel', 'ECH'], False, True, False, ['Mid-Atlantic Ocean', 'Irish Sea', 'Wales', 'London', 'Belgium', 'Picardy', 'Brest']),
			'Irish Sea': Territory('Irish Sea', ['IRI', 'Irish'], False, True, False, ['Mid-Atlantic Ocean', 'North Atlantic Ocean', 'Liverpool', 'Wales', 'English Channel']),
			'Heligoland Bight': Territory('Heligoland Bight', ['HEL', 'Heligoland'], False, True, False, ['North Sea', 'Denmark', 'Kiel', 'Holland']),
			'Skagerrack': Territory('Skagerrack', ['SKA'], False, True, False, ['North Sea', 'Norway', 'Sweden', 'Denmark']),
			'Baltic Sea': Territory('Baltic Sea', ['BAL', 'Baltic'], False, True, False, ['Denmark', 'Sweden', 'Gulf of Bothnia', 'Livonia', 'Prussia', 'Berlin', 'Kiel']),
			'Gulf of Bothnia': Territory('Gulf of Bothnia', ['BOT', 'GOB', 'BOTH', 'GulfOfB', 'Bothnia'], False, True, False, ['Sweden', 'Finland', 'Saint Petersburg', 'Livonia', 'Baltic Sea']),
			'Barents Sea': Territory('Barents Sea', ['BAR', 'Barents'], False, True, False, ['Norway', 'Norwegian Sea', 'Saint Petersburg']),
			'Western Mediterranean': Territory('Western Mediterranean', ['WES', 'WMED', 'West', 'Western', 'WestMed', 'WMS', 'WME', 'West Mediterranean'], False, True, False, ['Spain', 'Mid-Atlantic Ocean', 'North Africa', 'Tunis', 'Tyrrhenian', 'Gulf of Lyon']),
			'Gulf of Lyon': Territory('Gulf of Lyon', ['LYO', 'GOL', 'GulfOfL', 'Lyon'], False, True, False, ['Spain', 'Marseilles', 'Piedmont', 'Tuscany', 'Tyrrhenian Sea', 'Western Mediterranean']),
			'Tyrrhenian Sea': Territory('Tyrrhenian Sea', ['TYS', 'TYRR', 'Tyrrhenian', 'TYN', 'TYH'], False, True, False, ['Gulf of Lyon', 'Tuscany', 'Rome', 'Naples', 'Ionian Sea', 'Tunis', 'Western Mediterranean']),
			'Ionian Sea': Territory('Ionian Sea', ['ION', 'Ionian'], False, True, False, ['Tunis', 'Tyrrhenian Sea', 'Naples', 'Apulia', 'Adriatic Sea', 'Albania', 'Greece', 'Aegean Sea']),
			'Adriatic Sea': Territory('Adriatic Sea', ['ADR', 'Adriatic'], False, True, False, ['Venice', 'Trieste', 'Albania', 'Ionian Sea', 'Apulia']),
			'Aegean Sea': Territory('Aegean Sea', ['AEG', 'Aegean'], False, True, False, ['Ionian Sea', 'Greece', 'Bulgaria', 'Constantinople', 'Smyrna', 'Eastern Mediterranean']),
			'Eastern Mediterranean': Territory('Eastern Mediterranean', ['EAS', 'EMED', 'EAST', 'Eastern', 'EastMed', 'EMS', 'EME', 'East Mediterranean'], False, True, False, ['Ionian Sea', 'Aegean Sea', 'Smyrna', 'Syria']),
			'Black Sea': Territory('Black Sea', ['BLA', 'Black'], False, True, False, ['Bulgaria', 'Rumania', 'Sevastopol', 'Armenia', 'Ankara', 'Constantinople']),
		}
		for territory in self.territories:
			for abbreviation in territory.abbreviations:
				self.territories[abbreviation] = territory

		self.nations = {
			'Italy': Nation('Italy'),
			'Austria-Hungary': Nation('Austria-Hungary'),
			'Russia': Nation('Russia'),
			'Turkey': Nation('Turkey'),
			'England': Nation('England'),
			'France': Nation('France'),
			'Germany': Nation('Germany')
		}

	def standard_setup():
		self.territories['Piedmont'].set_owner(self.nations['Italy'])
		self.territories['Venice'].set_owner(self.nations['Italy'])
		self.territories['Tuscany'].set_owner(self.nations['Italy'])
		self.territories['Rome'].set_owner(self.nations['Italy'])
		self.territories['Apulia'].set_owner(self.nations['Italy'])
		self.territories['Naples'].set_owner(self.nations['Italy'])
		self.territories['Tyrrhenian Sea'].set_owner(self.nations['Italy'])
		Unit(False, self.nations['Italy'], self.territories['Rome'])
		Unit(False, self.nations['Italy'], self.territories['Venice'])
		Unit(True, self.nations['Italy'], self.territories['Naples'])
		self.nations['Italy'].finalize_starting_territory()

		self.territories['Tyrolia'].set_owner(self.nations['Austria-Hungary'])
		self.territories['Bohemia'].set_owner(self.nations['Austria-Hungary'])
		self.territories['Galicia'].set_owner(self.nations['Austria-Hungary'])
		self.territories['Vienna'].set_owner(self.nations['Austria-Hungary'])
		self.territories['Trieste'].set_owner(self.nations['Austria-Hungary'])
		self.territories['Budapest'].set_owner(self.nations['Austria-Hungary'])
		Unit(False, self.nations['Austria-Hungary'], self.territories['Vienna'])
		Unit(False, self.nations['Austria-Hungary'], self.territories['Budapest'])
		Unit(True, self.nations['Austria-Hungary'], self.territories['Trieste'])
		self.nations['Austria-Hungary'].finalize_starting_territory()

		self.territories['Finland'].set_owner(self.nations['Russia'])
		self.territories['Saint Petersburg'].set_owner(self.nations['Russia'])
		self.territories['Livonia'].set_owner(self.nations['Russia'])
		self.territories['Moscow'].set_owner(self.nations['Russia'])
		self.territories['Warsaw'].set_owner(self.nations['Russia'])
		self.territories['Ukraine'].set_owner(self.nations['Russia'])
		self.territories['Sevastopol'].set_owner(self.nations['Russia'])
		Unit(False, self.nations['Russia'], self.territories['Moscow'])
		Unit(False, self.nations['Russia'], self.territories['Warsaw'])
		Unit(True, self.nations['Russia'], self.territories['Saint Petersburg'])
		Unit(True, self.nations['Russia'], self.territories['Sevastopol'])
		self.nations['Russia'].finalize_starting_territory()

		self.territories['Constantinople'].set_owner(self.nations['Turkey'])
		self.territories['Ankara'].set_owner(self.nations['Turkey'])
		self.territories['Armenia'].set_owner(self.nations['Turkey'])
		self.territories['Smyrna'].set_owner(self.nations['Turkey'])
		self.territories['Syria'].set_owner(self.nations['Turkey'])
		self.territories['Eastern Mediterranean'].set_owner(self.nations['Turkey'])
		Unit(False, self.nations['Turkey'], self.territories['Constantinople'])
		Unit(False, self.nations['Turkey'], self.territories['Smyrna'])
		Unit(True, self.nations['Turkey'], self.territories['Ankara'])
		self.nations['Turkey'].finalize_starting_territory()

		self.territories['Clyde'].set_owner(self.nations['England'])
		self.territories['Edinburgh'].set_owner(self.nations['England'])
		self.territories['Liverpool'].set_owner(self.nations['England'])
		self.territories['Yorkshire'].set_owner(self.nations['England'])
		self.territories['Wales'].set_owner(self.nations['England'])
		self.territories['London'].set_owner(self.nations['England'])
		self.territories['Irish Sea'].set_owner(self.nations['England'])
		Unit(False, self.nations['England'], self.territories['Liverpool'])
		Unit(True, self.nations['England'], self.territories['Edinburgh'])
		Unit(True, self.nations['England'], self.territories['London'])
		self.nations['England'].finalize_starting_territory()

		self.territories['Gascony'].set_owner(self.nations['France'])
		self.territories['Brest'].set_owner(self.nations['France'])
		self.territories['Picardy'].set_owner(self.nations['France'])
		self.territories['Paris'].set_owner(self.nations['France'])
		self.territories['Burgundy'].set_owner(self.nations['France'])
		self.territories['Marseilles'].set_owner(self.nations['France'])
		Unit(False, self.nations['France'], self.territories['Paris'])
		Unit(False, self.nations['France'], self.territories['Marseilles'])
		Unit(True, self.nations['France'], self.territories['Brest'])
		self.nations['France'].finalize_starting_territory()

		self.territories['Ruhr'].set_owner(self.nations['Germany'])
		self.territories['Kiel'].set_owner(self.nations['Germany'])
		self.territories['Berlin'].set_owner(self.nations['Germany'])
		self.territories['Prussia'].set_owner(self.nations['Germany'])
		self.territories['Munich'].set_owner(self.nations['Germany'])
		self.territories['Silesia'].set_owner(self.nations['Germany'])
		Unit(False, self.nations['Germany'], self.territories['Berlin'])
		Unit(False, self.nations['Germany'], self.territories['Munich'])
		Unit(True, self.nations['Germany'], self.territories['Kiel'])
		self.nations['Germany'].finalize_starting_territory()

class Territory():
	def __init__(self, name, abbreviations, is_land, is_water, is_supply_center, adjacent_territory_names):
		self.name = name
		self.abbreviations = abbreviations
		self.is_land = is_land
		self.is_water = is_water
		self.is_supply_center = is_supply_center
		self.adjacent_territory_names = adjacent_territory_names
		self.owner = None
		self.unit = None
		self.map = game_map

	def set_owner(player):
		if self.owner != None:
			self.owner.territories.pop(self.name, None)
		self.owner = player
		self.owner.territories.append(self)

class Nation():
	def __init__(self, name):
		self.name = name
		self.territories = []
		self.units = []
		self.productive_territories = []

	def finalize_starting_territory():
		self.productive_territories = list(filter(lambda territory: territory.is_supply_center, self.territories))

class Unit():
	def __init__(self, is_navy, owner, territory):
		self.is_navy = is_navy
		self.owner = owner
		self.owner.units.append(self)
		self.last_territory = None
		self.territory = territory
		self.territory.unit = self

	def move_to(territory):
		self.territory.unit = None
		self.last_territory = self.territory
		self.territory = territory
		self.territory.unit = self

	def available_moves():
		if self.is_navy:
			if self.territory.is_water:
				return adjacent_territories()
			else:
				adjacent_water_territories = list(filter(lambda adjacent_water_territory: adjacent_water_territory.is_water, self.adjacent_territories()))
				adjacent_land_territories = list(filter(lambda adjacent_land_territory: adjacent_land_territory.is_land, self.adjacent_territories()))
				land_territories_adjacent_to_adjacent_water_territories = None
				return []
				# TODO
		else:
			return list(filter(lambda territory: territory.is_land, self.adjacent_territories()))

	def is_landlocked():
		return bool(len(list(filter(lambda adjacent_water_territory: adjacent_water_territory.is_water, self.adjacent_territories()))))

	def adjacent_territories():
		return list(lambda adjacent_territory: self.territory.map.territories[adjacent_territory], self.territory.adjacent_territory_names)

class Command():
	def __init__(self, help_string, action):
		self.help_string = help_string
		self.action = action

	def action(query):
		self.action(query)


def simplify_string(string):
	return ''.join(list([character for character in string if character.isalpha()])).lower()

print('Diplomat v1.0 by Travis Martin.')
print('Type \'help\' for a list of commands.')

help_string = 'Type \'help\' for a list of commands.'
commands = {
	'help': Command('HELP [Command name]\t\tGives information about commands.', lambda query:
		print(query)
		# TODO
		),
	'view': None, # TODO
	'newunit': None, # TODO
	'modify': None, # TODO
	'move': None, # TODO
	'newmap': None, # TODO
	'standardsetup': None, # TODO
	'exit': Command('EXIT\t\tExits the program.', lambda query: None)
}

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
