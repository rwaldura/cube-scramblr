#
# Unit test.
#

from color_mapper import *
from asserts import *

##############################################################################
assertEqual("distance black-black", 0, distance2(cu.RGB_BLACK, cu.RGB_BLACK))
assertEqual("distance black-blue", 100 * 100, distance2(cu.RGB_BLACK, cu.RGB_BLUE))
assertEqual("distance blue-black", 100 * 100, distance2(cu.RGB_BLUE, cu.RGB_BLACK))
assertEqual("distance red-black", 100 * 100, distance2(cu.RGB_RED, cu.RGB_BLACK))
assertEqual("distance red-blue", 100 * 100 + 100 * 100, distance2(cu.RGB_RED, cu.RGB_BLUE))
assertEqual("distance green-red", 100 * 100 + 100 * 100, distance2(cu.RGB_GREEN, cu.RGB_RED))
assertEqual("distance white-black", MAX_DISTANCE, distance2(cu.RGB_WHITE, cu.RGB_BLACK))

##############################################################################
assertEqual("mapping true WHITE",  Color.WHITE, rgb2color(cu.RGB_WHITE))
assertEqual("mapping true RED",    Color.RED, rgb2color(cu.RGB_RED))
assertEqual("mapping true GREEN",  Color.GREEN,  rgb2color(cu.RGB_GREEN))
assertEqual("mapping color BLUE",  Color.BLUE,  rgb2color(cu.RGB_BLUE))

# tricky-tricky: the black color is not a possible mapping
# assertEqual("mapping true BLACK",  None,  rgb2color(cu.RGB_BLACK))

##############################################################################
cube.set_center_rgb(0, cu.RGB_WHITE)
# therefore face 2 is yellow
cube.set_center_rgb(1, cu.RGB_BLUE)
# therefore face 3 is green
cube.set_center_rgb(4, cu.RGB_RED)
# therefore face 5 is orange 

map_face_centers()

assertEqual("mapped face 1.1", Color.WHITE, cube.center(0))
assertEqual("mapped face 1.2", Color.YELLOW, cube.center(2))
assertEqual("mapped face 1.3", Color.BLUE, cube.center(1))
assertEqual("mapped face 1.4", Color.GREEN, cube.center(3))
assertEqual("mapped face 1.5", Color.RED, cube.center(4))
assertEqual("mapped face 1.6", Color.ORANGE, cube.center(5))

# negative test
assertEqual("mapped face 1.7", Color.BLACK, cube.facelet(0, 1))
assertEqual("mapped face 1.8", Color.BLACK, cube.facelet(1, 1))
assertEqual("mapped face 1.9", Color.BLACK, cube.facelet(2, 1))

##############################################################################
cube.reset()

cube.set_center_rgb(0, cu.RGB_GREEN)
cube.set_center_rgb(1, cu.RGB_RED)
cube.set_center_rgb(2, cu.RGB_BLUE)
cube.set_center_rgb(4, cu.RGB_WHITE)

map_face_centers()

assertEqual("mapped face 2.1", Color.GREEN, cube.center(0))
assertEqual("mapped face 2.2", Color.BLUE, cube.center(2))
assertEqual("mapped face 2.3", Color.RED, cube.center(1))
assertEqual("mapped face 2.4", Color.ORANGE, cube.center(3))
assertEqual("mapped face 2.5", Color.WHITE, cube.center(4))
assertEqual("mapped face 2.6", Color.YELLOW, cube.center(5))

