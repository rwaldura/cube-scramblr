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

# in 100-based RGB space
KNOWN_COLORS = [
    { 'r':  -1, 'g':  -1, 'b':  -1 }, # None
    { 'r':   0, 'g':   0, 'b':   0 }, # black
    { 'r':   0, 'g':   0, 'b': 100 }, # blue
    { 'r':   0, 'g': 100, 'b':   0 }, # green
    { 'r': 100, 'g': 100, 'b':   0 }, # yellow
    { 'r': 100, 'g':   0, 'b':   0 }, # red
    { 'r': 100, 'g': 100, 'b': 100 }, # white
    { 'r':  50, 'g':  25, 'b':   0 }, # brown
    { 'r': 100, 'g':  50, 'b':   0 }, # orange
    { 'r':  50, 'g':   0, 'b':  50 }  # purple
    # { 'r': 100, 'g':   0, 'b': 100 }, # pink
]

COLOR_NAMES = [
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
]

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
    dist = [max_distance] * len(KNOWN_COLORS)
    for i in range(len(dist)) :
        if (i > 0) : # ignore the first dummy color
            dist[i] = get_distance(rgb, KNOWN_COLORS[i])
            print("distance to", color2str(i), "=", dist[i])

    # closest color has the lowest distance
    color = dist.index(min(dist))
    print("found closest color", color, color2str(color))
    return color

def sqr(x) :
    return x * x

def get_distance(x, y) :
    return math.sqrt(
          sqr(x['r'] - y['r']) 
        + sqr(x['g'] - y['g'])
        + sqr(x['b'] - y['b'])
    )