import collections

# Create tuple type
typename = 'Point'              # string
field_names = ('x', 'y')        # iterable
# Convention: variable name is the same as the typename
Point = collections.namedtuple(typename, field_names, verbose=False)

# Instantiate tuple
Point(0, 1)
Point(x=0, y=1)
Point(0, y=1)
Point(y=1, x=1)

# Access
point = Point(x=0, y=0)

# by field name
point.x
point.y

# or by index
point[0]
point[1]
