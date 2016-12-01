from constants import VERTICAL_SHIP, HORIZONTAL_SHIP


class Ship:
    """
    Ship with name, size, coordinates, and hits.

    Args:
        name (str): Name of the ship
        size (int): ship size in board spaces
        coords (list[str]): list of ship board coords
        direction (str): ship direction vertical or horizontal

    Attributes:
        hits (list[str]): coords "hit" by guess
        sunk (boolean): all coords "hit"
        char (str): display charater "|" vertical or "-" horizontal
    """


    def __init__(self, name, size, coords, orientation):
        """
        Initialize Ship with name, size, coordinates and direction.
        """
        self.name = name
        self.size = size
        self.coords = coords
        self.orientation = orientation
        # List[str]: coordinates of ship that has been "hit"
        self.hits = []
        # Boolean: Has this ship sunk (all coords as "hit")
        self.sunk = False
        # str: display character
        if orientation.lower() == 'v':
            self.char = VERTICAL_SHIP
        else:
            self.char = HORIZONTAL_SHIP


    def hit(self, coord):
        pass
