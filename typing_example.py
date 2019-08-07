from typing import NamedTuple

# Create tuple type
class Point(NamedTuple):
    x: int
    y: int = 0

# Instantiate
Point(0, 1)
Point(x=0, y=0)
Point(0)                # use default value
Point('not an int')     # does not cause a type error!

# Access
point = Point(x=0, y=1)
point.x
point.y

point[0]
point[1]

# Member assignment is not allowed - tuples are immutable
# point.x = 7
# point[0] = 7
