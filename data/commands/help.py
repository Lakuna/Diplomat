import importlib.util
import __main__

name = 'help'
usage = 'HELP [Command]'
description = 'Displays information about commands.'
def execute(query):
	if len(query) > 0:
		if query[0] in __main__.commands:
			command = __main__.commands[query[0]]
			return command.usage + '\t\t' + command.description

	output = [['Syntax', 'Description']]
	for command in __main__.commands.values():
		output.append([command.usage, command.description])
	__main__.print_columns(output)

	return '\nKey: LITERAL [Optional] (Required)'
