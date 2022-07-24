import pytest
from src.position import Position
from src.robot import Robot
from src.table import Table


@pytest.fixture(scope="function")
def robot():
    return Robot()


@pytest.fixture(scope="function")
def table():
    return Table()


@pytest.fixture(scope="function")
def position(table):
    Position.set_table(table)
    position = dict(x=0, y=0, direction="NORTH")
    return Position.set_position(position)
