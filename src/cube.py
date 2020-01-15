#
# Core data structure.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color

import color_utils

_facelet = { 
    'rgb': { 'r':0, 'g':0, 'b':0 }, 
    'color': Color.BLACK 
}

# initialize the cube
_cube = [None] * 6
for i in range(6) :
    _cube[i] = [None] * 9
    for j in range(9) :
        _cube[i][j] = dict(_facelet)

# my cube has these colors, and no others
CUBE_COLORS = (
    # Color.BLACK
    Color.BLUE,
    Color.GREEN,
    Color.YELLOW,
    Color.RED,
    Color.WHITE,
    # Color.BROWN
    Color.ORANGE
    # Color.PURPLE
)

# Corner pieces have these colors.
# Note color order does not matter
CUBE_CORNERS = (
    # from white face
    (Color.WHITE, Color.GREEN, Color.RED),
    (Color.WHITE, Color.GREEN, Color.ORANGE),
    (Color.RED, Color.WHITE, Color.BLUE),
    (Color.ORANGE, Color.WHITE, Color.BLUE),
    # from yellow face
    (Color.ORANGE, Color.GREEN, Color.YELLOW),
    (Color.YELLOW, Color.GREEN, Color.RED),
    (Color.RED, Color.YELLOW, Color.BLUE),
    (Color.BLUE, Color.YELLOW, Color.ORANGE)
)

# Edge pieces.
# again, tuple order does not matter
# edge (green, orange) == edge (orange, green)
CUBE_EDGES = (
    # green face: no blue
    (Color.GREEN, Color.RED),
    (Color.GREEN, Color.WHITE),
    (Color.GREEN, Color.ORANGE),
    (Color.GREEN, Color.YELLOW),
    # blue face: no green
    (Color.BLUE, Color.RED), 
    (Color.BLUE, Color.WHITE),
    (Color.BLUE, Color.ORANGE),
    (Color.BLUE, Color.YELLOW),
    # in between
    (Color.YELLOW, Color.RED),
    (Color.YELLOW, Color.ORANGE),
    (Color.WHITE, Color.RED),
    (Color.WHITE, Color.ORANGE)
)

##############################################################################
# Return the color constant of a facelet, defined by its number
# with: 
# 0: center
# 1, 3, 5, 7: edge pieces
# 2, 4, 6, 8: corner pieces
def facelet(face, n) :
    return _cube[face][n]['color']

# Return the RGB color of a facelet, defined by its number
def facelet_rgb(face, n) :
    return _cube[face][n]['rgb']

def set_facelet(face, n, color) :
    _cube[face][n]['color'] = color

def set_facelet_rgb(face, n, rgb) :
    _cube[face][n]['rgb'] = rgb

def center(face) :
    return facelet(face, 0)

def center_rgb(face) :
    return facelet_rgb(face, 0)

def set_center(face, color) :
    set_facelet(face, 0, color)

def set_center_rgb(face, rgb) :
    set_facelet_rgb(face, 0, rgb)

##############################################################################
# Allowed colors for the cube
def is_valid(color) :
    return color in CUBE_COLORS

##############################################################################
# Return the possible colors for a corner piece, given 1 or 2 colors
def corner_colors(color1, color2 = None) :
    assert color1 != color2

    corners = filter(
        lambda corner: color1 in corner, 
        CUBE_CORNERS)

    if (color2 != None) :
        corners = filter(
            lambda corner: color2 in corner,
            corners)

    return uniq(corners) - { color1, color2 }

##############################################################################
# Flatten a list, and return the unique elements
def uniq(l) :
    return { item for sublist in l for item in sublist }

##############################################################################
def to_str() :
    result = []

    for face in range(len(_cube)) :
        for facelet in range(len(_cube[face])) :
            rgb = facelet_rgb(face, facelet)
            (red, green, blue) = (rgb['r'], rgb['g'], rgb['b'])
            color = color_utils.rgb2str(rgb)
            s = "face {} facelet {} RGB {}/{}/{} mapped to {}".format(
                face, facelet, red, green, blue, color
            )
            result.append(s)

    return "\n".join(result)
