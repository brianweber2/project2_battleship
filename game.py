from battleship import clear_screen
from player import Player


class Game:
    '''
    Decides what to do

    Decides whos turn it is (holds onto Player objects) switches between them.
    Decides if the game is over.
    Decides who won.
    '''
    def setup(self):
        clear_screen()
        self.player1 = Player(input("Player 1's name: "))
        self.player2 = Player(input("Player 2's name: "))


    def __init__(self):
        # Prompt the players for their names
        self.setup()
        # Display an empty board for player1
        clear_screen()
        self.player1.print_board()
        # Prompt player1 to place a ship. Validate player1 input and ship placement
        self.player1.prompt_user_to_place_ships(self.player1.ship_info)




Game()