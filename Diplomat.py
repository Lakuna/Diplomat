import importlib.util
from pathlib import Path
from glob import glob
import inspect
import os.path

# Global values.
diplomat_path = str(Path(__file__).parent.absolute())
classes_path = diplomat_path + '\\data\\classes\\*.py'
maps_path = diplomat_path + '\\data\\maps\\*.diplomap'
commands_path = diplomat_path + '\\data\\commands\\*.py'
help_string = 'Type \'help\' for a list of commands.'
active_board = None

# Create paths if they don't exist.
for path in (diplomat_path, classes_path, maps_path, commands_path):
	dirname = os.path.dirname(path)
	if not os.path.exists(dirname):
		os.makedirs(dirname)
		print('Created directory: ' + dirname)

# Load commands.
command_files = glob(commands_path)
commands = {}
for command_file in command_files:
	spec = importlib.util.spec_from_file_location('', command_file)
	command_file = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(command_file)
	commands[command_file.name] = command_file

# Load classes.
class_files = glob(classes_path)
classes = {}
loadable_classes = {}
for class_file in class_files:
	spec = importlib.util.spec_from_file_location('', class_file)
	class_file = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(class_file)
	for name, class_object in inspect.getmembers(class_file):
		if not inspect.isclass(class_object):
			continue
		classes[name] = class_object
		if not hasattr(class_object, 'load_from_query_identifier'):
			continue
		if not isinstance(class_object.load_from_query_identifier, str):
			continue
		loadable_classes[class_object.load_from_query_identifier] = class_object

# Print the help string once at the beginning.
print(help_string)

# Take commands from user.
query = [None]
command_name = None
while command_name != 'exit':
	# Get user input.
	query = list(map(lambda word: ''.join(list([character for character in word if character.isalpha() or character.isdigit()])).lower(), input('\n>').split()))
	if len(query) == 0:
		print(help_string)
		continue

	# Get command.
	command_name = query.pop(0)
	command = None
	if command_name in commands:
		command = commands[command_name]
	if command == None:
		print(help_string)
		continue

	# Execute command.
	try:
		print(command.execute(query))
	except Exception as error:
		print('Error executing command: ' + str(error))
