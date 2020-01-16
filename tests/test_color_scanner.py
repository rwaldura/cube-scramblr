#
# Unit test.
#

from color_scanner import *
from asserts import *

init()
assertTrue("init", True)

scan_cube_face_center(1)
assertEqual("scan_cube_face_center", {'r':  0, 'g':  0, 'b':  0}, cube.center_rgb(0))
assertEqual("scan_cube_face_center", {'r':100, 'g':100, 'b':100}, cube.center_rgb(1))
