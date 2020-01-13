#!/usr/bin/env pybricks-micropython
#
# The structure, the build, is based off David Gilday's MindCub3r
# at https://www.mindcuber.com/mindcub3r/mindcub3r.html
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import (Color)
from pybricks.tools import print, wait, StopWatch

import random, time

import turntable, flip_arm, scan_arm
import color_utils as cu

##############################################################################
# Scan an entire face of the cube, starting with the center facelet.
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    face_color = scan_cube_face_center(face_num)
    print("face", face_num, "may be", cu.rgb2str(face_color))

    facelet_colors = scan_cube_face_edges(face_num)
    facelets = [face_color] + facelet_colors
    print("face", face_num, "colors:", print_facelets(facelets))

    # re-align the table, due to accumulated errors
    scan_arm.reset()
    turntable.reset(False)

    return facelets

##############################################################################
# Scan the center facelet, return its color.
# Bring arm to center, and read the color of the center facelet
def scan_cube_face_center(face_num) :
    scan_arm.move_center()
    return scan_arm.read_rgb()

##############################################################################
# Read each facelet: rotate the table by a entire turn, reading all
# colors under the scanning head (color sensor) as we go.
#
# This will require some solid post-processing to isolate distinct 
# facelet colors. 
def scan_cube_face_edges(face_num) :
    face_colors = [()] * 9

    scan_arm.move_edge()

    # rotate cube
    for i in range(9) :
        # if (i % 2 == 0) :
            # scan_arm.move_edge()
        # else :
            # scan_arm.move_corner()

        # read color underneath sensor
        rgb = scan_arm.read_rgb()
        face_colors[i] = rgb

        print("face", face_num, "facelet", i, "may be", cu.rgb2str(rgb))

        if (i < 8) :
            turntable.rotate(45)
            # pause()

    return face_colors

##############################################################################
def print_facelets(facelets) :
    facelets_str = ""
    for f in (facelets) :
        facelets_str += cu.rgb2str(f) + " "
    return facelets_str
