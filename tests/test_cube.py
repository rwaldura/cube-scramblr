#
# Unit test.
# 

from cube import *
from asserts import *

set_center(1, Color.WHITE)
assertEqual("1.1. center color", Color.BLACK, center(0))
assertEqual("1.2. center color", Color.WHITE, center(1))
assertEqual("1.3. center color", Color.BLACK, center(2))

set_center_rgb(2, {'r':12, 'g':24, 'b':42})
assertEqual("2.1. center color rgb", {'r': 0, 'g': 0, 'b': 0}, center_rgb(1))
assertEqual("2.2. center color rgb", {'r':12, 'g':24, 'b':42}, center_rgb(2))
assertEqual("2.3. center color rgb", {'r': 0, 'g': 0, 'b': 0}, center_rgb(3))
assertEqual("2.4. center color", Color.BLACK, center(2))

set_facelet(2, 1, Color.BLUE)
assertEqual("3.1. facelet color", Color.BLUE,  facelet(2, 1))
assertEqual("3.2. facelet color", Color.BLACK, facelet(2, 2))
assertEqual("3.3. center color rgb", {'r':12, 'g':24, 'b':42}, center_rgb(2))
assertEqual("3.4. center color", Color.WHITE, center(1))
assertEqual("3.5. center color", Color.BLACK, center(2))

set_facelet_rgb(1, 4, {'r':2, 'g':3, 'b':4})
assertEqual("4.1. facelet color rgb", {'r':2, 'g':3, 'b':4}, facelet_rgb(1, 4))
assertEqual("4.2. facelet color", Color.BLUE, facelet(2, 1))
assertEqual("4.3. center color rgb", {'r':12, 'g':24, 'b':42}, center_rgb(2))
assertEqual("4.4. center color", Color.WHITE, center(1))
assertEqual("4.5. center color", Color.BLACK, center(2))

# print(to_str())

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

assertEqual("opposite face 1.1",
    Color.YELLOW,
    opposite_face_color(Color.WHITE))

assertEqual("opposite face 1.2",
    Color.WHITE,
    opposite_face_color(Color.YELLOW))

assertEqual("opposite face 2.1",
    Color.BLUE,
    opposite_face_color(Color.GREEN))

assertEqual("opposite face 2.2",
    Color.GREEN,
    opposite_face_color(Color.BLUE))

assertEqual("opposite face 3.1",
    Color.RED,
    opposite_face_color(Color.ORANGE))

assertEqual("opposite face 3.2",
    Color.ORANGE,
    opposite_face_color(Color.RED))
