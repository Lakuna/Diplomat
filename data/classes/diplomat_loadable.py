from data.classes.diplomat_viewable import DiplomatViewable
from data.classes.board import Board

class DiplomatLoadable(DiplomatViewable):
	load_from_query_identifier = None

	def __init__(self, board, identifier, names):
		super().__init__(names)

		if not isinstance(board, Board):
			raise TypeError('board must be a Board.')
		if not isinstance(identifier, str):
			raise TypeError('identifier must be a string.')

		self.board = board
		self.identifier = identifier
		self.initialized = False

	def init_relationships(self):
		self.initialized = True

	@staticmethod
	def load_from_query(board, identifier, query):
		if not isinstance(board, Board):
			raise TypeError('board must be a Board.')
		if not isinstance(identifier, str):
			raise TypeError('identifier must be a string.')
		if not isinstance(query, list):
			raise TypeError('query must be a list.')
		for part in query:
			if not isinstance(part, str):
				raise TypeError('query must contain only strings.')
