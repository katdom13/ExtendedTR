from functools import wraps

from .constants import DIRECTIONS
from .exceptions import CollisionError, InvalidPosition


def has_table(f):
    @wraps(f)
    def wrapper(cls, *args, **kwargs):
        if not cls.table:
            return
        return f(cls, *args, **kwargs)

    return wrapper


class Position(object):
    table = None

    def __init__(self, x, y, direction):
        if direction in DIRECTIONS and self.table and 0 <= x < self.table.x and 0 <= y < self.table.y:
            if self.table.has_content(x, y):
                raise CollisionError
            self.x = x
            self.y = y
            self.direction = direction
        else:
            raise InvalidPosition

    @classmethod
    def set_table(cls, table):
        cls.table = table

    @classmethod
    def set_position(cls, data):
        x, y, direction = data.values()
        return Position(x, y, direction)

    @has_table
    def get_position(self):
        return dict(x=self.x, y=self.y, direction=self.direction)

    def __repr__(self):
        return f"{self.x},{self.y},{self.direction}"
