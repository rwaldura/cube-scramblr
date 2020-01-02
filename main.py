#!/usr/bin/env pybricks-micropython
#
# The structure, the build, is based off David Gilday's MindCub3r
# at https://www.mindcuber.com/mindcub3r/mindcub3r.html
#
# The language, MicroPython, is documented at
# https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
#
# by Ren Waldura ren+lego@waldura.org, 2019
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
arm_motor = Motor(Port.A)
arm_max_angle = 200
arm_hold_angle = 120
arm_min_angle = 5
arm_speed = 256

# "B" motor rotates the turntable
table_motor = Motor(Port.B, Direction.CLOCKWISE, [12, 36])
table_speed = 90
table_motor.set_run_settings(table_speed, 2 * table_speed)
table_epsilon = 20

# color sensor, used to align the turntable
table_sensor = ColorSensor(Port.S1)

##############################################################################
def display(mesg) :
    brick.display.text(mesg)

##############################################################################
def init_all() :
    random.seed(int(time.time()))

    brick.display.clear()
    display("CUBE SCRAMBLER")

    init_flipping_arm()
    init_turntable()

    print("initialized all.")

##############################################################################
def init_turntable() :
    # go through a full rotation, seeking to maximize the reflection 
    # returned by the sensor
    table_motor.run(table_speed / 2)

    # record the reflection for each angle
    reflect = [0] * 400

    while (table_motor.angle() < 360) :
        r = table_sensor.reflection()
        a = table_motor.angle()
        print("reflect", r, "at angle", a)
        reflect[a] = r

    table_motor.stop()

    # find the highest reflection angle
    max_angle = reflect.index(max(reflect))
    print("found highest reflection", reflect[max_angle], "at angle", max_angle)

    table_motor.run_target(table_speed, max_angle + 5, Stop.HOLD)
    table_motor.reset_angle(0)

##############################################################################
def init_flipping_arm() :
    print("initializing flipping arm...")

    # bring it to its lowest position
    arm_motor.run_until_stalled(-arm_speed)
    arm_motor.reset_angle(0)
    print("zero found")

##############################################################################
def reset_arm() :
    print("resetting flipping arm")

    if (arm_motor.angle() > arm_min_angle) :
        move_arm(arm_min_angle)

##############################################################################
# Rotate the turntable BY the given angle
def rotate_table(angle) :
    table_motor.run_angle(table_speed, angle, Stop.HOLD)

##############################################################################
# Move the flipping arm TO the given angle
def move_arm(angle) :
    arm_motor.run_target(arm_speed, angle)

##############################################################################
# Flip the cube, i.e. tilt it by a quarter-turn
def flip_cube(n = 1) :
    print("flipping cube:", n)

    move_arm(arm_hold_angle)

    for i in range(n) :
        move_arm(arm_max_angle)
        move_arm(arm_hold_angle)

##############################################################################
# Rotate the bottom layer of the cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube_layer(n = 1) :
    print("rotating cube bottom layer:", n)
    arm_motor.run_target(arm_speed, arm_hold_angle)
    rotate_cube(n, True, False)

##############################################################################
# Rotate the entire cube
# n is the number of quarter-turns: positive for clockwise, negative for 
# counter-clockwise
def rotate_cube(n = 1, correct = False, arm_reset = True) :
    if (arm_reset) : 
        reset_arm()

    print("rotating cube:", n)

    angle = 90 * n
    if (angle == 0) : 
        return
    print("rotating angle:", angle)

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
# main

init_all()

display("insert cube, and")
display("press any button")
pause()

for n in range(scrambling_max) :
    r = random.randint(-3, 3)
    print("performing layer rotations", r)
    rotate_cube_layer(r)

    r = random.randint(1, 3)
    print("performing flips", r)
    flip_cube(r)

rotate_cube(4)
