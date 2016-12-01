from board import Board


class Player(object):
    """
    Battleship Player

    Args:
        name (str): name of player

    Attributes:
        board (class): board instance belonging to the player
        ships (list[ship_objects]): list of all ship objects
        guesses(list[coord]): list of all guessed coordinates 
    """
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