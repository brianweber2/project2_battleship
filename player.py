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


    def add_ship(self, ship):
        """Adds ship to list on player's instance."""
        self.ships.append(ship)


