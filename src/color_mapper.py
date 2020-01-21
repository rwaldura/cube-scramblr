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
    { 'r': 50, 'g': 60, 'b': 43 },  # 4 - yellow
    { 'r': 50, 'g': 19, 'b':  9 },  # 5 - red
    { 'r': 65, 'g': 65, 'b': 65 },  # 6 - white
    None,                           # 7 - brown (undefined)
    { 'r': 50, 'g': 39, 'b': 12 },  # 8 - orange
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
    color = pick_closest_color(rgb)
    # print("mapped RGB {}/{}/{} to color {}".format(rgb['r'], rgb['g'], rgb['b'], color))
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
def distance2(a, b) :
    (aR, aG, aB) = (a['r'], a['g'], a['b'])
    (bR, bG, bB) = (b['r'], b['g'], b['b'])
    d = sqr(aR - bR) + sqr(aG - bG) + sqr(aB - bB)
    # print("distance between", a, "and", b, "=", d)
    return d

##############################################################################
# Assign a color to each center facelet -- it represents the face color.
def map_face_centers() :
    for f in cube.faces() :
        rgb = cube.center_rgb(f)
        color = rgb2color(rgb)
        cube.set_center(f, color)
        print("face", f, "mapped to", cu.color2str(color))

    distinct = validate_distinct_face_colors()
    print("distinct color check:", distinct)

    opposites = validate_opposite_face_colors()
    print("opposite color check:", opposites)

    return distinct and opposites

##############################################################################
# validate each face is mapped to a distinct color
def validate_distinct_face_colors() :
    face_colors = map(lambda f: cube.center(f), cube.faces())
    return cube.CUBE_COLORS == set(face_colors)

##############################################################################
# validate each opposite face has the opposite color
def validate_opposite_face_colors() :
    result = True

    for f in cube.faces() :
        color = cube.center(f)
        opp_face = cube.opposite_face(f)
        result = result and cube.center(opp_face) == cube.opposite_color(color)
        
    return result

##############################################################################
# Alernate way to map color, by using cube hints
def _alt_map_face_centers() :
    f = closest_face_center(cu.RGB_WHITE)
    map_face_center(f, Color.WHITE)

    f = closest_face_center(cu.RGB_BLUE)
    map_face_center(f, Color.BLUE)

    f = closest_face_center(cu.RGB_RED)
    map_face_center(f, Color.RED)

##############################################################################
def closest_face_center(rgb) :
    dist = [0] * cube.faces()

    for f in cube.faces() :
        if (cube.is_valid(cube.center(f))) : # skip already mapped face
            dist[f] = MAX_DISTANCE 
        else :
            dist[f] = distance2(cube.center_rgb(f), rgb)

    return dist.index(min(dist))

##############################################################################
def map_face_center(face, color) :
    # sanity check: prevent overwrites
    #assert cube.center(face) == cu.RGB_BLACK

    cube.set_center(face, color)
    print("face", face, "mapped to", cu.color2str(color))

    opp_face = cube.opposite_face(face)
    cube.set_center(opp_face, cube.opposite_color(color))
    print("opposite face", opp_face, "mapped to", cu.color2str(cube.center(opp_face)))

