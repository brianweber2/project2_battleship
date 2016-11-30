from battleship import clear_screen


class Board:
    '''
    Everything to do with reporting info back to the game

    Can validate a move
    Can move/set game pieces when told to
    Can return new "updated" version of itself to Game
    '''
    BOARD_SIZE = 10

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'


    def __init__(self):
        self.board = [[self.EMPTY for n in range(self.BOARD_SIZE)] for n in range(self.BOARD_SIZE)]
        self.board_size = self.BOARD_SIZE


    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]))


    def print_board(self):
        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1


    def place_ship(self, ship, location, size, orientation):
        """
        Place ship on board. Ship is a string, location is "A5" and size is length
        """
        letter, num = list(location)


    def update_board(self, board):
    	pass


