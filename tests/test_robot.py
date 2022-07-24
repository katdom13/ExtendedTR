from src.position import Position
from src.robot import Robot
from src.table import Table


def test_robot_init(robot):
    assert robot


def test_robot_init_with_position(capsys):
    table = Table()
    Position.set_table(table)

    data = dict(x=0, y=0, direction="NORTH")
    position = Position.set_position(data)
    robot = Robot(1, position)

    assert robot
    assert robot.id == 1
    assert robot.position.get_position() == data


def test_report(robot, capsys):
    table = Table()
    Position.set_table(table)

    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)
    robot.report()

    out, err = capsys.readouterr()
    assert out == "0,0,NORTH\n"


def test_report_no_position(robot, capsys):
    table = Table()
    Position.set_table(table)

    robot.report()

    out, err = capsys.readouterr()
    assert not out


def test_valid_move(robot, capsys):
    table = Table()
    Position.set_table(table)

    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)
    robot.move()

    robot.report()
    out, err = capsys.readouterr()
    assert out == "0,1,NORTH\n"

    robot.right()
    robot.move()

    robot.report()
    out, err = capsys.readouterr()
    assert out == "1,1,EAST\n"

    robot.right()
    robot.move()

    robot.report()
    out, err = capsys.readouterr()
    assert out == "1,0,SOUTH\n"

    robot.right()
    robot.move()

    robot.report()
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"


def test_move_no_position(robot, capsys):
    robot.move()
    out, err = capsys.readouterr()
    assert not out
    assert not robot.position


def test_invalid_moves(robot, capsys):
    table = Table()
    Position.set_table(table)

    position = dict(x=-1, y=-1, direction="UP")
    robot.place(position)
    robot.report()
    out, err = capsys.readouterr()
    assert not out

    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)
    robot.report()
    out, err = capsys.readouterr()
    assert out == "0,0,NORTH\n"

    robot2 = Robot()
    position = dict(x=0, y=1, direction="NORTH")
    robot2.place(position)

    robot.move()
    robot.report()
    out, err = capsys.readouterr()
    assert out == "0,0,NORTH\n"


def test_rotate(robot, capsys):
    table = Table()
    Position.set_table(table)

    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)

    robot.left()
    assert robot.position.direction == "WEST"

    robot.left()
    assert robot.position.direction == "SOUTH"

    robot.left()
    assert robot.position.direction == "EAST"

    robot.right()
    assert robot.position.direction == "SOUTH"

    robot.right()
    assert robot.position.direction == "WEST"

    robot.right()
    assert robot.position.direction == "NORTH"


def test_rotate_no_position(robot, capsys):
    table = Table()
    Position.set_table(table)

    robot.left()
    robot.report()
    out, err = capsys.readouterr()
    assert not out

    assert not robot.position

    robot.right()
    robot.report()
    out, err = capsys.readouterr()
    assert not out

    assert not robot.position


def test_valid_place(robot):
    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)

    assert robot.position


def test_invalid_place(robot):
    position = dict(x=5, y=5, direction="NORTHWEST")
    robot.place(position)

    assert not robot.position


def test_replace_robot(robot):
    table = Table()
    Position.set_table(table)

    position = dict(x=0, y=0, direction="NORTH")
    robot.place(position)

    assert table.table[0][0] == robot

    position = dict(x=1, y=1, direction="NORTH")
    robot.place(position)

    assert not table.table[0][0]
    assert table.table[1][1] == robot
