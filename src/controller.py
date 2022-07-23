from parser import parse

from robot import Robot
from table import Table


def main(file):
    table = None
    robots = []
    place_counter = -1

    with open(file) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            instruction = parse(line)
            cmd = instruction.group("cmd")

            # The first two lines determine the table dimensions and 
            if idx == 0 or idx == 1:
                if cmd == 'TABLE' and not table:
                    x = int(instruction.group("table_x"))
                    y = int(instruction.group("table_y"))
                    table = Table(x, y)
                elif cmd == 'ROBOTS' and not robots:
                    num = int(instruction.group("num"))
                    for i in range(1, num + 1):
                        robots.append(
                            Robot(id=i)
                        )
                else:
                    table = Table()
                    robots.append(Robot())

            if cmd == 'PLACE':
                x = int(instruction.group("x"))
                y = int(instruction.group("y"))
                d = int(instruction.group("d"))
