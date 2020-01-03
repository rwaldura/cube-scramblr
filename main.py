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
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import random, time

import turntable, flip_arm

##############################################################################
# globals and constants

# total number of scrambling moves: flips and rotations
scrambling_max = 10

# "C" motor moves the scanning arm
scan_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
scan_max_angle = -1
scan_speed = 50

# color sensor #2, to scan the cube
scan_sensor = ColorSensor(Port.S2)

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
    init_scan_arm()

    print("initialized all.")

##############################################################################
def init_scan_arm() :
    print("initializing scanning arm...")

    scan_motor.run_until_stalled(-scan_speed)
    scan_motor.reset_angle(0)
    print("zero found on scanning arm")

    scan_motor.run_until_stalled(+scan_speed)
    scan_max_angle = scan_motor.angle()
    print("max angle for scanning arm", scan_max_angle)

    # scan_max_angle is where we're looking at the center of the cube
    # (scan_max_angle - 10) lets us look at the edge

    reset_scan_arm()

##############################################################################
def reset_scan_arm() :
    move_scan_arm(0)

##############################################################################
# Move the scanning arm TO the given angle
def move_scan_arm(angle) :
    scan_motor.run_target(scan_speed, angle, Stop.BRAKE)

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

    angle = 90 * n
    print("rotating angle:", angle)

    if (angle == 0) : 
        return

    turntable.rotate(angle, correct)

##############################################################################
# Wait until any of the buttons are pressed
def pause() :
    while not any(brick.buttons()):
        wait(100)

##############################################################################
def scramble_cube() :
    for n in range(scrambling_max) :
        r = random.randint(-3, 3)
        print("performing layer rotations", r)
        rotate_cube_layer(r)

        r = random.randint(1, 3)
        print("performing flips", r)
        flip_arm.flip_cube(r)

    # show off scrambled cube
    flip_arm.reset()
    turntable.spin()

##############################################################################
def scan_cube() :
    x = 0

##############################################################################
# main

init_all()

display("insert cube, and")
display("press any button")
pause()

scramble_cube()
scan_cube()
