
class Battlefield:
    def __init__(self):
        self.ShipCollection = []
        self.Missed = []

    def addShip(self,Ship):
        for s in self.ShipCollection:
            if(s.isConflict(Ship)):
                raise ValueError("Ship in the way (%s)" % Ship.getType().getName())
            if(s.getType().getName() == Ship.getType().getName()):
                raise ValueError("Ship Type Already Used (%s)" % s.getType().getName())
        self.ShipCollection.append(Ship)

    def fire(self,coordinate):
        for ship in self.ShipCollection:
            hit = ship.fire(coordinate)
            if(hit):
                return ship
        self.Missed.append(coordinate)
        return None

    def areAllSunk(self):
        for ship in self.ShipCollection:
            if(not ship.isSunk()):
                return False
        return True
