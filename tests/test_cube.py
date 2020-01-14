#
# Unit test.
# 

from cube import *

def assertEqual(mesg, expected, actual) :
    if (expected != actual) :
        print("FAIL:", mesg, "expected", expected, "but got instead", actual)
        assert False
    else :
        print("pass:", mesg)

##############################################################################
# main, for unit testing

set_center(2, Color.WHITE)
assertEqual("set center color", Color.WHITE, center(2))

set_facelet(2, 1, Color.BLUE)
assertEqual("set facelet color", Color.BLUE, facelet(2, 1))

corner_colors = corner_colors(Color.WHITE, Color.BLUE)
assertEqual("corner colors 2", (Color.RED, Color.ORANGE), corner_colors)

corner_colors = corner_colors(Color.WHITE, None)
assertEqual("corner colors 1", 
    (Color.RED, Color.ORANGE, Color.BLUE, Color.GREEN), 
    corner_colors)
 