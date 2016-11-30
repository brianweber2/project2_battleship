from battleship import clear_screen
from player import Player
from board import Board
from ship import Ship


class Game:
	'''
	Decides what to do

	Decides whos turn it is (holds onto Player objects) switches between them.
	Decides if the game is over.
	Decides who won.
	'''
	def setup(self):
		clear_screen()
		self.player1 = Player(input("Player 1's name: "))
		self.player2 = Player(input("Player 2's name: "))
		self.ship1 = Ship()
		self.ship2 = Ship()


	def __init__(self):
		# Prompt the players for their names
		self.setup()		
		# Prompt user to place a ship and validate user input
		self.player1.prompt_user_to_place_ship()




Game()