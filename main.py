#!/usr/bin/env pybricks-micropython

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

# motor on port A for flips
flip_motor = Motor(Port.A)
flip_motor_max_angle = 200
flip_motor_hold_angle = 105
flip_motor_min_angle = 15
flip_motor_speed = 80
flip_motor_power = 30 # percent of total torque

# motor on port B for rotations
rot_motor = Motor(Port.B, Direction.CLOCKWISE, [12, 36])
rot_motor_speed = 90

##############################################################################
def display(mesg) :
    brick.display.text(mesg)

##############################################################################
def init_all() :
    random.seed(int(time.time()))

    brick.display.clear()
    display("CUBE SCRAMBLER")

    init_flipping_arm()
    #init_rotating_shelf()

    print("initialized all.")

##############################################################################
def init_rotating_shelf() :
    # reset rotation angle to zero
    rot_motor.run_angle(90, 0)
    rot_motor.reset_angle(0)

##############################################################################
def init_flipping_arm() :
    print("initializing flipping arm...")

    # bring it to its lowest position
    flip_motor.run_until_stalled(-flip_motor_speed)
    flip_motor.reset_angle(0)
    print("zero found")

    # # bring it to its highest position
    # flip_motor.run_until_stalled(+flip_motor_speed, Stop.COAST, flip_motor_power)
    # max = flip_motor.angle()
    # print("max angle", max)

    # # reset
    # flip_motor.run_target(flip_motor_speed, 0)

    # return max

##############################################################################
def reset_arm() :
    print("resetting flipping arm")

    if (flip_motor.angle() > flip_motor_min_angle) :
        flip_motor.run_target(flip_motor_speed, flip_motor_min_angle)

##############################################################################
def flip_cube(n = 1) :
    print("flipping cube:", n)

    reset_arm()

    for i in range(n) :
        flip_motor.run_target(flip_motor_speed, flip_motor_max_angle)
        flip_motor.run_target(flip_motor_speed, flip_motor_min_angle)

##############################################################################
# Rotate the bottom layer of the cube
# n is the number of rotations: positive for clockwise, negative for counter-clockwise
def rotate_cube_layer(n = 1) :
    print("rotating cube bottom layer:", n)
    flip_motor.run_target(flip_motor_speed, flip_motor_hold_angle)
    rotate_cube(n, True, False)

##############################################################################
# Rotate the entire cube
# n is the number of rotations: positive for clockwise, negative for counter-clockwise
def rotate_cube(n = 1, correct = False, arm_reset = True) :
    if (arm_reset) : 
        reset_arm()

    print("rotating cube:", n)
    angle = 90 * n

    # because the cube is not snug on the shelf, we must
    # overshoot a bit to get the cube to align correctly
    if (correct) :
        if (n > 0) : 
            angle += 10
        else :
            angle -= 10

    rot_motor.run_angle(rot_motor_speed, angle)

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

rotate_cube(2)
flip_cube(2)
rotate_cube_layer(1)
reset_arm()

# for n in range(5) :
#     r = random.randint(-3, 3)
#     print("performing rotations", r)
#     rotate_cube(r)
#     print("performing flips", r)
#     flip_cube(r)
