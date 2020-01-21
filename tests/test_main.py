#
# Unit test.
#

from main import *
from asserts import *

init_all()
assertTrue("init_all", True)

scramble_cube(1)
assertTrue("scramble_cube", True)

scan_cube(False)
# verify all facelets have been seen
for i in cube.faces() :
    for j in cube.facelets() :
        assertEqual("face {} facelet {} is RGB white".format(i, j), cu.RGB_WHITE, cube.facelet_rgb(i, j))
        assertEqual("face {} facelet {} is color black".format(i, j), Color.BLACK, cube.facelet(i, j))

