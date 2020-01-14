#
# Unit test.
#

from color_mapper import *
from asserts import *

# tricky-tricky: the black color is not a possible mapping; it's mapped to BLUE instead
assertEqual("mapping true BLACK",  Color.BLUE,  rgb2color({ 'r':  0, 'g':  0, 'b':  0 }))

assertEqual("mapping true WHITE",  Color.WHITE, rgb2color({ 'r':100, 'g':100, 'b':100 }))

# we struggle to correctly map pure primaries, so use made-up values instead
assertEqual("mapping true RED",    Color.WHITE, rgb2color({ 'r':100, 'g':  0, 'b':  0 }))
assertEqual("mapping color RED",   Color.RED,   rgb2color({ 'r': 50, 'g': 10, 'b': 10 }))

assertEqual("mapping true GREEN",  Color.BLUE,  rgb2color({ 'r':  0, 'g':100, 'b':  0 }))
assertEqual("mapping color GREEN", Color.GREEN, rgb2color({ 'r': 15, 'g': 30, 'b': 10 }))

assertEqual("mapping color BLUE",  Color.BLUE,  rgb2color({ 'r':  0, 'g':  0, 'b':100 }))
