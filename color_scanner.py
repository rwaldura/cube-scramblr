#
# Color scanning logic.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print, wait, StopWatch

import cube, turntable, flip_arm, scan_arm
import color_utils as cu

##############################################################################
# Scan an entire face of the cube, starting with the center facelet.
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    face_color = scan_cube_face_center(face_num)
    cube.set_center_rgb(face_num, face_color)
    print("face", face_num, "may be", cu.rgb2str(face_color))

    scan_cube_face_edges(face_num)
    
    scan_arm.reset()
    turntable.reset()   # re-align the table, due to accumulated errors

    return facelets

##############################################################################
# Scan the center facelet, return its color.
# Bring arm to center, and read the color of the center facelet
def scan_cube_face_center(face_num) :
    scan_arm.move_center()
    return scan_arm.read_rgb()

##############################################################################
# Read each facelet, edges and corners: rotate the table by a entire turn, 
# reading all colors under the scanning head (color sensor) as we go.
#
# This will require some solid post-processing to isolate distinct 
# facelet colors.
def scan_cube_face_edges(face_num) :
    scan_arm.move_edge()

    # rotate cube
    for i in range(8) :
        # if (i % 2 == 0) :
            # scan_arm.move_edge()
        # else :
            # scan_arm.move_corner()

        # read color underneath sensor
        rgb = scan_arm.read_rgb()
        cube.set_facelet_rgb(face_num, i+1, rgb)
        # print("face", face_num, "facelet", i+1, "may be", cu.rgb2str(rgb))

        if (i < 7) :
            turntable.next_facelet()
            # pause()

    return face_colors
