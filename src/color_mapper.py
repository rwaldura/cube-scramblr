#
# Color scanning logic.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print

import cube

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

CUBE_COLORS_RGB = (
    None,                           # 0 - undefined
    None,                           # 1 - black (undefined)
    { 'r': 12, 'g': 20, 'b': 34 },  # 2 - blue
    { 'r': 15, 'g': 30, 'b': 10 },  # 3 - green
    { 'r': 70, 'g': 65, 'b': 43 },  # 4 - yellow
    { 'r': 50, 'g': 19, 'b':  9 },  # 5 - red
    { 'r': 75, 'g': 75, 'b': 75 },  # 6 - white
    None,                           # 7 - brown (undefined)
    { 'r': 56, 'g': 39, 'b': 12 },  # 8 - orange
    None                            # 9 - purple (undefined)
)

max_distance = 30000 # (√3 * 100)^2, the squared diagonal of a 100x100x100 cube

##############################################################################
# Map a R/G/B dict to a known Color constant
def rgb2color(rgb) :
    print("mapping R/G/B", rgb['r'], rgb['g'], rgb['b'])

    # compute Euclidean distance to all known colors
    dist = [max_distance] * (1 + max(cube.CUBE_COLORS))
    for c in (cube.CUBE_COLORS) :
        dist[c] = distance2(rgb, CUBE_COLORS_RGB[c])
        # print("distance to", color2str(c), "=", dist[c])

    # closest color has the lowest distance
    color = dist.index(min(dist))
    # print("found closest color", color, color2str(color))
    return color

def sqr(x) :
    return x * x

##############################################################################
# Compute Euclidean distance (squared) between 2 points in RGB space. 
# Optimization: since all we do is compare distances (the actual value
# is not relevant), only return the squared distance -- no need to compute
# the square root
def distance2(x, y) :
    return sqr(x['r'] - y['r']) 
    + sqr(x['g'] - y['g'])
    + sqr(x['b'] - y['b'])
