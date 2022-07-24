import sys

from src.controller import Controller

if __name__ == "__main__":
    filename = sys.argv[1]
    c = Controller()

    c.start(filename)
