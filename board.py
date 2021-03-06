from constants import (BOARD_HEADING, BOARD_SIZE, VERTICAL_SHIP, 
                       HORIZONTAL_SHIP, EMPTY, MISS, HIT, SUNK)

from utils import coord_to_number


class Board(object):
    """
    Battleship Board

    Args:
        size (int): size of square board

    Atrributes:
        board (list[list['O']]): square array with EMPTY string
    """


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


    def verify_no_ship_collision(self, coords):
        """
        Verify that there are no ships already where the new ship is being 
        placed.
        """
        answer = True
        for coord in coords:
            row, col = coord_to_number(coord)
            # Check ship location against ships already on board
            if (self.board[row][col] == HORIZONTAL_SHIP or 
                self.board[row][col] == VERTICAL_SHIP):
                answer = False
        return answer


    def get_player_view(self, ships):
        """
        Get the opponent's board that shows where the current player has 
        guessed so far with SUNK, HIT and EMPTY characters displayed.
        """
        for ship in ships:
            for coord in ship.coords:
                row, col = coord_to_number(coord)
                if ship.sunk:
                    self.board[row][col] = SUNK
                elif coord in ship.hits:
                    self.board[row][col] = HIT
                else:
                    self.board[row][col] = EMPTY
            for coord in ship.misses:
                row, col = coord_to_number(coord)
                self.board[row][col] = MISS

        view = [BOARD_HEADING]
        row_num = 1
        for row in self.board:
            view.append((str(row_num).rjust(2) + " " + " ".join(row)))
            row_num += 1
        return view


    def get_opp_view(self, ships):
        """
        Get the player's board that shows where the opponent has guessed on the
        so far with SUNK, HIT, MISS, EMPTY and ship characters. Make sure to 
        show where the ships are located.
        """
        for ship in ships:
            for coord in ship.coords:
                row, col = coord_to_number(coord)
                if ship.sunk:
                    self.board[row][col] = SUNK
                elif coord in ship.hits:
                    self.board[row][col] = HIT
                else:
                    self.board[row][col] = ship.char
            for coord in ship.misses:
                row, col = coord_to_number(coord)
                self.board[row][col] = MISS

        view = [BOARD_HEADING]
        row_num = 1
        for row in self.board:
            view.append((str(row_num).rjust(2) + " " + " ".join(row)))
            row_num += 1
        return view


    def guess(self, coord, ships):
        """Apply guess to board."""
        for ship in ships:
            if coord in ship.coords:
                ship.hits.append(coord)
                if len(ship.hits) == ship.size:
                    ship.sunk = True
                    result = "Guess [{}]: you SUNK my {}!!\n".format(
                        coord, ship.name)
                    break
                else:
                    result = "Guess [{}]: it's a HIT!\n".format(coord)
                    break
            else:
                ship.misses.append(coord)
                result = "Guess [{}]: you MISSED!\n".format(coord)
        return result