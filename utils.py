"""
Utility functions for the Battleship project.

Project 2 of Treehouse Techdegree - Python Web Development
"""

import os

from constants import (BOARD_SIZE, VERTICAL_SHIP, HORIZONTAL_SHIP, EMPTY,
                       MISS, HIT, SUNK)


def clear_screen():
    """Clear screen by sending command to OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_legend():
    """Print legend of board symbols."""
    print("Legend: Ships {} or {}, Empty {}, Miss {}, Hit {}, Sunk {}\n"
          "".format(VERTICAL_SHIP, HORIZONTAL_SHIP, EMPTY, MISS, HIT, SUNK))


def validate_coord(coord, board_size=BOARD_SIZE):
    """Verify that the coordinate is within the board limits."""
    if len(coord) != 2:
        # Length of coordinate from player must equal 2.
        return False
    # Attempt to convert between characters and numbers for letter part.
    # Check to make sure the row number is in fact an integer.
    try:
        ship_row = int(coord[1])
        ship_col = ord(coord[0])
    except (ValueError, TypeError):
        return False
    # Check to make sure coordinate is on the board.
    return (ship_row >= 1 and ship_row <= board_size and 
            ship_col >= ord('A') and ship_col <= ord('A') + board_size - 1)