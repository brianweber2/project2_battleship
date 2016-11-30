from battleship import (BOARD_SIZE, VERTICAL_SHIP, HORIZONTAL_SHIP, EMPTY, 
					    MISS, HIT, SUNK)
from collections import OrderedDict


class Board:
    '''
    Everything to do with reporting info back to the game

    Can validate a move
    Can move/set game pieces when told to
    Can return new "updated" version of itself to Game
    '''
    def __init__(self):
        # self.board = [[EMPTY for n in range(BOARD_SIZE)] for n in range(BOARD_SIZE)]
        self.board = [OrderedDict([('A1', EMPTY), ('B1', EMPTY), ('C1', EMPTY),
            ('D1', EMPTY), ('E1', EMPTY), ('F1', EMPTY), ('G1', EMPTY), ('H1',
            EMPTY), ('I1', EMPTY), ('J1', EMPTY)]), OrderedDict([('A2', EMPTY),
            ('B2', EMPTY), ('C2', EMPTY), ('D2', EMPTY), ('E2', EMPTY), ('F2', EMPTY), 
            ('G2', EMPTY), ('H2', EMPTY), ('I2', EMPTY), ('J2', EMPTY)]), 
            OrderedDict([('A3', EMPTY), ('B3', EMPTY), ('C3', EMPTY), ('D3', EMPTY),
            ('E3', EMPTY), ('F3', EMPTY), ('G3', EMPTY), ('H3',	EMPTY), 
            ('I3', EMPTY), ('J3', EMPTY)]), OrderedDict([('A4', EMPTY), 
            ('B4', EMPTY), ('C4', EMPTY), ('D4', EMPTY), ('E4', EMPTY), 
            ('F4', EMPTY), ('G4', EMPTY), ('H4', EMPTY), ('I4', EMPTY), 
            ('J4', EMPTY)]), OrderedDict([('A5', EMPTY), ('B5', EMPTY), 
            ('C5', EMPTY), ('D5', EMPTY), ('E5', EMPTY), ('F5', EMPTY),
            ('G5', EMPTY), ('H5', EMPTY), ('I5', EMPTY), ('J5', EMPTY)]),
            OrderedDict([('A6', EMPTY), ('B6', EMPTY), ('C6', EMPTY), 
            ('D6', EMPTY), ('E6', EMPTY), ('F6', EMPTY), ('G6', EMPTY),
            ('H6', EMPTY), ('I6', EMPTY), ('J6', EMPTY)]), OrderedDict([
            ('A7', EMPTY), ('B7', EMPTY), ('C7', EMPTY), ('D7', EMPTY), 
            ('E7', EMPTY), ('F7', EMPTY), ('G7', EMPTY), ('H7', EMPTY), 
            ('I7', EMPTY), ('J7', EMPTY)]), OrderedDict([('A8', EMPTY), 
            ('B8', EMPTY), ('C8', EMPTY), ('D8', EMPTY), ('E8', EMPTY), 
            ('F8', EMPTY), ('G8', EMPTY), ('H8', EMPTY), ('I8', EMPTY), 
            ('J8', EMPTY)]), OrderedDict([('A9', EMPTY), ('B9', EMPTY),
            ('C9', EMPTY), ('D9', EMPTY), ('E9', EMPTY), ('F9', EMPTY), 
            ('G9', EMPTY), ('H9', EMPTY), ('I9', EMPTY), ('J9', EMPTY)]),
            OrderedDict([('A10', EMPTY), ('B10', EMPTY), ('C10', EMPTY), 
            ('D10', EMPTY), ('E10', EMPTY), ('F10', EMPTY), ('G10', EMPTY), 
            ('H10', EMPTY), ('I10', EMPTY), ('J10', EMPTY)])]


    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


    def print_board(self):
        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(list(row.values()))))
            row_num += 1


    def place_ship(self, ship, location, size, orientation):
        """
        Place ship on board. Ship is a string, location is "A5" and size is length
        """
        letter, num = list(location)


    def update_board(self, board):
    	pass


