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

	for i in range(iterations):
		iterations -= 1;

		for unit in list(filter(lambda component: isinstance(component, __main__.classes['Unit']), __main__.active_board.loadables.values())):
			available_actions = []
			pass # TODO: Discover unit actions.

		pass # TODO: Resolve unit actions. Convoy -> Move & Support. Save actions and winrates into dictionary here.
			
	return 'Iterations complete.' # TODO: Output.
