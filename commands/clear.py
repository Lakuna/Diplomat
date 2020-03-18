from os import system, name as os_name

name = 'clear'
usage = 'CLEAR'
description = 'Clears the screen.'
def execute(query):
	if os_name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	return 'Cleared the screen.'
