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

def assertListEqual(mesg, expected, actual) :
    assertEqual(mesg, len(expected), len(actual))
    for i in range(len(expected)) :
        assertEqual(mesg, expected[i], actual[i])

##############################################################################
# main, for unit testing

set_center(2, Color.WHITE)
assertEqual("set center color", Color.WHITE, center(2))

set_facelet(2, 1, Color.BLUE)
assertEqual("set facelet color", Color.BLUE, facelet(2, 1))

colors = corner_colors(Color.WHITE)
assertListEqual("corner colors 1", 
    (Color.BLUE, Color.GREEN, Color.RED, Color.ORANGE), 
    colors)

colors = corner_colors(Color.GREEN)
assertListEqual("corner colors 2", 
    (Color.YELLOW, Color.RED, Color.WHITE, Color.ORANGE), 
    colors)

colors = corner_colors(Color.WHITE, Color.BLUE)
assertListEqual("corner colors 3", (Color.ORANGE, Color.RED), colors)

colors = corner_colors(Color.YELLOW, Color.GREEN)
assertListEqual("corner colors 4", (Color.ORANGE, Color.RED), colors)

colors = corner_colors(Color.RED, Color.BLUE)
assertListEqual("corner colors 5", (Color.YELLOW, Color.WHITE), colors)

colors = corner_colors(Color.ORANGE, Color.RED)
assertListEqual("corner colors 6", (), colors)
