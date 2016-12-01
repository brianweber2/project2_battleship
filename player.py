from board import Board


class Player(object):
    '''
    Does the following to set the player's data:

    1. Prompt the players for their names
    2. Prompt user to place a ship
    '''
    def __init__(self, name):
        """
        Define player's name, board, ships and guesses
        """
        self.name = name
        self.board = Board()
        self.ships = []
        self.guesses = []


    def prompt_user_to_place_ships(self):
        pass


    def validate_player_input(self, ship, player_input):
        """
        Function validates player input for ship location.
        """
        pass