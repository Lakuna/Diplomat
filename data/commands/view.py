import __main__

name = 'view'
usage = 'VIEW (MAP | identifier | name)'
description = 'View a component of the active map.'
def execute(query):
	if len(query) < 1:
		return usage

	if __main__.active_board == None:
		return 'No active map.'

	if query[0] == 'map':
		return __main__.active_board.view_string()

	for component in  __main__.active_board.loadables.values():
		if query[0] in component.names or component.identifier == query[0]:
			return component.view_string()

	return '\'' + query[0] + '\' not found in loadables.'
