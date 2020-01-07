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
def flip_cube(n, reset_arm = True) :
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
    turntable.spin()

##############################################################################
# Visit all 6 faces of the cube, scanning each one.
def scan_cube(debug = False) :
    for face in range(4) :
        flip_cube(1, True)
        scan_cube_face(face)
        if (debug) :
            pause()

    rotate_cube()
    flip_cube(1, True)
    scan_cube_face(4)

    if (debug) :
        pause()

    flip_cube(2, True)
    scan_cube_face(5)

##############################################################################
# Scan an entire face of the cube, starting with the center facelet.
# We also populate the cube[] array with the facelet colors.
# @todo this needs work!
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    # bring arm to center, and read the color of the center facelet
    scan_arm.move_center()
    face_color = scan_arm.read_color()
    print("current face", face_num, "has color:", cu.color2str(face_color))

    facelets = [0] * 8
    cube[face_color] = facelets

    # read each facelet in turn
    for facelet in range(8) :
        if (facelet > 0) :
            turntable.next_facelet()

        if (facelet % 2 == 0) :
            scan_arm.move_edge()
        else :
            scan_arm.move_corner()

        facelets[facelet] = scan_arm.read_color()
        print_facelets(face_num, face_color, facelet, facelets)
        pause()

    turntable.next_facelet()
    scan_arm.reset()

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
        rgb = scan_arm._read_rgb_avg()
        print("center color", rgb['r'], rgb['g'], rgb['b'])
        color = scan_arm.read_color()
        print("center color mapped to", cu.color2str(color))

        scan_arm.move_edge()
        rgb = scan_arm._read_rgb_avg()
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
