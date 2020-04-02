from data.classes.board import Board

class DiplomatLoadable:
	load_from_query_identifier = None

	def __init__(self, board, identifier):
		if not isinstance(board, Board):
			raise TypeError('board must be a Board.')
		if not isinstance(identifier, str):
			raise TypeError('identifier must be a string.')

		self.board = board
		self.identifier = identifier
		self.initialized = False

	def init_relationships(self):
		self.initialized = True

	def __str__(self):
		return self.board + ': ' + self.identifier

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
