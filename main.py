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

##############################################################################
# globals and constants

# total number of scrambling moves: flips and rotations
scrambling_max = 10

# "A" motor flips arm
flip_motor = Motor(Port.A)
flip_max_angle = 200
flip_hold_angle = 120
flip_min_angle = 0
flip_speed = 300

# "B" motor rotates the turntable
table_motor = Motor(Port.B, Direction.CLOCKWISE, [12, 36])
table_speed = 90
table_max_speed = 2 * table_speed
table_motor.set_run_settings(table_speed, 2 * table_speed)
table_epsilon = 20

# "C" motor moves the scanning arm
scan_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
scan_max_angle = -1
scan_speed = 100

# color sensor #1, to align the turntable
table_sensor = ColorSensor(Port.S1)

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

    init_flip_arm()
    init_turntable()
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
def init_turntable() :
    print("initializing turntable...")

    # go through a full rotation, seeking to maximize the reflection 
    # returned by the sensor
    table_motor.run(table_speed / 2)

    # record the reflection for each angle
    reflect = [0] * 400

    while (table_motor.angle() < 360) :
        wait(10) # sample 10 times per second
        r = table_sensor.reflection()
        a = table_motor.angle()
        # print("reflect", r, "at angle", a)
        reflect[a] = r

    table_motor.stop()

    # find the highest reflection angle
    max_angle = reflect.index(max(reflect))
    print("found highest reflection", reflect[max_angle], "at angle", max_angle)

    # correct to get a straight angle on the table
    angle_reflection_epsilon = 7

    table_motor.run_target(table_speed, max_angle + angle_reflection_epsilon, Stop.HOLD)
    table_motor.reset_angle(0)

##############################################################################
def init_flip_arm() :
    print("initializing flipping arm...")

    # bring it to its lowest position
    flip_motor.run_until_stalled(-flip_speed)
    flip_motor.reset_angle(0)
    print("zero found on flipping arm")

##############################################################################
def reset_flip_arm() :
    print("resetting flipping arm")

    if (flip_motor.angle() > flip_min_angle) :
        move_flip_arm(flip_min_angle)

##############################################################################
def reset_scan_arm() :
    move_scan_arm(0)

##############################################################################
# Rotate the turntable BY the given angle
def rotate_table(angle, speed = table_speed) :
    table_motor.run_angle(speed, angle, Stop.HOLD)

##############################################################################
# Move the flipping arm TO the given angle
def move_flip_arm(angle) :
    flip_motor.run_target(flip_speed, angle, Stop.HOLD)

##############################################################################
# Move the scanning arm TO the given angle
def move_scan_arm(angle) :
    scan_motor.run_target(scan_speed, angle, Stop.HOLD)

##############################################################################
# Flip the cube, i.e. tilt it by a quarter-turn
def flip_cube(n = 1) :
    print("flipping cube:", n)

    move_flip_arm(flip_hold_angle)

    for i in range(n) :
        move_arm(flip_max_angle)
        move_arm(flip_hold_angle)

##############################################################################
# Rotate the bottom layer of the cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube_layer(n = 1) :
    print("rotating cube bottom layer:", n)
    flip_motor.run_target(flip_speed, flip_hold_angle)
    rotate_cube(n, True, False)

##############################################################################
# Rotate the entire cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube(n = 1, correct = False, flip_reset = True) :
    if (flip_reset) : 
        reset_flipping_arm()

    print("rotating cube:", n)

    angle = 90 * n
    print("rotating angle:", angle)
    if (angle == 0) : 
        return

    # because the cube is not snug on the turntable, we must
    # overcorrect a bit to get the cube to align correctly
    if (correct) :
        if (n > 0) : 
            angle += table_epsilon
        else :
            angle -= table_epsilon

    print("corrected angle:", angle)
    rotate_table(angle)

    if (correct) :
        if (n > 0) : 
            angle = -table_epsilon
        else :
            angle = +table_epsilon

        print("re-corrected angle:", angle)
        rotate_table(angle)

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
        flip_cube(r)

    # show off scrambled cube
    reset_flip_arm()
    rotate_table(6 * 90 + 45, table_max_speed)

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
