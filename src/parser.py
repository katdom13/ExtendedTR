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

    cmd = instruction.group("cmd")
    table_x = instruction.group("table_x")
    table_y = instruction.group("table_y")
    num = instruction.group("num")
    id = instruction.group("id")

    # Convert
    table_x = int(table_x) if table_x else None
    table_y = int(table_y) if table_y else None
    num = int(num) if num else None

    position = None
    if cmd == "PLACE":
        position = dict(
            x=int(instruction.group("x")), y=int(instruction.group("y")), direction=instruction.group("dir")
        )

    return cmd, table_x, table_y, num, id, position
