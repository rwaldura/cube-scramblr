#
# Color scanning logic.
# This module implements logic to determine the Color of a facelet.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print

import cube
import color_utils as cu

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

MAX_DISTANCE = 3 * 100 * 100 # (√3 * 100)^2, the squared diagonal of a 100x100x100 cube

##############################################################################
# Return the name of a given Color
def rgb2str(rgb) :
    return cu.color2str(rgb2color(rgb))

##############################################################################
# Map a R/G/B dict to a known Color constant
def rgb2color(rgb) :
    print("mapping RGB {}/{}/{}".format(rgb['r'], rgb['g'], rgb['b']))
    color = pick_closest_color(rgb)
    return color

##############################################################################
# Compute Euclidean distance to all known colors, and 
# return the known color that has the shortest distance to parameter.
def pick_closest_color(rgb) :
    dist = [MAX_DISTANCE] * (1 + max(cube.CUBE_COLORS))

    for c in (cube.CUBE_COLORS) :
        dist[c] = distance2(rgb, CUBE_COLORS_RGB[c])
        # print("distance to", color2str(c), "=", dist[c])

    return dist.index(min(dist))

def sqr(x) :
    return x * x

##############################################################################
# Compute Euclidean distance (squared) between 2 points in RGB space. 
# Optimization: since all we do is compare distances (the actual value
# is irrelevant), only return the squared distance -- no need to compute
# the square root
def distance2(x, y) :
    d = sqr(x['r'] - y['r']) + sqr(x['g'] - y['g']) + sqr(x['b'] - y['b'])
    # print("distance between", x, "and", y, "=", d)
    return d

##############################################################################
# Assign a color to each center facelet -- it represents the face color.
#
# Compute distance for each face color. The face that has the highest
# distance overall, is labelled White. Its opposite face is Yellow.
# The face that has the smallest distance from black is Blue. Its opposite 
# face is Green.
# For red, we pick the face with the highest red component. The last face is 
# therefore Orange.
def map_face_centers() :
    dist = [0] * 6
    for f in range(6) :
        dist[f] = distance2(cube.center_rgb(f), cu.RGB_BLACK)
        print("face", f, "color", cube.center_rgb(f), "distance to black", dist[f])

    map_face_center(dist.index(max(dist)), Color.WHITE)
    map_face_center(dist.index(min(dist)), Color.BLUE)

    # find how close the last un-mapped faces are to RED
    for f in range(6) :
        if (cube.is_valid(cube.center(f))) :
            dist[f] = MAX_DISTANCE # skip mapped face
        else :
            dist[f] = distance2(cube.center_rgb(f), cu.RGB_RED)

    map_face_center(dist.index(min(dist)), Color.RED)

##############################################################################
def map_face_center(face, color) :
    cube.set_center(face, color)
    print("face #", face, "mapped to", cu.color2str(color))

    opp_face = cube.opposite_face(face)
    cube.set_center(opp_face, cube.opposite_color(color))
    print("opposite face #", opp_face, "mapped to", cu.color2str(cube.center(opp_face)))

