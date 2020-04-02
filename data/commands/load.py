import __main__
import os.path
from glob import glob

name = 'load'
usage = 'LOAD (Map name)'
description = 'Load a map.'
def execute(query):
	if len(query) < 1:
		return usage

	# Find map file.
	map_file_name = __main__.maps_path.replace('*', query[0])
	if not os.path.isfile(map_file_name):
		return 'Unknown map \'' + map_file_name + '\'.'

	# Build map.
	__main__.active_board = __main__.classes['Board'](query[0])
	with open(map_file_name, 'r') as file:
		for line in file:
			line_query = line.split()
			if len(line_query) < 1 or line_query[0] == '#':
				continue
			if len(line_query) < 2:
				return 'line_query must have at least two parts unless it is empty or marked as a comment with a pound (#).'
			identifier = line_query.pop(0)
			query_type = line_query.pop(0)

			if identifier in __main__.active_board.loadables:
				return 'Diplicate identifier [' + identifier + '].'

			if not query_type in __main__.loadable_classes:
				return 'Unknown query_type [' + query_type + '] on line [' + identifier + '].'

			try:
				__main__.active_board.loadables[identifier] = __main__.loadable_classes[query_type].load_from_query(__main__.active_board, identifier, line_query)
			except Exception as error:
				return 'Error loading component on line [' + identifier + ']: ' + str(error)

	for loadable in __main__.active_board.loadables:
		try:
			if not __main__.active_board.loadables[loadable].initialized:
				__main__.active_board.loadables[loadable].init_relationships()
		except Exception as error:
			return 'Error initializing relationships on line [' + loadable + ']: ' + str(error)

	return 'Loaded map with ' + str(len(__main__.active_board.loadables)) + ' components.'
