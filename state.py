from constants import EMPTY


class State(object):
	""" 
	Holds onto a single board state and ships.
	
	Args:
		coord (str): board coordinate, i.e. "A2"

	Attributes:
		ship (Ship): the ship in this location
		state (str): holds onto the state of each index in board
	"""


	def __init__(self, coord):
		"""Initialize state of board and ships."""
		self.coord = coord
		self.ship = None
		self.state = EMPTY


	def player_view(self):
		"""Return board state that is seen by the player."""
		if self.ship:
			return self.ship.get_player_state(self.coord)
		else:
			return self.state


	def opp_view(self):
		"""Return board state that is seen by the opponent."""
		if self.ship:
			return self.ship.get_opp_state(self.coord)
		else:
			return self.state