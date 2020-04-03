import __main__

name = 'iterate'
usage = 'ITERATE [Iterations] [Nation]'
description = 'Simulate games of Diplomacy.'
def execute(query):
	if __main__.active_board == None:
		return 'No active map.'

	iterations = 1000
	if len(query) > 0:
		try:
			iterations = int(query.pop(0))
		except:
			pass

	nation = None
	if len(query) > 0:
		for component in __main__.active_board.loadables.values():
			if (query[0] in component.names or component.identifier == query[0]) and isinstance(component, __main__.classes['Nation']):
				nation = component

	# Game loop.
	for i in range(iterations):
		# TODO: Reset map.

		# Turn loop.
		winner = None
		while winner == None:
			# Get available unit actions.
			for unit in list(filter(lambda component: isinstance(component, __main__.classes['Unit']), __main__.active_board.loadables.values())):
				available_actions = []

				# Holding.
				available_actions.append(Action('hold', unit.location.identifier))

				# Moving and supporting.
				for territory in unit.movable_territories():
					available_actions.append(Action('move', territory.identifier))

				# Convoying.
				if not isinstance(unit, __main__.classes['Fleet']):
					continue
				for unit in unit.convoyable_units():
					available_actions.append('convoy', unit.identifier)

			# TODO: Resolve unit actions. Convoy -> Move & Support. Save actions and winrates into dictionary here.

			# TODO: Resolve conflicts.

			# TODO: Update territory ownership on even turns.

			# TODO: Update unit count on even turns.

			# Check for end of game.
			for nation in __main__.active_board.nations.values:
				if len(list(filter(lambda territory: territory.is_supply_center, nation.territories))) >= 20:
					winner = nation
					break

			# End of turn.

		# TODO: Update progress bar.

		# End of game.
			
	return 'Iterations complete.' # TODO: Output.

class Action:
	def __init__(self, action_name, target_identifier):
		self.action_name = action_name
		self.target_identifier = target_identifier

	def resolve(self):
		pass # TODO: Resolve action and return action string.
