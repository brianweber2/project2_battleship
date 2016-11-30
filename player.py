from battleship import clear_screen, SHIP_INFO, BOARD_SIZE
from board import Board


class Player(Board):
	'''
	Does the following to set the player's data:

	1. Prompt the players for their names
	2. Prompt user to place a ship
	'''
	def __init__(self, name):
		Board.__init__(self)
		self.name = name


	def __str__(self):
		return "{}".format(self.name)


	def prompt_user_to_place_ship(self):
		self.user_choices = {}
		for ship in SHIP_INFO:
			clear_screen()
			self.print_board(self.board)
			print("{} choose ship locations".format(self.name))
			# Validate user input
			try:
				self.user_choices[ship[0]] = (input("Place the location of the"
				" {} ({} spaces): ".format(*ship))).upper().strip()
				if set('[~!@#$%^&*()_+{}":;\']+$').intersection(
					self.user_choices[ship[0]]) or (self.user_choices[ship[0]] not
					in [key for row in self.board for key in row]):
					raise ValueError	
			except:
				clear_screen()
				print("Error! {} is not a valid input. Make sure you only use "
					"lower or uppercase characters for columns and a number "
					"1-{} for rows. Spaces are allowed.".format(
						self.user_choices[ship[0]], BOARD_SIZE)
					)
				self.print_board(self.board)
				self.user_choices[ship[0]] = (input("Place the location of the"
				" {} ({} spaces): ".format(*ship))).upper().strip()

			if input("Is it horizontal? (Y)/N: ").lower() != 'y':
				self.user_choices[ship[0] + "_horizontal?"] = 'n'
			# Place ship on board
			self.place_ship(ship[0], self.user_choices[ship[0]], ship[1], 
							self.user_choices[ship[0] + "_horizontal?"])
			


