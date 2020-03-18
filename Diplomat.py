import importlib.util
from pathlib import Path
from glob import glob

# Global values.
diplomat_path = str(Path(__file__).parent.absolute())
maps_path = diplomat_path + '\\maps\\*.diplomap'
commands_path = diplomat_path + '\\commands\\*.py'
help_string = 'Type \'help\' for a list of commands.'

# Load commands.
command_files = glob(commands_path)
commands = {}
for command in command_files:
	spec = importlib.util.spec_from_file_location('', command)
	command = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(command)
	commands[command.name] = command

# Print the help string once at the beginning.
print(help_string)

# Take commands from user.
query = [None]
while query[0] != 'exit':
	query = list(map(lambda word: ''.join(list([character for character in word if character.isalpha() or character.isdigit()])).lower(), input('\n>').split()))

	if len(query) == 0:
		query = [None] # So that the loop doesn't throw an error if the query was empty.

	command = None
	if query[0] in commands:
		command = commands[query[0]]

	if command == None:
		print(help_string)
	else:
		print(command.execute(query))
