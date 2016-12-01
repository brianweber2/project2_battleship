from constants import (BOARD_HEADING, BOARD_SIZE, VERTICAL_SHIP, 
                       HORIZONTAL_SHIP, EMPTY, MISS, HIT, SUNK)
from utils import coord_to_number


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
        return board


    def place_ship(self, ship):
        """
        Place ship on board.
        """
        for coord in ship.coords:
            row, col = coord_to_number(coord)
            self.board[row][col] = ship.char


    def guess(self, coord):
        """
        Apply guess to board.
        """
        pass


    def verify_no_ship_collision(self, coords):
        """
        Verify that there are no ships already where the new ship is being 
        placed.
        """
        answer = True
        for coord in coords:
            row, col = coord_to_number(coord)
            # Check ship location against ships already on board
            if self.board[row][col] == HORIZONTAL_SHIP or self.board[row][col] == VERTICAL_SHIP:
                answer = False
        return answer