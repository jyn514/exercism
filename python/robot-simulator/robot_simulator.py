directions = ["NORTH", "EAST", "SOUTH", "WEST"]

class Robot(object):
    def __init__(self, direction, x, y):
        self.bearing = directions.index(direction)
        self.coordinates = [x, y]
        
    def act(letter):
        if letter == "R":
            self.bearing += 1
        elif letter == "L":
            self.bearing -= 1
        else:
            advance(directions[self.bearing % 4])

    def advance(bearing):
        if bearing == "NORTH":
            self.coordinates[0] += 1
        elif bearing == "SOUTH":
            self.coordinates[0] -= 1
        elif bearing == "EAST":
            self.coordinates[1] += 1
        else:
            self.coordinates[1] -= 1
