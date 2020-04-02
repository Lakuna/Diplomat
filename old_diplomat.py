print('This file is no longer functional.')

"""

import random
import copy
from os import system, name

class Map():
	def resolve_turn(self):
		global active_nation

		for nation in list(filter(lambda nation: nation.player_type == 'ai', self.nations.values())):
			if len(nation.units) < nation.maximum_units(): # Build up to maximum units.
				# print(nation.name + ' building up to maximum units.')
				player_nation = active_nation
				active_nation = nation
				while len(nation.units) < nation.maximum_units():
					command = ['new']
					open_supply_centers = list(filter(lambda territory: territory.is_supply_center and len(territory.units) == 0 and territory.owner == nation, nation.productive_territories))
					if len(open_supply_centers) == 0:
						# print(nation.name + ' cannot make more units because it has no open supply centers.')
						break
					else:
						territory = random.choice(open_supply_centers)
						command.append(territory.abbreviations[0])
						if territory.is_landlocked:
							command.append('no')
						else:
							command.append(random.choice(['yes', 'no']))
						commands[command[0]].action(command)
				active_nation = player_nation

		for nation in list(filter(lambda nation: nation.player_type == 'ai', self.nations.values())):
			if len(nation.units) > nation.maximum_units(): # Cut down to maximum units.
				# print(nation.name + ' cutting down to maximum units.')
				player_nation = active_nation
				active_nation = nation
				while len(nation.units) > nation.maximum_units():
					command = ['destroy']
					unit = random.choice(nation.units)
					command.append(unit.territory.abbreviations[0])
					commands[command[0]].action(command)
				active_nation = player_nation

		for nation in list(filter(lambda nation: nation.player_type == 'ai', self.nations.values())):
			nation.automatic_turn() # Assign commands.

		output_dictionary = {}
		all_units = []
		for nation in self.nations.values():
			for unit in nation.units:
				all_units.append(unit)
		for unit in list(filter(lambda unit: unit.action == 'convoy', all_units)):
			output_dictionary[unit.old_identifier] = unit.resolve_action()
		for unit in list(filter(lambda unit: unit.action == 'move', all_units)):
			output_dictionary[unit.old_identifier] = unit.resolve_action()
		for unit in list(filter(lambda unit: unit.action == 'support', all_units)):
			output_dictionary[unit.old_identifier] = unit.resolve_action()
		for unit in list(filter(lambda unit: unit.action == 'hold', all_units)):
			output_dictionary[unit.old_identifier] = unit.resolve_action()

		for territory in self.territories.values():
			if len(territory.units) > 1:
				bounce_all = False
				maximum_power = -1
				for unit in territory.units:
					if unit.power > maximum_power:
						maximum_power = unit.power
						bounce_all = False
					elif unit.power == maximum_power:
						bounce_all = True
				if bounce_all:
					for unit in territory.units:
						unit.territory.units.remove(unit)
						if unit.last_territory == None:
							unit.owner.units.remove(unit)
						elif len(unit.last_territory.units) > 0:
							unit.owner.units.remove(unit)
						else:
							unit.territory = unit.last_territory
							unit.territory.units.append(unit)
				else:
					for unit in territory.units:
						if unit.power == 0:
							unit.territory.units.remove(unit)
							movement_targets = list(filter(lambda territory: len(territory.units) == 0, unit.available_movement_targets()))
							if len(movement_targets) > 0:
								unit.territory = random.choice(movement_targets)
								unit.territory.units.append(unit)
							else:
								unit.owner.units.remove(unit)
						elif unit.power < maximum_power:
							unit.territory.units.remove(unit)
							if unit.last_territory == None:
								unit.owner.units.remove(unit)
							elif len(unit.last_territory.units) > 0:
								unit.owner.units.remove(unit)
							else:
								unit.territory = unit.last_territory
								unit.territory.units.append(unit)

		for nation in self.nations.values(): # Set all units back to 1 power.
			for unit in nation.units:
				unit.power = 1

		if self.season == 'spring':
			self.season = 'fall'
		else:
			self.season = 'spring'
			for territory in self.territories.values():
				if len(territory.units) > 0:
					old_owner = None
					if territory.owner != None:
						territory.owner.territories.remove(territory)
						old_owner = territory.owner
					territory.owner = territory.units[0].owner
					territory.owner.territories.append(territory)
					if old_owner != territory.owner:
						pass # print(territory.name + ' switched control to ' + territory.owner.name + '.')

		for nation in self.nations.values():
			if len(nation.territories) >= 20:
				global current_game_placements
				current_game_placements = {}
				temp_nations = list(self.nations.values())
				place = 1
				while len(temp_nations) > 0:
					most_supply_centers = 0
					for nation in temp_nations:
						if most_supply_centers < len(list(filter(lambda territory: territory.is_supply_center, nation.territories))):
							most_supply_centers = len(list(filter(lambda territory: territory.is_supply_center, nation.territories)))
					for nation in temp_nations:
						if len(list(filter(lambda territory: territory.is_supply_center, nation.territories))) == most_supply_centers:
							current_game_placements[nation] = place
							temp_nations.remove(nation)
							place = place + 1
				break

		# print('Finished turn.')
		return output_dictionary # For getting turn moves in iteration.

class Unit():
	def resolve_action(self):
		self.old_identifier = self.identifier()
		if self.action == 'move':
			self.last_territory = self.territory
			self.territory.units.remove(self)
			self.territory = self.action_target
			self.territory.units.append(self)
			output_string = self.old_identifier + ' -> ' + self.territory.abbreviations[0]
		elif self.action == 'support':
			self.power = self.power - 1
			if len(self.action_target.units) > 0:
				for unit in self.action_target.units:
					if unit.owner == self.owner:
						unit.power = unit.power + 1
						if unit.action == 'move':
							output_string = self.old_identifier + ' -S- ' + unit.old_identifier + ' -> ' + unit.action_target.abbreviations[0]
						else:
							output_string = self.old_identifier + ' -S- ' + unit.old_identifier + ' HOLD'
			else:
				output_string = self.old_identifier + ' HOLD (illegal support).'
		elif self.action == 'convoy':
			self.power = self.power - 1
			if self.action_target.action == 'move':
				output_string = self.old_identifier + ' -C- ' + self.action_target.old_identifier + ' -> ' + self.action_target.action_target.abbreviations[0]
			else:
				output_string = self.old_identifier + ' HOLD (illegal convoy).'
			# Convoy applied as command is given to allow move to work correctly.
		else:
			output_string = self.identifier() + ' HOLD'
		self.action = 'hold'
		self.action_target = None
		self.convoys = []
		return output_string

def view_command(query):
	if game_map == None:
		print('There is no map.')
		return

	if len(query) < 2:
		print(commands['view'].help_string)
	elif query[1] == 'map':
		print(game_map)
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

def iterate_command(query):
	global game_map
	global in_game
	global commands
	global current_game_placements

	if game_map == None:
		print('There is no map.')
		return

	iterate_games = 1000

	placement_results = {}
	fastest_win_turns = {}
	total_win_turns = {}
	total_wins = {}
	for nation in game_map.nations.values():
		placement_results[nation.name] = 0
		fastest_win_turns[nation.name] = 9999
		total_win_turns[nation.name] = 0
		total_wins[nation.name] = 0

	selected_nation = None
	turn_one_identifiers = []
	best_first_moves = {}
	best_ally = None
	if len(query) > 1:
		if query[1] in game_map.nations:
			selected_nation = game_map.nations[query[1]].name
			for unit in game_map.nations[selected_nation.lower()].units:
				turn_one_identifiers.append(unit.identifier())
		else:
			print('Unknown nation \'' + query[1] + '\'.')

	for i in range(0, iterate_games):
		for command in commands_since_last_newmap:
			commands[command[0]].action(command) # Set up map to start.
		
		in_game = True
		commands = game_commands

		current_game_placements = None
		turns = 0
		turn_one_actions = {}

		while current_game_placements == None:
			turns = turns + 1
			turn_actions = game_map.resolve_turn() # Play game.
			if turns == 1 and selected_nation != None:
				for identifier in turn_one_identifiers:
					if identifier in turn_actions: # If the piece never won, it won't be in turn_actions.
						turn_one_actions[identifier] = turn_actions[identifier] # Save first moves.
		for nation in game_map.nations.values():
			placement_results[nation.name] = placement_results[nation.name] + current_game_placements[nation]
			if current_game_placements[nation] == 1:
				total_win_turns[nation.name] = total_win_turns[nation.name] + turns
				total_wins[nation.name] = total_wins[nation.name] + 1
				if turns < fastest_win_turns[nation.name]:
					fastest_win_turns[nation.name] = turns
		if selected_nation != None:
			if current_game_placements[game_map.nations[selected_nation.lower()]] == 1: # Only show moves that lead to a winning game.
				for action in turn_one_actions.values():
					if action in best_first_moves:
						best_first_moves[action] = best_first_moves[action] + 1
					else:
						best_first_moves[action] = 1
		print_progress_bar(i + 1, iterate_games, prefix='Simulation:', suffix='Complete', length=50)

		in_game = False
		commands = setup_commands

		# print('Game ' + str(i) + ' complete.')

	if selected_nation != None:
		print('Iteration complete for nation ' + selected_nation + '.\nRecommended next moves:')
		for move in best_first_moves:
			print(move + '\t\tWinrate: ' + str(best_first_moves[move] / iterate_games))
	print('\nNations by win from current map state:')
	for nation in game_map.nations.values():
		win_turn_string = 'N/A'
		if total_wins[nation.name] > 0:
			win_turn_string = str(total_win_turns[nation.name] / total_wins[nation.name])
		print(nation.name + '\t\tAverage placement: ' + str(placement_results[nation.name] / iterate_games) + '\tFastest win: ' + str(fastest_win_turns[nation.name]) + ' turns\tAverage win turn: ' + win_turn_string + '\tWinrate: ' + str(total_wins[nation.name] / iterate_games))

	for command in commands_since_last_newmap:
			commands[command[0]].action(command) # Reset map to start.

# Credit to Benjamin Cordier.
def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
	if iteration == total: 
		print()

"""