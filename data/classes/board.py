from data.classes.diplomat_viewable import DiplomatViewable

class Board(DiplomatViewable):
	def __init__(self, name):
		names = [name]

		super().__init__(names)

		self.loadables = {}
		self.nations = []
		self.places = []
		self.units = []
		self.turn_number = 1

	def view_string(self):
		return_string = str(self) + ':\nLoadables: ' + str(len(self.loadables)) + '\nNations:'
		for nation in self.nations:
			return_string += ',\t' + str(nation)
		return_string += '\nPlaces:'
		for place in self.places:
			return_string += ',\t' + str(place)
		return_string += '\nUnits:'
		for unit in self.units:
			return_string += ',\t' + str(unit)
		return return_string
