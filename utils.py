"""Utility functions used across Battleship project.

Project 2 of Treehouse Techdegree - Python Web Development
"""
import os


def clear_screen():
    """Clear screen by sending command to OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def coord_to_number(coord):
    """Converts the string version of a ship coordinate, i.e. 'A2', to a number
    for a row and column. Note the conversion is based on a 0-based row and 
    column offset.
    """
    row = int(coord[1:]) - 1
    col = ord(coord[0]) - ord('A')
    return row, col