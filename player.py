from battleship import clear_screen
from board import Board
from ship import Ship


class Player(Board, Ship):
    '''
    Does the following to set the player's data:

    1. Prompt the players for their names
    2. Prompt user to place a ship
    '''
    def __init__(self, name):
        Board.__init__(self)
        Ship.__init__(self)

        self.name = name


    def __str__(self):
        return "{}".format(self.name)


    def prompt_user_to_place_ship(self, ships):
        self.user_choices = {}
        print("{} choose ship locations".format(self.name))
        for ship in ships:
            self.user_choices[ship[0]] = (input("Place the location of the"
            " {} ({} spaces): ".format(*ship))).upper().strip()
            # Validate player input
            self.user_choices[ship[0]] = self.validate_player_input(
                ship, self.user_choices[ship[0]])

            if input("Is it horizontal? (Y)/N: ").lower() != 'y':
                self.user_choices[ship[0] + "_horizontal?"] = 'n'
            else:
                self.user_choices[ship[0] + "_horizontal?"] = 'y'
            # Place ship on board

            # Print updated board with ship location
            # self.update_board()
            clear_screen()
            self.print_board()
            print("{} choose ship locations".format(self.name))
        return self.user_choices


    def validate_player_input(self, ship, player_input):
        """
        Function validates player input for ship location.
        """
        input_validated = False
        while input_validated == False:
            if set('[~!@#$%^&*()_+{}":;\']+$').intersection(
            player_input) or (player_input not in 
            [letter+str(n) for n in range(1,11) for letter in "ABCDEFGHIJ"]):
                clear_screen()
                print("Error! {} is not a valid input. Make sure you only use "
                        "lower or uppercase characters for columns and a number "
                        "1-{} for rows. Spaces are allowed.".format(
                        player_input, self.board_size)
                )
                self.print_board()
                print("{} choose ship locations".format(self.name))
                player_input = (input("Place the location of the"
                " {} ({} spaces): ".format(*ship))).upper().strip()
            else:
                input_validated = True
        return player_input