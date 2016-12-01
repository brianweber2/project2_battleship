from constants import (BOARD_HEADING, BOARD_SIZE, VERTICAL_SHIP, 
                       HORIZONTAL_SHIP, EMPTY, MISS, HIT, SUNK)


class Board:
    '''
    Battleship Board

    Board is a square array of Locations
    '''


    def __init__(self, size=BOARD_SIZE):
        """
        Initialize board to specified size.
        """
        self.board = [[EMPTY for n in range(size)] for n in range(size)]


    def get_player_board(self):
        """
        Return player view of game board without ships revealed.
        """
        board = [BOARD_HEADING]
        row_num = 1
        for row in self.board:
            board.append((str(row_num).rjust(2) + " " + " ".join(row)))
            row_num += 1
        board.append("")
        return board


    def place_ship(self, size, index, orientation):
        """
        Place ship on board.
        """
        pass


    def guess(self, coord):
        """
        Apply guess to board.
        """
        pass