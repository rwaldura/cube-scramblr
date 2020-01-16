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
white = {'r':100, 'g':100, 'b':100}
for i in range(6) :
    for j in range(9) :
        assertEqual("face {} facelet {} is RGB white".format(i, j), white, cube.facelet_rgb(i, j))
        assertEqual("face {} facelet {} is color black".format(i, j), Color.BLACK, cube.facelet(i, j))

