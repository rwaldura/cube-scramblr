#!/usr/bin/env pybricks-micropython
#
# The structure, the build, is based off David Gilday's MindCub3r
# at https://www.mindcuber.com/mindcub3r/mindcub3r.html
#
# The language, MicroPython, is documented at
# https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
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

##############################################################################
# globals and constants

# total number of scrambling moves: flips and rotations
scrambling_moves = 10

# cube faces, indexed by color of the central facelet
cube = {}

color2str = { 
    Color.BROWN:"brown", 
    Color.GREEN:"green",
    Color.BLACK:"black",
    Color.WHITE:"white",
    Color.RED:"red",
    Color.BLUE:"blue",
    Color.YELLOW:"yellow" 
    }

##############################################################################
def display(mesg) :
    brick.display.text(mesg)

##############################################################################
def init_all() :
    random.seed(int(time.time()))

    brick.display.clear()
    display("CUBE SCRAMBLER")

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
# Wait until any of the buttons are pressed
def pause() :
    while not any(brick.buttons()):
        wait(100)

##############################################################################
def flip_cube(n = 1, reset_arm = False) :
    flip_arm.flip_cube(n)

    if (reset_arm) : 
        flip_arm.reset()

##############################################################################
def scramble_cube() :
    for n in range(scrambling_moves) :
        r = random.randint(-3, 3)
        print("performing layer rotations", r)
        rotate_cube_layer(r)

        f = random.randint(1, 3)
        print("performing flips", f)
        flip_cube(f)

    # show off scrambled cube
    flip_arm.reset()
    turntable.spin()

##############################################################################
# Visit all 6 faces of the cube, scanning each one.
def scan_cube() :
    for face in range(4) :
        flip_cube(1, True)
        scan_cube_face(face)
        pause()

    rotate_cube()
    flip_cube(1, True)
    scan_cube_face()

    flip_cube(2, True)
    scan_cube_face()

##############################################################################
def scan_cube_face(face_num) :
    print("scanning face", face_num, "...")

    # bring arm to center, and read the color of the center facelet
    scan_arm.move_center()
    face_color = scan_arm.read_color()
    print("current face", face_num, "has color", color2str[face_color])

    facelets = [Color.BLACK] * 8
    cube[face_color] = facelets

    # read each facelet in turn
    for i in range(8) :
        if (i % 2 == 0) :
            scan_arm.move_edge()
        else :
            scan_arm.move_corner()

        facelets[i] = scan_arm.read_color()
        print("facelet", i, "color", color2str[facelets[i]])
        turntable.next_facelet()

    turntable.next_facelet()
    scan_arm.reset()

##############################################################################
# main

init_all()

display("insert cube, and")
display("press any button")
pause()

# scramble_cube()
scan_cube()
