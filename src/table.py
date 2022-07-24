from functools import wraps


def has_table(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if not self.table:
            return
        return f(self, *args, **kwargs)

    return wrapper


class Table(object):
    table = None

    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

        self.table = [[None] * self.y for i in range(self.x)]

    @has_table
    def remove(self, x, y):
        el = self.table[x][y]
        if el:
            self.table[x][y] = None
            return el

    @has_table
    def place(self, obj, x, y):
        self.table[x][y] = obj
        return obj

    @has_table
    def get(self, x, y):
        return self.table[x][y]

    @has_table
    def has_content(self, x, y):
        return bool(self.get(x, y))
