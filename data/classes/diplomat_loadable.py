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

	def init_relationships(self):
		raise NotImplementedError('DiplomatLoadable children must implement init_relationships().')

	@staticmethod
	def load_from_query(board, identifier, query):
		if not isinstance(board, Board):
			raise TypeError('board must be a Board.')
		if not isinstance(identifier, str):
			raise TypeError('identifier must be a string.')
		if not isinstance(query, list):
			raise TypeError('query must be a list.')
