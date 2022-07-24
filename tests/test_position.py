import pytest
from src.exceptions import CollisionError, InvalidPosition
from src.position import Position


def test_set_position(position, table):
    assert position.x == 0
    assert position.y == 0
    assert position.direction == "NORTH"
    assert position.table == table


def test_invalid_position(table):
    Position.set_table(table)
    data = dict(x=-1, y=-1, direction="UP")
    with pytest.raises(InvalidPosition):
        Position.set_position(data)


def test_set_position_no_table():
    Position.table = None
    data = dict(x=0, y=0, direction="NORTH")
    with pytest.raises(InvalidPosition):
        Position.set_position(data)


def test_get_position(position, table):
    data = dict(x=0, y=0, direction="NORTH")
    assert data == position.get_position()


def test_get_position_no_table(position):
    Position.table = None
    assert not position.get_position()


def test_position_repr(position):
    assert position.__repr__() == "0,0,NORTH"


def test_position_collision_error(robot, table):
    Position.set_table(table)
    table.place(robot, 0, 0)
    data = dict(x=0, y=0, direction="NORTH")
    with pytest.raises(CollisionError):
        Position.set_position(data)
