import pytest
from src.exceptions import InvalidCommand
from src.parser import parse


def test_valid_table():
    line = "TABLE 5x4"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "TABLE"
    assert table_x == 5
    assert table_y == 4


def test_valid_robots():
    line = "ROBOTS 5"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "ROBOTS"
    assert num == 5


def test_valid_move():
    line = "MOVE"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == line
    assert not id

    line = "MOVE 1"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "MOVE"
    assert id == "1"


def test_valid_left():
    line = "LEFT"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == line
    assert not id

    line = "LEFT 1"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "LEFT"
    assert id == "1"


def test_valid_right():
    line = "RIGHT"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == line
    assert not id

    line = "RIGHT 1"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "RIGHT"
    assert id == "1"


def test_valid_report():
    line = "REPORT"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == line
    assert not id

    line = "REPORT 1"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "REPORT"
    assert id == "1"


def test_valid_place():
    expected_pos = dict(x=0, y=0, direction="NORTH")
    line = "PLACE 0,0,NORTH"
    cmd, table_x, table_y, num, id, position = parse(line)

    assert cmd == "PLACE"
    assert position == expected_pos


def test_invalid_cmd():
    line = "PLACE"
    with pytest.raises(InvalidCommand):
        cmd, table_x, table_y, num, id, position = parse(line)

    line = "PLACE A,B,UP"
    with pytest.raises(InvalidCommand):
        cmd, table_x, table_y, num, id, position = parse(line)
