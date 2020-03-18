import importlib.util
import __main__

name = 'help'
usage = 'HELP [Command]'
description = 'Displays information about commands.'
def execute(query):
	if len(query) > 1:
		if query[1] in __main__.commands:
			command = __main__.commands[query[1]]
			return command.usage + '\t\t' + command.description

	output = 'List of Commands\nKey: LITERAL [Optional] (Required)'
	for command in __main__.commands.values():
		output += '\n' + command.usage + '\t\t' + command.description
	return output
