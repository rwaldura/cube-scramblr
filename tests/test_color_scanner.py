#
# Unit test.
#

from color_scanner import *
from asserts import *
import color_utils as cu

init()
assertTrue("init", True)


scan_cube_face_center(1)

# negative test
assertEqual("scan_cube_face_center 1", cu.RGB_BLACK, cube.center_rgb(0))
assertEqual("scan_cube_face_center 2", Color.BLACK, cube.center(0))

# positive test
assertEqual("scan_cube_face_center 3", cu.RGB_WHITE, cube.center_rgb(1))
# scanner doesn't map colors
assertEqual("scan_cube_face_center 4", Color.BLACK, cube.center(1))


scan_cube_face_edges(2)

# negative test
assertEqual("scan_cube_face_edges 1", cu.RGB_BLACK, cube.facelet_rgb(3, 1))
assertEqual("scan_cube_face_edges 2", Color.BLACK, cube.facelet(3, 1))

for i in range(1, 9) : 
    assertEqual("scan_cube_face_edges 3", cu.RGB_WHITE, cube.facelet_rgb(2, i))
    # scanner doesn't map colors
    assertEqual("scan_cube_face_edges 4", Color.BLACK, cube.facelet(2, i))


scan_cube_face(4)

for i in range(0, 9) : 
    assertEqual("scan_cube_face 5", cu.RGB_WHITE, cube.facelet_rgb(4, i))

# verify only face 4 was changed
for i in range(0, 9) : 
    assertEqual("scan_cube_face 6", cu.RGB_BLACK, cube.facelet_rgb(5, i))
