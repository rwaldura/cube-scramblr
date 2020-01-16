#
# Unit test.
#

from color_scanner import *
from asserts import *

init()
assertTrue("init", True)


scan_cube_face_center(1)

# negative test
assertEqual("scan_cube_face_center 1", {'r':  0, 'g':  0, 'b':  0}, cube.center_rgb(0))
assertEqual("scan_cube_face_center 2", Color.BLACK, cube.center(0))

assertEqual("scan_cube_face_center 3", {'r':100, 'g':100, 'b':100}, cube.center_rgb(1))
# scanner doesn't map colors
assertEqual("scan_cube_face_center 4", Color.BLACK, cube.center(1))


scan_cube_face_edges(2)

# negative test
assertEqual("scan_cube_face_edges 1", {'r':  0, 'g':  0, 'b':  0}, cube.facelet_rgb(3, 1))
assertEqual("scan_cube_face_edges 2", Color.BLACK, cube.facelet(3, 1))

for i in range(1, 9) : 
    assertEqual("scan_cube_face_edges 3", {'r':100, 'g':100, 'b':100}, cube.facelet_rgb(2, i))
    # scanner doesn't map colors
    assertEqual("scan_cube_face_edges 4", Color.BLACK, cube.facelet(2, i))


scan_cube_face(4)

for i in range(0, 9) : 
    assertEqual("scan_cube_face", {'r':100, 'g':100, 'b':100}, cube.facelet_rgb(4, i))

