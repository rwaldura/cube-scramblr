#
# Unit test.
# 

from cube import *

def assertTrue(mesg, cond) :
    if (not cond) :
        print("FAIL:", mesg)
        assert cond
    else :
        print("pass:", mesg)

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

set_center_rgb(3, {'r':12, 'g':24, 'b':42})
assertEqual("set center color rgb", {'r':12, 'g':24, 'b':42}, center_rgb(2))

set_facelet(2, 1, Color.BLUE)
assertEqual("set facelet color", Color.BLUE, facelet(2, 1))

set_facelet_rgb(1, 4, {'r':2, 'g':3, 'b':4})
assertEqual("set facelet color rgb", {'r':2, 'g':3, 'b':4}, facelet_rgb(1, 4))

assertTrue("valid color 1", is_valid(Color.GREEN))
assertTrue("valid color 2", not is_valid(Color.PURPLE))

assertEqual("uniq 1", {'a', 'b', 'c', 'd'}, uniq((('a', 'b'), ('c', 'd'))))
assertEqual("uniq 2", {'a', 'b', 'c', 'd'}, uniq(('a', 'b', 'c', 'd')))
assertEqual("uniq 3", {'a', 'b', 'c', 'd'}, uniq(('a', ('b'), 'c', ('d'))))
assertEqual("uniq 4", {'a', 'b', 'c', 'd'}, uniq(('a', ('b', ('c')), ('d'))))

assertEqual("corner colors 1", 
    { Color.BLUE, Color.GREEN, Color.RED, Color.ORANGE }, 
    corner_colors(Color.WHITE))

assertEqual("corner colors 2", 
    { Color.YELLOW, Color.RED, Color.WHITE, Color.ORANGE }, 
    corner_colors(Color.GREEN))

assertEqual("corner colors 3", 
    { Color.ORANGE, Color.RED },
    corner_colors(Color.WHITE, Color.BLUE))

assertEqual("corner colors 4", 
    { Color.ORANGE, Color.RED }, 
    corner_colors(Color.YELLOW, Color.GREEN))

assertEqual("corner colors 5", 
    { Color.YELLOW, Color.WHITE }, 
    corner_colors(Color.RED, Color.BLUE))

assertEqual("corner colors 6", 
    set(), 
    corner_colors(Color.ORANGE, Color.RED))
