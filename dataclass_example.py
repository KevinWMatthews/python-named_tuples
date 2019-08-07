from dataclasses import dataclass

# Create class
@dataclass
class Point():
    x: int
    y: int = 0

# Instantiate
Point(0, 1)
Point(x=0, y=1)
Point(0)
Point('wat')        # does not cause a type error!

# Access
point = Point(x=0, y=1)

point.x
point.y

# Does not allow subscript notation
# point[0]
# point[1]

# This class allows assignment!
point.x = 7
point.y = 8
