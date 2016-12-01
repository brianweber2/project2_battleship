"""Constants used across Battleship project.

Project 2 of Treehouse Techdegree - Python Web Development
"""


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

BOARD_HEADING = ("   " + " ".join(
    [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'