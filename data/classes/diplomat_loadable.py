from data.classes.board import Board

class DiplomatLoadable:
	load_from_query_identifier = None

	def __init__(self, board):
		if not isinstance(board, Board):
			raise TypeError('board must be a Board.')

		self.board = board

	def init_relationships(self):
		raise NotImplementedError('DiplomatLoadable children must implement init_relationships().')

	def load_from_query(self, query):
		if not isinstance(query, list):
			raise TypeError('query must be a list.')
