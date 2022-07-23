from re import X, compile

from .exceptions import InvalidCommand


def parse(line):
    line = line.strip()

    PATTERN = compile(
        r"""
            (?<=^)
            (?P<cmd>TABLE
            (?=\s?
            (?P<table_x>\d+)x
            (?P<table_y>\d+)
            $)|
            ROBOTS
            (?=\s?
            (?P<num>\d+)
            $)|
            (MOVE|LEFT|RIGHT|REPORT)
            (?=\s?
            (?P<id>\d+)
            $)?|
            PLACE
            (?=\s?
            (?P<x>\d+),
            (?P<y>\d+),
            (?P<dir>NORTH|EAST|SOUTH|WEST)
            $))
        """,
        X,
    )

    instruction = PATTERN.match(line)
    if not instruction:
        raise InvalidCommand

    return instruction
