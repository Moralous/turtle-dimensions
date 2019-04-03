class point(object):
    """A point in 3d space, can be represented by a 3x1 matrix"""
    def __init__(self, x:float, y:float, z:float):
        self.matrix = [x, y, z]

class triangle(object):
    """A triangle formed by three points in space.
    Can be represented by a 3x3 matrix"""

    def __init__(self, a:point, b:point, c:point):
        self.matrix = [a, b, c]  # A 2d array forming a 3x3 matrix

# Our main goal is to render a rotating, three dimensional cube:
# First, we will attempt to render a triangle without the face.
# Then, we will attempt to render a triangle with the face.
# Then, we will attempt to render a cube without the faces.
# Finally, we will attempt to use triangles to form a cube, and render them instead - first without faces, then with.
# If we manage all that, we will attempt to rotate the image frame by frame to create the rotating cube we desire.

our_triangle = triangle(point(1, 0, 0),
                        point(0, 1, 0),
                        point(0, 0, 1))

# To render a triangle, we need to flatten these coordinates to 2d coordinates.
# We can then draw ("render") them using turtle.
def flatten(shape):
    
