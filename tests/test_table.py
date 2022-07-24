def test_create_table(table):
    assert table
    assert table.table
    assert table.x == 5
    assert table.y == 5


def test_table_place(robot, table):
    el = table.place(robot, 0, 0)
    assert el
    assert el == robot


def test_table_place_no_table(robot, table):
    table.table = None
    el = table.place(robot, 0, 0)
    assert not el


def test_table_get(robot, table):
    el = table.place(robot, 0, 0)
    got = table.get(0, 0)

    assert el == got == robot


def test_table_get_no_table(robot, table):
    table.table = None
    el = table.place(robot, 0, 0)
    got = table.get(0, 0)

    assert not el
    assert not got


def test_table_has_content(robot, table):
    table.place(robot, 0, 0)
    assert table.has_content(0, 0)


def test_table_content_no_table(robot, table):
    table.table = None
    table.place(robot, 0, 0)
    assert not table.has_content(0, 0)


def test_table_remove(robot, table):
    el = table.place(robot, 0, 0)
    removed = table.remove(0, 0)

    assert el == removed
    assert not table.has_content(0, 0)


def test_table_remove_no_table(robot, table):
    table.table = None
    el = table.place(robot, 0, 0)
    removed = table.remove(0, 0)

    assert not el
    assert not removed
