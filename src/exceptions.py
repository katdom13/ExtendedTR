class InvalidPosition(Exception):
    """
    Raised when the given position is out of table bounds
    """

    pass


class InvalidCommand(Exception):
    """
    Raised when the given command is invalid
    """

    pass


class CollisionError(Exception):
    """
    Raised when there is a collision on the table
    """

    pass
