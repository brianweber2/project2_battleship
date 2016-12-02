from constants import (BOARD_SIZE, VERTICAL_SHIP, HORIZONTAL_SHIP, EMPTY,
                       MISS, HIT, SUNK, SHIP_INFO)
from utils import clear_screen

from player import Player
from ship import Ship


class Game(object):
    """
    Decides what to do.
    """
    def setup(self):
        clear_screen()
        # Ask for player's name
        name1 = self.ask_player_name(1)
        name2 = self.ask_player_name(2)
        self.player1 = Player(name1)
        self.player2 = Player(name2)

        input("\nNow we will add your ships. {} goes first while {} cannot"
          " see the monitor.\n\nPress ENTER to continue..."
          "".format(name1, name2))

        ##### PLACING SHIPS #####
        # Define player1's ships and locations
        self.define_player_ships(self.player1)
        # Define player2's ships and locations
        input("It is now {}'s turn to add their ships. Press ENTER to continue..."
        "".format(name2))
        self.define_player_ships(self.player2)


    def __init__(self):
        """Game Play"""
        self.setup()
        player1 = self.player1
        player2 = self.player2
        input("Time to begin the game! {} will go first. Press ENTER to continue..."
        "".format(player1.name))
        winner_declared = False
        while not winner_declared:
            self.take_turn(player1, player2)
            if not player2.ships_left():
                print("{} wins!!!\n".format(player1.name))
                player_view = player1.board.get_opp_view(player1.ships)
                opp_view = player2.board.get_opp_view(player2.ships)
                # Print both boards with name labels
                self.print_all_boards(player1, player2, player_view, opp_view)
                winner_declared = True
                break
            self.take_turn(player2, player1)
            if not player1.ships_left():
                print("{} wins!!!".format(player2.name))
                player_view = player2.board.get_opp_view(player2.ships)
                opp_view = player1.board.get_opp_view(player1.ships)
                # Print both boards with name labels
                self.print_all_boards(player2, player1, player_view, opp_view)
                winner_declared = True
                break


    def ask_player_name(self, order):
        """Ask for player's name."""
        name = None
        # Get the player's name
        while not name:
            name = input("Enter the name of Player {}: ".format(order)).strip()
            if not name:
                print("Empty name is not allowed!")
        print("Thanks {}!".format(name))
        return name


    def print_board(self, player_name, player_view):
        """Print a player's board.
     
        player_name (str): name of current player
        player_view (list[str]): list of strings representing board view
        """
        print("\n{}'s board:\n".format(player_name))
        for line in player_view:
            print(" {}".format(line))
        self.print_legend()


    def print_legend(self):
        """Print legend of board symbols."""
        print("\nLegend: Ships {} or {}, Empty {}, Miss {}, Hit {}, Sunk {}\n"
              "".format(VERTICAL_SHIP, HORIZONTAL_SHIP, EMPTY, MISS, HIT, SUNK))


    def validate_coord(self, coord, board_size=BOARD_SIZE):
        """Verify that the coordinate is within the board limits."""
        if len(coord) < 2:
            # Length of coordinate from player must be greater than 2.
            return False
        # Attempt to convert between characters and numbers for letter part.
        # Check to make sure the row number is in fact an integer.
        try:
            ship_row = int(coord[1:])
            ship_col = ord(coord[0])
        except (ValueError, TypeError):
            return False
        # Check to make sure coordinate is on the board.
        return (ship_row >= 1 and ship_row <= board_size and 
                ship_col >= ord('A') and ship_col <= ord('A') + board_size - 1)


    def get_orientation(self, ship_name):
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


    def get_ship_starting_coord(self, player, ship_name, ship_size):
        """Ask player for ship starting coordinate."""
        while True:
            user_input = input("Enter the upper-most or left-most ship position "
                "(i.e. A2): ").strip()
            starting_coord = user_input.upper()
            # Validate coordinate
            if self.validate_coord(starting_coord):
                return starting_coord
            else:
                clear_screen()
                print("Coordinate {} is not on the board. Please enter the LETTER "
                    "and NUMBER as one word. Spaces before or after input, and both"
                    " upper and lowercase characters are allowed."
                    "\n".format(user_input))
                self.print_board(player.name, player.board.get_player_board())
                # Display info for the ship that is being placed
                print("Choose {} location ({} spaces): \n".format(
                    ship_name, ship_size))


    def create_ship_coords(self, starting_coord, ship_size, orientation):
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
            coords = [chr(n) + str(ship_row) for n in range(
                ship_col, ship_col + ship_size)]
        else: # Ship coordinates for vertical orientation
            coords = [chr(ship_col) + str(n) for n in range(
                ship_row, ship_row + ship_size)]
        # Validate that the ship's bow and stern are located on the board
        if self.validate_coord(coords[0]) and self.validate_coord(coords[-1]):
            return coords
        else:
            print("\nERROR: Not all coordinates are on the board!")
            print("Here are the calculated coordinates: {}\n".format(coords))
            return []


    def define_player_ships(self, player):
        """Define player's ships and location on the game board."""
        for ship in SHIP_INFO:
            clear_screen()
            ship_name = ship[0]
            ship_size = ship[1]
            print("Placing ships for {}...\n".format(player.name))
            # Display board
            self.print_board(player.name, player.board.get_player_board())
            # Display info for the ship that is being placed
            print("Choose {} location ({} spaces): \n".format(ship_name, ship_size))

            # Grab ship placement information
            while True:
                # Ask player for starting coordinate
                starting_coord = self.get_ship_starting_coord(player, ship_name, ship_size)
                # Ask player for the ship's orientation
                orientation = self.get_orientation(ship_name)
                # Validate ship placement and generate ship coordinates
                coords = self.create_ship_coords(starting_coord, ship_size, orientation)
                if not coords:
                    continue
                # Validate that this ship does not collide with another one already
                # on the board
                if not player.board.verify_no_ship_collision(coords):
                    print("\nERROR: Ship coordinates collide with other ships! "
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


    def take_turn(self, player, opponent):
        """Allow the player to take a turn guessing the opponent's ship locations."""
        clear_screen()
        input("It is {}'s turn. Press ENTER to continue...".format(player.name))

        # Print board that shows where current player has guessed so far.
        clear_screen()
        print("{}'s turn: ".format(player.name))
        player_view = opponent.board.get_player_view(opponent.ships)
        opp_view = player.board.get_opp_view(player.ships)

        # Print both boards with name labels
        self.print_all_boards(player, opponent, player_view, opp_view)

        # Prompt player for guess and remember guess
        coord = self.get_player_guess(player, opponent)
        player.guesses.append(coord)

        # Check the guess against the opponent's board
        result = opponent.board.guess(coord, opponent.ships)
        # Update opponent's board for player's view
        clear_screen()
        print(result)
        input("\nHit ENTER to continue...\n")
        clear_screen()


    def print_all_boards(self, player, opponent, player_view, opp_view):
        """
        Display player and opponent boards to screen that shows current state
        of game.
        """
        print("\n{}'s board (current player)\n".format(player.name))
        for line in player_view:
            print(" {}".format(line))
        print("\n{}'s board (your opponent)\n".format(opponent.name))
        for line in opp_view:
            print(" {}".format(line))
        self.print_legend()


    def get_player_guess(self, player, opponent):
        """Prompt player for guess."""
        while True:
            user_input = input("\n{}, enter a location: ".format(player.name)).strip()
            guess = user_input.upper()
            # Validate guess
            if guess in player.guesses:
                clear_screen()
                print("\nERROR: {} has already been guessed! Please try again."
                    "".format(guess))
                print("Here are the guesses you have made so far: " + 
                    ", ".join(player.guesses))
                player_view = opponent.board.get_player_view(opponent.ships)
                opp_view = player.board.get_opp_view(player.ships)
                # Print both boards with name labels
                self.print_all_boards(player, opponent, player_view, opp_view)
            elif self.validate_coord(guess):
                return guess
            else:
                clear_screen()
                print("\nERROR: {} is not a valid guess. Please enter the LETTER"
                    " and NUMBER as one word. Spaces before or after input, and "
                    "both upper and lowercase characters are allowed.".format(
                        guess))
                player_view = opponent.board.get_player_view(opponent.ships)
                opp_view = player.board.get_opp_view(player.ships)

                # Print both boards with name labels
                self.print_all_boards(player, opponent, player_view, opp_view)
