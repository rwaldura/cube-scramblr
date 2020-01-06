#
# Utility functions to deal with EV3 colors.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print

import math

# my cube has these colors, and no others
CUBE_COLORS = (
    # Color.BLACK,
    Color.BLUE,
    Color.GREEN,
    Color.YELLOW,
    Color.RED,
    Color.WHITE,
    # Color.BROWN
    Color.ORANGE
    # Color.PURPLE
)

# values in 100-based RGB space, based on experimentation

# yellow
# center color  69.80999999999999 65.27 43.44999999999999

# red
# center color  46.83999999999999 18.65 9.000000000000002

# blue
# center color  11.77 19.13 34.05

# green
# center color  14.26 29.52 10.4

# orange
# center color  55.68 38.73 11.5

# white
# center color  64.76000000000001 73.70000000000001 75.94999999999999

CUBE_COLORS_RGB = [
    { 'r':  0, 'g':  0, 'b':  0 }, # None (undefined)
    { 'r':  0, 'g':  0, 'b':  0 }, # black (undefined)
    { 'r': 12, 'g': 20, 'b': 35 }, # blue
    { 'r': 15, 'g': 30, 'b': 10 }, # green
    { 'r': 70, 'g': 65, 'b': 43 }, # yellow
    { 'r': 47, 'g': 20, 'b':  9 }, # red
    { 'r': 65, 'g': 75, 'b': 75 }, # white
    { 'r':  0, 'g':  0, 'b':  0 }, # brown (undefined)
    { 'r': 55, 'g': 40, 'b': 12 }, # orange
    { 'r':  0, 'g':  0, 'b':  0 }  # purple (undefined)
]

COLOR_NAMES = (
    "",         # 0 - None
    "black",    # 1 - Color.BLACK
    "blue",     # 2 - Color.BLUE
    "green",    # 3 - Color.GREEN
    "yellow",   # 4 - Color.YELLOW
    "red",      # 5 - Color.RED
    "white",    # 6 - Color.WHITE
    "brown",    # 7 - Color.BROWN
    "orange",   # 8 - Color.ORANGE
    "purple"    # 9 - Color.PURPLE
)

max_distance = 174 # √3 * 100, the diagonal of a 100x100x100 cube

##############################################################################
# Return the name of a given Color
def color2str(color) :
    if (color != None and color < len(COLOR_NAMES)) :
        return COLOR_NAMES[color]
    else :
        return ""

##############################################################################
# Map a R/G/B dict to a known Color constant
def rgb2color(rgb) :
    print("mapping R/G/B", rgb['r'], rgb['g'], rgb['b'])

    # compute Euclidean distance to all known colors
    dist = [max_distance] * len(CUBE_COLORS_RGB)
    for i in range(len(dist)) :
        cc = CUBE_COLORS_RGB[i]
        if (cc['r'] > 0) : # ignore undefined colors
            dist[i] = _distance(rgb, cc)
            # print("distance to", color2str(i), "=", dist[i])

    # closest color has the lowest distance
    color = dist.index(min(dist))
    print("found closest color", color, color2str(color))
    return color

def sqr(x) :
    return x * x

def _distance(x, y) :
    return math.sqrt(
          sqr(x['r'] - y['r']) 
        + sqr(x['g'] - y['g'])
        + sqr(x['b'] - y['b'])
    )

##############################################################################
# Allowed colors for the cube
def is_valid(color) :
    return color in CUBE_COLORS
