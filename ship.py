class Ship:
    '''
    Everything to do with the ship itself

    Knows how to mark himself or piece of him as a hit.
    Knows how to turn into a destroyed ship.
    Knows how to return his size/dimensions.
    '''
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

    def __init__(self):
        self.ship_info = self.SHIP_INFO


    def return_ship_size(self, ship_name):
        for ship in self.ship_info:
            if ship[0] == ship_name:
                return ship[1]


    def ship_destoyed(self):
        pass


    def hit_or_miss(self):
        pass