#
# Color scanning logic.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print, wait

import cube, turntable, flip_arm, scan_arm
import color_utils as cu

##############################################################################
def init() :
    pass

##############################################################################
# Scan an entire face of the cube, starting with the center facelet.
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    scan_cube_face_center(face_num)
    scan_cube_face_edges(face_num)
    
    scan_arm.reset()
    turntable.reset()   # re-align the table, due to accumulated errors

##############################################################################
# Scan the center facelet, return its color.
# Bring arm to center, and read the color of the center facelet
def scan_cube_face_center(face_num) :
    scan_arm.move_center()
    rgb = scan_arm.read_rgb()
    cube.set_center_rgb(face_num, rgb)
    print("face", face_num, "may be", cu.rgb2str(cube.center_rgb(face_num)))

##############################################################################
# Read each facelet, edges and corners: rotate the table by a entire turn, 
# reading all colors under the scanning head (color sensor) as we go.
#
# This will require some solid post-processing to isolate distinct 
# facelet colors.
def scan_cube_face_edges(face_num) :
    scan_arm.move_edge()

    # for each facelet
    for i in range(1, 9) : # 1..8
        # if (i % 2 == 0) :
            # scan_arm.move_edge()
        # else :
            # scan_arm.move_corner()

        # read color underneath sensor
        rgb = scan_arm.read_rgb()
        cube.set_facelet_rgb(face_num, i, rgb)
        print("face", face_num, "facelet", i, "may be", cu.rgb2str(rgb))

        if (i < 8) :
            turntable.next_facelet()
            # pause()
