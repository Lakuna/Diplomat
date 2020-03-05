import random
from os import system, name

class Map():
	def __init__(self):
		self.territories = {
			'ankara': Territory('Ankara', ['ank'], True, False, True, ['con', 'bla', 'arm', 'smy']),
			'belgium': Territory('Belgium', ['bel'], True, False, True, ['eng', 'pic', 'nth', 'hol', 'ruh', 'bur']),
			'berlin': Territory('Berlin', ['ber'], True, False, True, ['kie', 'bal', 'pru', 'mun', 'sil']),
			'brest': Territory('Brest', ['bre'], True, False, True, ['eng', 'mao', 'gas', 'par', 'pic']),
			'budapest': Territory('Budapest', ['bud'], True, False, True, ['tri', 'vie', 'gal', 'rum', 'ser']),
			'bulgaria': Territory('Bulgaria', ['bul'], True, False, True, ['ser', 'rum', 'bla', 'con', 'aeg', 'gre']),
			'constantinople': Territory('Constantinople', ['con'], True, True, True, ['bul', 'bla', 'ank', 'smy', 'aeg']),
			'denmark': Territory('Denmark', ['den'], True, True, True, ['hel', 'nth', 'ska', 'bal', 'kie', 'swe']),
			'edinburgh': Territory('Edinburgh', ['edi'], True, False, True, ['cly', 'nwg', 'nth', 'yor', 'lvp']),
			'greece': Territory('Greece', ['gre'], True, False, True, ['alb', 'ser', 'bul', 'aeg', 'ion']),
			'holland': Territory('Holland', ['hol'], True, False, True, ['nth', 'hel', 'kie', 'ruh', 'bel']),
			'kiel': Territory('Kiel', ['kie'], True, False, True, ['hol', 'hel', 'den', 'bal', 'ber', 'mun', 'ruh']),
			'liverpool': Territory('Liverpool', ['lvp', 'livp', 'lpl'], True, False, True, ['cly', 'nao', 'edi', 'yor', 'wal', 'iri']),
			'london': Territory('London', ['LON'], True, False, True, ['wal', 'yor', 'nth', 'eng']),
			'marseilles': Territory('Marseilles', ['mar', 'mars'], True, False, True, ['spa', 'gas', 'bur', 'lyo', 'pie']),
			'moscow': Territory('Moscow', ['mos'], True, False, True, ['stp', 'sev', 'ukr', 'war', 'liv']),
			'munich': Territory('Munich', ['mun'], True, False, True, ['ruh', 'kie', 'ber', 'sil', 'boh', 'tys', 'bur']),
			'naples': Territory('Naples', ['nap'], True, False, True, ['tyr', 'rom', 'apu', 'ion']),
			'norway': Territory('Norway', ['nor', 'nwy', 'norw'], True, False, True, ['ska', 'nth', 'nwg', 'bar', 'swe', 'fin', 'stp']),
			'paris': Territory('Paris', ['par'], True, False, True, ['bre', 'pic', 'bur', 'gas']),
			'portugal': Territory('Portugal', ['por'], True, False, True, ['mao', 'spa']),
			'rome': Territory('Rome', ['rom'], True, False, True, ['tus', 'ven', 'apu', 'nap', 'tyr']),
			'rumania': Territory('Rumania', ['ruh'], True, False, True, ['bud', 'sev', 'bla', 'bul', 'ser', 'gal', 'ukr']),
			'saintpetersburg': Territory('Saint Petersburg', ['stp', 'stpetersburg'], True, False, True, ['bot', 'fin', 'nar', 'bar', 'mos', 'liv']),
			'serbia': Territory('Serbia', ['ser'], True, False, True, ['alb', 'tri', 'bud', 'rum', 'bul', 'gre']),
			'sevastopol': Territory('Sevastopol', ['sev'], True, False, True, ['ukr', 'mos', 'arm', 'bla', 'rum']),
			'smyrna': Territory('Smyrna', ['smy'], True, False, True, ['con', 'ank', 'arm', 'syr', 'eas', 'aeg']),
			'spain': Territory('Spain', ['spa'], True, False, True, ['por', 'mao', 'gas', 'mer', 'lyo', 'wes']),
			'sweden': Territory('Sweden', ['swe'], True, False, True, ['nor', 'fin', 'bot', 'bal', 'den', 'ska']),
			'trieste': Territory('Trieste', ['tri'], True, False, True, ['ven', 'tyr', 'vie', 'bud', 'ser', 'alb', 'adr']),
			'tunis': Territory('Tunis', ['tun', 'tunisia'], True, False, True, ['nth', 'wes', 'tys', 'ion']),
			'venice': Territory('Venice', ['ven'], True, False, True, ['pie', 'tyr', 'tri', 'adr', 'apu', 'rom', 'tus']),
			'vienna': Territory('Vienna', ['vie'], True, False, True, ['tyr', 'boh', 'gal', 'bud', 'tri']),
			'warsaw': Territory('Warsaw', ['war'], True, False, True, ['sil', 'pru', 'liv', 'mos', 'ukr', 'gal']),
			'clyde': Territory('Clyde', ['cly'], True, False, False, ['nao', 'nwg', 'edi', 'lvp']),
			'yorkshire': Territory('Yorkshire', ['yor', 'york', 'yonkers'], False, True, False, ['edi', 'nth', 'lon', 'wal', 'lvp']),
			'wales': Territory('Wales', ['wal'], True, False, False, ['iri', 'lvp', 'yor', 'lon', 'eng']),
			'picardy': Territory('Picardy', ['pic'], True, False, False, ['bre', 'eng', 'bel', 'bur', 'par']),
			'gascony': Territory('Gascony', ['gas'], True, False, False, ['bre', 'par', 'bur', 'mar', 'spa', 'mao']),
			'burgundy': Territory('Burgundy', ['bur'], True, False, False, ['par', 'pic', 'bel', 'ruh', 'mun', 'mar', 'gas']),
			'northafrica': Territory('North Africa', ['naf', 'nora'], True, False, False, ['mao', 'wes', 'tun']),
			'ruhr': Territory('Ruhr', ['ruh'], True, False, False, ['bel', 'hol', 'kie', 'mun', 'bur']),
			'prussia': Territory('Prussia', ['pru'], True, False, False, ['ber', 'bal', 'liv', 'war', 'sil']),
			'silesia': Territory('Silesia', ['sil'], True, False, False, ['mun', 'ber', 'pru', 'war', 'gal', 'boh']),
			'piedmont': Territory('Piedmont', ['pie'], True, False, False, ['mar', 'tyr', 'ven', 'tus', 'lyo']),
			'tuscany': Territory('Tuscany', ['tus'], True, False, False, ['lyo', 'pie', 'ven', 'rom', 'tys']),
			'apulia': Territory('Apulia', ['apu'], True, False, False, ['ven', 'adr', 'ion', 'nap', 'rom']),
			'tyrolia': Territory('Tyrolia', ['tyr', 'tyl', 'trl'], True, False, False, ['pie', 'mun', 'boh', 'vie', 'tri', 'ven']),
			'galicia': Territory('Galicia', ['gal'], True, False, False, ['boh', 'sil', 'war', 'ukr', 'rum', 'bud', 'vie']),
			'bohemia': Territory('Bohemia', ['boh'], True, False, False, ['mun', 'sil', 'gal', 'vie', 'tyr']),
			'finland': Territory('Finland', ['fin'], True, False, False, ['swe', 'nor', 'stp', 'bot']),
			'livonia': Territory('Livonia', ['lvn', 'livo', 'lvo', 'lva'], True, False, False, ['bot', 'stp', 'mos', 'war', 'pru', 'bal']),
			'ukraine': Territory('Ukraine', ['ukr'], True, False, False, ['war', 'mos', 'sev', 'rum', 'gal']),
			'albania': Territory('Albania', ['alb'], True, False, False, ['adr', 'tri', 'ser', 'gre', 'ion']),
			'armenia': Territory('Armenia', ['arm'], True, False, False, ['ank', 'bla', 'syr', 'smy', 'sev']),
			'syria': Territory('Syria', ['syr'], True, False, False, ['eas', 'smy', 'arm']),
			'northatlanticocean': Territory('North Atlantic Ocean', ['nao', 'northatlantic'], False, True, False, ['cly', 'lvp', 'iri', 'mao', 'nwg']),
			'midatlanticocean': Territory('Mid-Atlantic Ocean', ['mao', 'midatlantic', 'mid', 'mat'], False, True, False, ['nao', 'iri', 'eng', 'bre', 'gas', 'spa', 'por', 'naf', 'wes']),
			'norwegiansea': Territory('Norwegian Sea', ['nwg', 'norwsea', 'nrg', 'norwegian'], False, True, False, ['nao', 'bar', 'nor', 'nth', 'edi', 'cly']),
			'northsea': Territory('North Sea', ['nth', 'norsea', 'nts'], False, True, False, ['nwg', 'nor', 'ska', 'den', 'hel', 'hol', 'bel', 'eng', 'lon', 'yor', 'edi']),
			'englishchannel': Territory('English Channel', ['eng', 'english', 'channel', 'ech'], False, True, False, ['mao', 'iri', 'wal', 'lon', 'bel', 'pic', 'bre', 'nth']),
			'irishsea': Territory('Irish Sea', ['iri', 'irish'], False, True, False, ['mao', 'nao', 'lvp', 'wal', 'eng']),
			'heligolandbight': Territory('Heligoland Bight', ['hel', 'heligoland'], False, True, False, ['nth', 'den', 'kie', 'hol']),
			'skagerrack': Territory('Skagerrack', ['ska'], False, True, False, ['nth', 'nor', 'swe', 'den']),
			'balticsea': Territory('Baltic Sea', ['bal', 'baltic'], False, True, False, ['den', 'swe', 'bot', 'liv', 'pru', 'ber', 'kie']),
			'gulfofbothnia': Territory('Gulf of Bothnia', ['bot', 'gob', 'both', 'gulfofb', 'bothnia'], False, True, False, ['swe', 'fin', 'stp', 'liv', 'bal']),
			'barentssea': Territory('Barents Sea', ['bar', 'barents'], False, True, False, ['nor', 'nwg', 'stp']),
			'westernmediterranean': Territory('Western Mediterranean', ['wes', 'wmed', 'west', 'western', 'westmed', 'wms', 'wme', 'westmediterranean'], False, True, False, ['spa', 'mao', 'naf', 'tun', 'tys', 'lyo']),
			'gulfoflyon': Territory('Gulf of Lyon', ['lyo', 'gol', 'gulfofl', 'lyon'], False, True, False, ['spa', 'mar', 'pie', 'tus', 'tys', 'wes']),
			'tyrrheniansea': Territory('Tyrrhenian Sea', ['tys', 'tyrr', 'tyrrhenian', 'tyn', 'tyh'], False, True, False, ['lyo', 'tus', 'rom', 'nap', 'ion', 'tun', 'wes']),
			'ioniansea': Territory('Ionian Sea', ['ion', 'ionian'], False, True, False, ['tun', 'tys', 'nap', 'apu', 'adr', 'alb', 'gre', 'aeg', 'eas']),
			'adriaticsea': Territory('Adriatic Sea', ['adr', 'adriatic'], False, True, False, ['ven', 'tri', 'alb', 'ion', 'apu']),
			'aegeansea': Territory('Aegean Sea', ['aeg', 'aegean'], False, True, False, ['ion', 'gre', 'bul', 'con', 'smy', 'eas']),
			'easternmediterranean': Territory('Eastern Mediterranean', ['eas', 'emed', 'east', 'eastern', 'eastmed', 'ems', 'eme', 'eastmediterranean'], False, True, False, ['ion', 'aeg', 'smy', 'syr']),
			'blacksea': Territory('Black Sea', ['bla', 'black'], False, True, False, ['bul', 'rum', 'sev', 'arm', 'ank', 'con']),
		}
		territory_abbreviation_dictionary = {}
		for territory in self.territories.values():
			for abbreviation in territory.abbreviations:
				territory_abbreviation_dictionary[abbreviation] = territory
		self.territories.update(territory_abbreviation_dictionary)

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
		self.adjacent_territories = list(map(lambda territory_name: game_map.territories[territory_name], list(filter(lambda adjacent_territory_name: adjacent_territory_name in game_map.territories, self.adjacent_territory_names))))
		self.adjacent_water = list(filter(lambda territory: territory.is_water, self.adjacent_territories))
		self.adjacent_land = list(filter(lambda territory: territory.is_land, self.adjacent_territories))

	def __str__(self):
		return_string = 'Territory ' + self.name + '\nAbbreviations: ' + ''.join(list(map(lambda abbreviation: abbreviation + ', ', self.abbreviations)))
		if self.is_land:
			return_string = return_string + '\nLand'
		if self.is_water:
			return_string = return_string + '\nWater'
		if self.is_supply_center:
			return_string = return_string + '\nSupply center'
		return_string = return_string + '\nAdjacent territories: ' + ''.join(list(map(lambda adjacent_territory: adjacent_territory.name + ', ', self.adjacent_territories)))
		if self.owner != None:
			return_string = return_string + '\nOwner: ' + self.owner.name
		if len(self.units) > 0:
			return_string = return_string + '\nUnits: ' + ''.join(list(map(lambda unit: unit.identifier() + ', ', self.units)))
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
		pass # TODO - For AI players. Equal chance for each individual action. Convoy only if allied land unit is adjacent. Support only if allied land unit is moving into adjacent. Return all unit powers to 1.

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
		return_string = return_string + self.territory.name + '\nOwner: ' + self.owner.name
		if self.last_territory:
			return_string = return_string + '\nLast territory: ' + self.last_territory.name
		return_string = return_string + '\nIdentifier: ' + self.identifier()
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
		# Convoy applied as command is given to allow move to work correctly.
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

def help_command(query):
	if len(query) == 1:
		print('Key: LITERAL (Required) [Optional]\nWhen referring to the name of a unit, use the name of the territory it\'s on.\nWhen referring to the name of the map, use any non-blank string.\n')
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
				if len(game_map.territories[query[1]].units) > 0:
					print(game_map.territories[query[1]].name + ' already has a unit.')
				elif game_map.territories[query[1]] in player_nation.productive_territories:
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
				if len(game_map.territories[query[1]].units) > 0:
					print(game_map.territories[query[1]].name + ' already has a unit.')
				elif query[2] in game_map.nations:
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

	if len(query) < 5:
		print(commands['modify'].help_string)
	elif query[1] == 'map':
		if query[3] == 'season':
			if query[4] == 'spring':
				game_map.season = 'spring'
			elif query[4] == 'fall':
				game_map.season = 'fall'
			else:
				print('Available options: SPRING/FALL')
		else:
			print('Available options: SEASON')
	elif query[1] == 'territory':
		if query[2] in game_map.territories:
			if query[3] == 'supplycenter':
				if query[4] == 'yes':
					game_map.territories[query[2]].is_supply_center = True
				elif query[4] == 'no':
					game_map.territories[query[2]].is_supply_center = False
				else:
					print('Available options: YES/NO')
			elif query[3] == 'owner':
				if query[4] in game_map.nations:
					game_map.territories[query[3]].owner = game_map.nations[query[4]]
				else:
					print('Unknown nation \'' + query[4] + '\'.')
			else:
				print('Available options: SUPPLYCENTER/OWNER')
		else:
			print('Unknown territory \'' + query[2] + '\'.')
	else:
		print(commands['modify'].help_string)

def destroy_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if in_game:
		if len(player_nation.units) <= player_nation.maximum_units():
			print('Cannot remove units while at or below maximum units.')
		elif query[1] in player_nation.territories:
			for unit in game_map.territories[query[1]].units:
				if unit.owner = player_nation:
					unit.territory.units.pop(unit, None)
					unit.owner.units.pop(unit, None)
		else:
			print('Unknown territory \'' + query[1] + '\'.')
	else:
		if query[1] in game_map.territories:
			for unit in game_map.territories[query[1]].units:
				unit.territory.units.pop(unit, None)
				unit.owner.units.pop(unit, None)
		else:
			print('Unknown territory \'' + query[1] + '\'.')

def move_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if len(player_nation.units) > player_nation.maximum_units():
		print('Too many units. Must remove some before making actions.')
		return

	if len(query) < 3:
		print(commands['move'].help_string)
	else:
		if query[1] in game_map.territories:
			if len(game_map.territories[query[1]].units) > 0:
				for unit in game_map.territories[query[1]].units.values():
					if unit.owner = player_nation:
						if query[2] in unit.adjacent_territories:
							unit.action = 'move'
							unit.action_target = game_map.territories[query[2]]
			else:
				print('No units in ' + game_map.territories[query[1]].name + '.')
		else:
			print('Unknown territory \'' + query[1] + '\'.')

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

	if len(player_nation.units) > player_nation.maximum_units():
		print('Too many units. Must remove some before making actions.')
		return

	if len(query) < 3:
		print(commands['convoy'].help_string)
	elif query[1] in game_map.territories:
		if len(game_map.territories[query[1]].units) > 0:
			for unit in game_map.territories[query[1]].units.values():
				if unit.owner == player_nation:
					unit.power = unit.power - 1
					# TODO
		else:
			print('No units in ' + game_map.territories[query[1]].name + '.')
	else:
		print('Unknown territory \'' + query[1] + '\'.')

	print('Convoy.') # TODO

def support_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if len(player_nation.units) > player_nation.maximum_units():
		print('Too many units. Must remove some before making actions.')
		return

	print('Support.') # TODO

def end_command(query):
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
	'view': Command('VIEW (MAP/TERRITORY/NATION/UNIT) (Name)\t\tGives information about a territory, nation, or unit, or the map.', view_command),
	'new': Command('NEW (Territory) (Nation) (Is Navy YES/NO)\tAdds a unit to a territory.', new_command),
	'destroy': Command('DESTROY (Name)\t\t\t\t\tDestroys a unit.', destroy_command),
	'modify': Command('MODIFY (MAP/TERRITORY) (Name) (Parameter) (Value)\tModifies a specific parameter of the map, or a territory or unit.', modify_command),
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
	command = list(map(lambda word: ''.join(list([character for character in word if character.isalpha()])).lower(), input('\n>').split()))

	if len(command) == 0:
		print(help_string)
		command = [None] # So that the loop doesn't throw an error.
	elif command[0] in commands:
		commands[command[0]].action(command)
	else:
		print(help_string)
