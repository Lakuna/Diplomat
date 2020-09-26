import __main__
import random

name = 'iterate'
usage = 'ITERATE [Batches] [Batch size] [Nation]'
description = 'Simulate games of Diplomacy.'
def execute(query):
	if __main__.active_board == None:
		return 'No active map.'

	batches = 10
	if len(query) > 0:
		try:
			batches = int(query.pop(0))
		except:
			pass

	batch_size = 100
	if len(query) > 0:
		try:
			batch_size = int(query.pop(0))
		except:
			pass

	selected_nation = None
	if len(query) > 0:
		for component in __main__.active_board.loadables.values():
			if (query[0] in component.names or component.identifier == query[0]) and isinstance(component, __main__.classes['Nation']):
				selected_nation = component.name
				break
		if selected_nation == None:
			return 'Nation [' + query[0] + '] not found.'

	watched_actions = {}
	nation_wins = {}
	nation_win_turns = {}
	total_turns = 0
	rank_total = {}
	fastest_win = {}

	# Batch loop.
	iterations = 0
	for j in range(batches):
		# Game loop.
		for i in range(batch_size):
			iterations += 1

			# Reset map.
			__main__.commands['load'].execute([__main__.active_board.name])

			winner = None

			turn_one_actions = []

			# Turn loop.
			while winner == None:
				# Increment turn.
				__main__.active_board.turn_number += 1

				# Set fleet actions. These must be done before army actions so that armies can use convoys.
				fleet_actions = []
				for fleet in list(filter(lambda component: isinstance(component, __main__.classes['Fleet']), __main__.active_board.units)):
					available_actions = []

					# Holding.
					available_actions.append(Action(fleet, 'hold', fleet.location.identifier))

					# Moving and supporting.
					for territory in fleet.movable_territories():
						available_actions.append(Action(fleet, 'move', territory.identifier))

					# Convoying.
					for convoyable_unit in fleet.convoyable_units():
						available_actions.append(Action(fleet, 'convoy', convoyable_unit.identifier))

					# Set action from available.
					fleet_actions.append(random.choice(available_actions))

				# Resolve fleet actions.
				for action in fleet_actions:
					action_string = action.resolve()
					if __main__.active_board.turn_number == 1 and action.unit.owner.name == selected_nation:
						turn_one_actions.append(action_string)

				# Set army actions.
				army_actions = []
				for army in list(filter(lambda component: isinstance(component, __main__.classes['Army']), __main__.active_board.units)):
					available_actions = []

					# Holding.
					available_actions.append(Action(army, 'hold', army.location.identifier))

					# Moving and supporting.
					for territory in army.movable_territories():
						available_actions.append(Action(army, 'move', territory.identifier))

					# Set action from available.
					army_actions.append(random.choice(available_actions))

				# Resolve army actions.
				for action in army_actions:
					action_string = action.resolve()
					if __main__.active_board.turn_number == 1 and action.unit.owner.name == selected_nation:
						turn_one_actions.append(action_string)

				# Resolve territory conflicts.
				for territory in __main__.active_board.territories:
					if len(territory.units) <= 1:
						continue # No conflicts to resolve.

					# Check if all units need to be bounced or just a loser.
					highest_power = 0
					units_at_highest_power = 0
					for unit in territory.units:
						if unit.power > highest_power:
							highest_power = unit.power
							units_at_highest_power = 1
					if units_at_highest_power > 1:
						highest_power += 1 # Increase highest power so that all units get bounced.

					for unit in territory.units:
						if unit.power >= highest_power:
							continue # Don't bounce the strongest unit.

						if unit.old_location == None or len(unit.old_location.units) > 0:
							unit.destroy() # Destroy unit if it can't bounce back.
							continue

						unit.set_location(unit.old_location) # Bounce unit.

				# Reset units.
				for unit in __main__.active_board.units:
					unit.power = 1

					if isinstance(unit, __main__.classes['Army']):
						unit.convoys = []

				if __main__.active_board.turn_number % 2 == 0:
					# Update territory ownership on even turns.
					for territory in __main__.active_board.territories:
						if len(territory.units) < 1:
							continue

						territory.set_owner(territory.units[0].owner)

					# Update unit count on even turns.
					for nation in __main__.active_board.nations:
						while len(nation.units) < len(list(filter(lambda territory: territory.is_supply_center, nation.territories))):
							current_units = len(nation.units)
							for productive_territory in nation.productive_territories:
								if len(productive_territory.units) > 0:
									continue # Don't create a unit on a productive territory that already has a unit.

								# Choose unit type.
								unit_type = 'Army'
								if len(productive_territory.adjacent_water) > 0:
									unit_type = random.choice(('Army', 'Fleet'))

								# Choose unit identifier.
								identifier = 0
								while str(identifier) in __main__.active_board.loadables:
									identifier += 1
								identifier = str(identifier)

								# Create unit.
								__main__.active_board.loadables[identifier] = __main__.classes[unit_type](__main__.active_board, identifier, nation.identifier, productive_territory.identifier)
								__main__.active_board.loadables[identifier].init_relationships()
							if len(nation.units) == current_units:
								break # Failed to create a unit - most likely because all productive territories were full.

						while len(nation.units) > len(list(filter(lambda territory: territory.is_supply_center, nation.territories))):
							random.choice(nation.units).destroy()

				# Check for end of game.
				for nation in __main__.active_board.nations:
					if len(list(filter(lambda territory: territory.is_supply_center, nation.territories))) >= 20:
						winner = nation
						break

				if __main__.active_board.turn_number > 1000:
					raise Exception('Game surpassed turn limit.')

				# End of turn.

			# Determine rankings.
			game_rankings = {}
			temp_nations = list(__main__.active_board.nations)
			rank = 1
			while len(temp_nations) > 0:
				most_supply_centers = 0
				for nation in temp_nations:
					if most_supply_centers < len(list(filter(lambda territory: territory.is_supply_center, nation.territories))):
						most_supply_centers = len(list(filter(lambda territory: territory.is_supply_center, nation.territories)))
				for nation in temp_nations:
					if len(list(filter(lambda territory: territory.is_supply_center, nation.territories))) == most_supply_centers:
						game_rankings[nation.name] = rank
						temp_nations.remove(nation)
						rank += 1

			# Save pertinent game data.
			if selected_nation != None and winner.name == selected_nation:
				for action in turn_one_actions:
					if action in watched_actions:
						watched_actions[action] += 1
						continue
					watched_actions[action] = 1

			if winner.name in nation_wins:
				nation_wins[winner.name] += 1
			else:
				nation_wins[winner.name] = 1

			if winner.name in nation_win_turns:
				nation_win_turns[winner.name] += __main__.active_board.turn_number
			else:
				nation_win_turns[winner.name] = __main__.active_board.turn_number

			total_turns += __main__.active_board.turn_number

			for nation in __main__.active_board.nations:
				if nation.name in rank_total:
					rank_total[nation.name] += game_rankings[nation.name]
					continue
				rank_total[nation.name] = game_rankings[nation.name]

			if not winner.name in fastest_win or __main__.active_board.turn_number < fastest_win[winner.name]:
				fastest_win[winner.name] = __main__.active_board.turn_number

			# End of game.

		# Update progress bar.
		print_progress_bar(j + 1, batches, prefix='Simulation:', suffix='Complete', length=50)

		# End of batch.

	# Print nation-specific output.
	if selected_nation != None:
		output = [['Action', 'Winrate']]
		for action in watched_actions:
			output.append([action, '{0:.1f}'.format(100 * (watched_actions[action] / float(nation_wins[selected_nation]))) + '%'])
		__main__.print_columns(output)

	# Print generic output.
	output = [['Nation', 'Placement', 'Average Win', 'Fastest Win', 'Winrate']]
	for nation in nation_wins:
		output.append([nation, '{0:.2f}'.format(rank_total[nation] / float(iterations)), '{0:.1f}'.format(nation_win_turns[nation] / float(nation_wins[nation])), str(fastest_win[nation]), '{0:.1f}'.format(100 * (nation_wins[nation] / float(iterations))) + '%'])
	__main__.print_columns(output)

	return 'Iteration complete. ' + str(iterations) + ' games, ' + str(total_turns) + ' turns.'

	# End of execute()

# Credit to Benjamin Cordier.
def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
	if iteration == total: 
		print()

class Action:
	def __init__(self, unit, action_name, target_identifier):
		self.unit = unit
		self.action_name = action_name
		self.target_identifier = target_identifier

	def resolve(self):
		if self.action_name == 'hold':
			return self.unit.name + ' hold'
		elif self.action_name == 'move':
			target = __main__.active_board.loadables[self.target_identifier]
			if not set(target.units).isdisjoint(self.unit.owner.units):
				# Support instead.
				for unit in target.units:
					if unit.owner == self.unit.owner:
						unit.power += 1
						self.unit.power -= 1
						return self.unit.name + ' -S- ' + unit.name
			else:
				# Actually move.
				self.unit.set_location(target)
				return self.unit.old_name + ' -> ' + self.unit.location.name
		elif self.action_name == 'convoy':
			target = __main__.active_board.loadables[self.target_identifier]
			target.convoys.append(self.unit)
			return self.unit.name + ' -C- ' + target.name
