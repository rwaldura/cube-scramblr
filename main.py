#!/usr/bin/env pybricks-micropython
#
# The structure, the build, is based off David Gilday's MindCub3r
# at https://www.mindcuber.com/mindcub3r/mindcub3r.html
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks import ev3brick as brick 
from pybricks.parameters import (Port, Stop, Direction, Color)
from pybricks.tools import print, wait, StopWatch

import random, time

import turntable, flip_arm, scan_arm
import color_utils as cu

##############################################################################
# globals and constants

# total number of scrambling moves: flips and rotations
scrambling_moves = 10

# cube faces, indexed by color of the central facelet
cube = [None] * (1 + max(cu.CUBE_COLORS))

##############################################################################
def display(mesg) :
    brick.display.text(mesg)

##############################################################################
# Wait until any of the buttons are pressed
def pause() :
    display("press any button")
    brick.sound.beep()
    while not any(brick.buttons()):
        wait(200)

##############################################################################
def init_all() :
    random.seed(int(time.time()))

    brick.display.clear()
    display("CUBE SCRAMBL3R")

    flip_arm.init()
    turntable.init()
    scan_arm.init()

    print("initialized all.")

##############################################################################
# Rotate the bottom layer of the cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube_layer(n = 1) :
    print("rotating cube bottom layer:", n)
    flip_arm.hold()
    rotate_cube(n, True, False)

##############################################################################
# Rotate the entire cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube(n = 1, correct = False, flip_reset = True) :
    if (flip_reset) : 
        flip_arm.reset()

    print("rotating cube:", n)

    turntable.rotate(90 * n, correct)

##############################################################################
def flip_cube(n = 1, reset_arm = True) :
    flip_arm.flip_cube(n, reset_arm)

##############################################################################
def scramble_cube() :
    for n in range(scrambling_moves) :
        r = random.randint(-3, 3)
        print("performing layer rotations", r)
        rotate_cube_layer(r)

        f = random.randint(1, 3)
        print("performing flips", f)
        flip_cube(f, False)

    # show off scrambled cube
    flip_arm.reset()
    turntable.free_spin()

##############################################################################
# Visit all 6 faces of the cube, scanning each one.
def scan_cube(debug = False) :
    for face in range(6) :
        if (face == 3) :
            rotate_cube() # quarter turn

        if (face == 5) :
            flip_cube(2)
        elif (face > 0) :
            flip_cube()

        scan_cube_face(face)

        if (debug) :
            pause()

##############################################################################
# Scan an entire face of the cube, starting with the center facelet.
# We also populate the cube[] array with the facelet colors.
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    face_color = scan_cube_face_center(face_num)
    print("current face", face_num, "has color:", cu.color2str(face_color))

    cube[face_color] = scan_cube_face_edges(face_num)

    scan_arm.reset()

    return face_color

##############################################################################
# Scan the center facelet, return its color.
# Bring arm to center, and read the color of the center facelet
def scan_cube_face_center(face_num) :
    scan_arm.move_center()
    return scan_arm.read_color()

##############################################################################
# Read each facelet: rotate the table by a entire turn, reading all
# colors under the scanning head (color sensor) as we go.
#
# This will require some solid post-processing to isolate distinct 
# facelet colors. 
def scan_cube_face_edges(face_num) :
    scan_arm.move_edge()

    # start rotating the cube
    turntable.spin()
    spin_colors = [None] * 100

    # while cube is rotating
    while (turntable.speed() > 0) :
        wait(100) # give it time to move
        # read color underneath sensor
        rgb = scan_arm.read_rgb_avg(1)
        spin_colors.append(rgb)

    print("read", len(spin_colors), "edge color samples during full spin")
    return spin_colors

def print_facelets(face_num, face_color, facelet, facelets) :
    print("face", face_num, cu.color2str(face_color), 
            "facelet", facelet, "color", cu.color2str(facelets[facelet])) 
    facelets_str = ""
    for f in (facelets) :
        facelets_str += cu.color2str(f) + " "
    print("all facelets:", facelets_str)

##############################################################################
# Calibrate the color sensor; only used during development
def calibrate_color_sensor() :
    while (True) :
        scan_arm.move_center()
        rgb = scan_arm.read_rgb_avg()
        print("center color", rgb['r'], rgb['g'], rgb['b'])
        color = scan_arm.read_color()
        print("center color mapped to", cu.color2str(color))

        scan_arm.move_edge()
        rgb = scan_arm.read_rgb_avg()
        print("edge color", rgb['r'], rgb['g'], rgb['b'])
        color = scan_arm.read_color()
        print("edge color mapped to", cu.color2str(color))

        scan_arm.reset()
        pause()

##############################################################################
# main

init_all()

display("insert cube")
pause()

# scramble_cube()
scan_cube(False)
# flip_cube(5)
        
# calibrate_color_sensor()
