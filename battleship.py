"""
Author: Brian Weber
Date Created: November 30, 2016
Revision: 1.0
Title: Battleship Console-based Game
Description: In this project you will implement a console-based version of the
popular battleship game. The game will be playable by two players by passing a
laptop back and forth.
"""


from constants import SHIP_INFO
from utils import clear_screen, print_legend, validate_coord
from player import Player
from ship import Ship


def ask_player_name(order):
    """Ask for player's name."""
    name = None
    # get player's name
    while not name:
        name = input("Enter the name of Player {}: ".format(order)).strip()
        if not name:
            print("Empty name is not allowed!")
    print("Thanks {}!".format(name))
    return name


def print_board(player_name, player_view):
    """Print a player's board.
 
    player_name (str): name of current player
    player_view (list[str]): list of strings representing board view
    """
    print("\n{}'s board:\n".format(player_name))
    for line in player_view:
        print(" {}".format(line))
    print_legend() # Print legend for board; from utils.py


def create_ship_coords(starting_coord, ship_size, orientation):
    """Create ship coordinates based on starting position.
    
    To simplify things, the ship coordinates starts at the starting_coord and
    runs down for vertical orientation and to the right for horizontal 
    orientation.

    starting_coord (str): two character board coordinate, i.e. "D7"
    ship_size (int): length of ship in board spaces
    orientation (str): either 'v' for vertical or 'h' for horizontal
    """
    # Convert starting coord to integer for both row and column
    ship_row = int(starting_coord[1:])
    ship_col = ord(starting_coord[0])
    # If orientation is horizontal, calculate ship coordinates
    if orientation == 'h':
        coords = [chr(n) + str(ship_row) for n in range(ship_col, ship_col + ship_size)]
    else: # Ship coordinates for vertical orientation
        coords = [chr(ship_col) + str(n) for n in range(ship_row, ship_row + ship_size)]
    # Validate that the ship's bow and stern are located on the board
    if validate_coord(coords[0]) and validate_coord(coords[-1]):
        return coords
    else:
        print("ERROR: Not all coordinates are on the board!")
        print("Here are the calculated coordinates: {}".format(coords))
        return []


def define_player_ships(player):
    """Define player's ships and location on the game board."""
    for ship in SHIP_INFO:
        clear_screen()
        ship_name = ship[0]
        ship_size = ship[1]
        print("Placing ships for {}...\n".format(player.name))
        # Display board
        print_board(player.name, player.board.get_player_board())
        # Display info for the ship that is being placed
        print("Choose {} location ({} spaces): \n".format(ship_name, ship_size))

        # Grab ship placement information
        while True:
            # Ask player for starting coordinate
            starting_coord = get_ship_starting_coord(player, ship_name, ship_size)
            # Ask player for the ship's orientation
            orientation = get_orientation(ship_name)
            # Validate ship placement and generate ship coordinates
            coords = create_ship_coords(starting_coord, ship_size, orientation)
            if not coords:
                print("ERROR: Ship coordinates not all on the board!")
                continue
            # Validate that this ship does not collide with another one already
            # on the board
            if not player.board.verify_no_ship_collision(coords):
                print("ERROR: Ship coordinates collide with other ships! "
                      "Please try again.\n")
                continue
            # If code reaches here then the ship placement is valid
            break
        # Create ship
        ship = Ship(ship_name, ship_size, coords, orientation)
        # Add the ship to the player instance
        player.add_ship(ship)
        # Put ship on board
        player.board.place_ship(ship)
    clear_screen()
    input("All ships placed have been placed for {}. Hit any key to continue..."
        "".format(player.name))
    clear_screen()


def get_orientation(ship_name):
    """Ask player if ship is vertically or horizontally placed on the board."""
    while True:
        user_input = input("Does the {} run [H]orizontal or [V]ertical? "
            "".format(ship_name)).strip()
        if not user_input:
            print("\nERROR: nothing was entered! You must type 'h' or 'v'!\n")
            continue
        orientation = user_input.lower()
        if orientation == 'h' or orientation == 'v':
            return orientation
        else:
            print("\nERROR: you typed {}. This is not valid. Enter 'h' or 'v'!"
                "\n".format(user_input))


def get_ship_starting_coord(player, ship_name, ship_size):
    """Ask player for ship starting coordinate."""
    while True:
        user_input = input("Enter the upper-most or left-most ship position "
            "(i.e. A2): ").strip()
        starting_coord = user_input.upper()
        # Validate coordinate
        if validate_coord(starting_coord):
            return starting_coord
        else:
            clear_screen()
            print("Coordinate {} is not on the board. Please enter the LETTER "
                "and NUMBER as one word. Spaces before or after input, and both"
                " upper and lowercase characters are allowed."
                "\n".format(user_input))
            print_board(player.name, player.board.get_player_board())
            # Display info for the ship that is being placed
            print("Choose {} location ({} spaces): \n".format(ship_name, ship_size))


def main():
    """Runs the Battleship game."""
    clear_screen()

    # Ask for player's names
    name1 = ask_player_name(1)
    name2 = ask_player_name(2)
    # Instantiate player instances
    player1 = Player(name1)
    player2 = Player(name2)

    input("\nNow we will add your ships. {} goes first while {} cannot"
          " see the monitor.\n\nPress any key to continue".format(name1, name2))

    ##### PLACING SHIPS #####
    # Define player1's ships and locations
    define_player_ships(player1)
    # Define player2's ships and locations
    define_player_ships(player2)



if __name__ == '__main__':
    main()