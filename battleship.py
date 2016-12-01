"""
Puts togther all code to execute board game.

Project 2 of Treehouse Techdegree - Python Web Development
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

    Args: 
        player_name (str): name of current player
        player_view (list[str]): list of strings representing board view
    """
    print("\n{}'s board:\n".format(player_name))
    for line in player_view:
        print(" {}".format(line))
    print_legend()


def create_ship_coords(starting_coord, ship_size, orientation):
    pass


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
        # Ask player for starting coordinate
        starting_coord = get_ship_starting_coord(player, ship_name, ship_size)
        # Ask player for the ship's orientation
        orientation = get_orientation(ship_name)
        # Validate ship placement and generate ship coordinates 



def get_orientation(ship_name):
    """Ask player if ship is vertically or horizontally placed on the board."""
    while True:
        user_input = input("Does the {} run [H]orizontal or [V]ertical? "
            "".format(ship_name)).strip()
        if not user_input:
            print("\nERROR: nothing was entered! You must type 'h' or 'v'!\n")
            continue
        orientation = user_input[0].lower()
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




if __name__ == '__main__':
    main()