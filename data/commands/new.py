import __main__
import os.path
from glob import glob

name = 'new'
usage = 'NEW (MAP/TERRITORY/NATION/UNIT)...'
description = 'Create a new part of the game.'
def execute(query):
	if len(query) < 1:
		return usage

	new_type = query[0]

	if new_type == 'map':
		if len(query) < 2:
			return usage[:-len('...')] + ' (Map name)'

		# Find map file.
		map_file_name = __main__.maps_path.replace('*', query[1])
		if not os.path.isfile(map_file_name):
			return 'Unknown map \'' + map_file_name + '\'.'

		# Build map.
		__main__.active_board = __main__.classes['Board']()
		with open(map_file_name, 'r') as file:
			for line in file:
				query = line.split()
				if len(query) < 2:
					return 'query must contain at least two strings.'
				identifier = query.pop(0)
				query_type = query.pop(0)

				if not query_type in __main__.loadable_classes:
					return 'Unknown query type [' + query_type + '] on line [' + identifier + '].'

				try:
					__main__.active_board.loadables[identifier] = __main__.loadable_classes[query_type].load_from_query(__main__.active_board, identifier, query)
				except Exception as error:
					return 'Error creating new map on line [' + identifier + ']: ', error

		return 'Created new map with ' + str(len(__main__.active_board.loadables)) + ' components.'
	elif new_type == 'territory':
		pass
	elif new_type == 'nation':
		pass
	elif new_type == 'unit':
		pass
	else:
		return
