import os
from pathlib import Path

from src.controller import Controller
from src.position import Position

BASE_DIR = Path(__file__).resolve().parent.parent


def test_move(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample1.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "0,1,NORTH\n"


def test_rotate(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample2.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"


def test_complicated_commands(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample3.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "3,3,NORTH\n"


def test_multiple_robots(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample4.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "1,2,NORTH\n"


def test_multiple_robots_place_commands(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    table = None
    Position.set_table(table)
    filename = os.path.join(BASE_DIR, "examples", "sample5.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "1,4,NORTH\n1,3,NORTH\n"


def test_table_config(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample6.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert "9,9,NORTH\n" in out
    assert "0,0,EAST\n" in out
    assert "0,9,WEST\n" in out


def test_invalid_id(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample7.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == "0,9,WEST\n"


def test_invalid_command(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "examples", "sample8.txt")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == ""


def test_invalid_file(capsys):
    c = Controller()
    c.table = None
    c.robots = []
    c.place_counter = -1

    filename = os.path.join(BASE_DIR, "src", "constants.py")
    c.start(filename)
    out, err = capsys.readouterr()
    assert out == ""
