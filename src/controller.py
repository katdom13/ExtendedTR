from .exceptions import CollisionError, InvalidCommand
from .parser import parse
from .position import Position
from .robot import Robot
from .table import Table


class Controller(object):
    table = None
    robots = []
    place_counter = -1

    def start(self, file):
        with open(file, encoding="utf-8") as f:
            for idx, line in enumerate(f):
                try:
                    line = line.strip()
                    cmd, table_x, table_y, num, id, position = parse(line)

                    # Check the first two commands if it configures the table
                    # and the number of knights
                    if idx == 0 or idx == 1:
                        if cmd == "TABLE" and not self.table:
                            self.table = Table(table_x, table_y)
                            Position.set_table(self.table)
                        elif cmd == "ROBOTS" and not self.robots:
                            for i in range(1, num + 1):
                                self.robots.append(Robot(id=i))
                        else:
                            if not self.table:
                                self.table = Table()
                                # Set the position class table
                                Position.set_table(self.table)
                            if not self.robots:
                                self.robots.append(Robot())

                    # Place commands are alternating between robots
                    if cmd == "PLACE":
                        self.place_counter += 1
                        robot = self.robots[self.place_counter % len(self.robots)]
                        robot.place(position)
                    elif cmd not in ["PLACE", "TABLE", "ROBOTS"]:
                        # Ignore if there are more than 1 robots and the id is not indicated
                        # Or if an id is indicated but there are no other robots
                        if (not id and len(self.robots) > 1) or (id and len(self.robots) <= 1):
                            continue

                        robot = self.robots[int(id) - 1] if (id and len(self.robots) > 1) else self.robots[0]
                        getattr(robot, cmd.lower())()
                except InvalidCommand:
                    pass
                except CollisionError:
                    if cmd == "PLACE":
                        self.place_counter -= 1
