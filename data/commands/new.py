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

		map_file_name = __main__.maps_path.replace('*', query[1])

		if not os.path.isfile(map_file_name):
			return 'Unknown map \'' + map_file_name + '\'.'
		
		return 'Map found.' # TODO - Load map.
		__main__.active_board = Board()
	elif new_type == 'territory':
		pass
	elif new_type == 'nation':
		pass
	elif new_type == 'unit':
		pass
	else:
		return
