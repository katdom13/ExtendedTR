# ToyRobot
The Toy Robot is based on a blog post by Jon Eaves. Read it here https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/

It's a common test used by a few different Melbourne based companies, and for got reason. It's simple and can be completed in a reasonable time frame, but is also fairly flexible and open ended in the way a developer can approach it. Because of this, you can gain great insight into how the developer thinks about code. Do they consider the problem domain in their code? Do they correctly use design patterns? Are they a functional or object-oriented programmer? Do they over-engineer or practice YAGNI?

The Toy Robot also provides a great starting point for an in-interview pairing exercise. Candidates can work on code they are familiar with, which helps with creating a flowing pairing session in a limited time window.


## Usage

### Prerequisites

* Create a virtual environment
```
python -m venv venv
```

* Activate the virtual environment
```
venv\Scripts\activate
```

* Install requirements
```
pip install -r requirements.txt
```

### Running the application
```
python main.py <filename>
```

## Extending the solution

### Make the table size configurable

#### Command:
```
TABLE <columns>x<rows>
```

#### Caveats
- This should be in either the first or second line of the file input
- If not, this command will be ignored and the table size will be set to 5x5


### Add 2 (or n) robots on the table

#### Command:
```
ROBOTS <num>
```

#### Caveats
- This should be in either the first or second line of the file input
- If not, this command will be ignored and the robot number is set to 1 by default
- The commands "MOVE", "LEFT", "RIGHT", and "REPORT" will require and id
```
MOVE 1
LEFT 2
RIGHT 1
REPORT 1
```

### Multiple places, multiple robots
Consider the commands below:
```
ROBOTS 2
PLACE 1,2,NORTH
PLACE 1,3,NORTH
PLACE 1,3,NORTH
PLACE 1,4,NORTH
PLACE 1,4,NORTH
REPORT 1
REPORT 2
```

The result is
```
1,4,NORTH
1,3,NORTH
```

Why?

1.  first place command is for robot 1 (PLACE 1,2,NORTH)
2.  second place command is for robot 2 (PLACE 1,3,NORTH)
3.  third place command is for robot 1 again, but this fails due to collision with robot 2 and is ignored. (PLACE 1,3,NORTH)
4. fourth place command is still for robot 1 because the place command prior failed. (PLACE 1,4,NORTH)
5. ce the fourth place command did not fail, the next one is for robot 2, but this one is ignored due to failing and robot 2 retains its position. (PLACE 1,4,NORTH)

So the place commands alternate between the multiple robots, but stays with a robot if it fails.
