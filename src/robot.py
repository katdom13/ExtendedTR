from functools import wraps

from .constants import DIR_STATE
from .exceptions import CollisionError, InvalidPosition
from .position import Position


def has_position(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if not self.position:
            return
        return f(self, *args, **kwargs)

    return wrapper


class Robot(object):
    id = None
    position = None

    def __init__(self, id=None, position=None):
        self.id = id
        self.position = position

        if self.position:
            x, y = self.position.x, self.position.y
            self.position.table.place(self, x, y)

    def place(self, position):
        try:
            if self.position:
                old_x, old_y = self.position.x, self.position.y
                self.position.table.remove(old_x, old_y)

            self.position = Position.set_position(position)

            x, y = self.position.x, self.position.y
            self.position.table.place(self, x, y)
        except InvalidPosition:
            pass

    @has_position
    def move(self):
        old_x, old_y = self.position.x, self.position.y
        position = self.position.get_position()

        try:
            direction = position["direction"]
            if direction == "NORTH":
                position["y"] += 1
            elif direction == "SOUTH":
                position["y"] -= 1
            elif direction == "EAST":
                position["x"] += 1
            elif direction == "WEST":
                position["x"] -= 1

            self.position = Position.set_position(position)

            self.position.table.remove(old_x, old_y)
            x, y = self.position.x, self.position.y
            self.position.table.place(self, x, y)
        except (InvalidPosition, CollisionError):
            pass

    @has_position
    def __rotate(self, direction):
        position = self.position.get_position()
        try:
            position["direction"] = DIR_STATE[position["direction"]][direction]
            self.position.direction = position["direction"]
        except (KeyError):
            pass

    def left(self):
        self.__rotate("LEFT")

    def right(self):
        self.__rotate("RIGHT")

    @has_position
    def report(self):
        print(self.position)
