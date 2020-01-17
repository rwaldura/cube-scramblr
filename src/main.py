#
# The structure, the build, is based off David Gilday's MindCub3r
# at https://www.mindcuber.com/mindcub3r/mindcub3r.html
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks import ev3brick as brick 
from pybricks.parameters import Button, Color
from pybricks.tools import print, wait

import random, time

import cube, turntable, flip_arm, scan_arm, color_scanner
import color_utils as cu

##############################################################################
# globals and constants

# total number of scrambling moves: flips and rotations
default_scrambling_moves = 10

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
def scramble_cube(moves = default_scrambling_moves) :
    for n in range(moves) :
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
# Populate the "cube" data structure.
def scan_cube(debug = False) :
    for face in range(6) :
        if (face == 4) :
            rotate_cube() # quarter turn
        if (face == 5) :
            flip_cube(2)
        elif (face > 0) :
            flip_cube()

        color_scanner.scan_cube_face(face)

        if (debug) :
            print(cube.to_str())
            pause()

##############################################################################
# We've scanned the entire cube, and read RGB samples for each facelet.
# Now map each facelet to an actual color constant. 
def map_cube_colors() :    
    # identify the white face first
    white_face = color_mapper.find_white_face()

    # the opposite of the white face is the yellow face

    return

##############################################################################
# Calibrate the color sensor; only used during development
def calibrate_color_sensor() :
    while (True) :
        scan_arm.move_center()
        rgb = scan_arm.read_rgb()
        print("center color", rgb['r'], rgb['g'], rgb['b'])
        color = scan_arm.read_color()
        print("center color mapped to", cu.color2str(color))

        scan_arm.move_edge()
        rgb = scan_arm.read_rgb()
        print("edge color", rgb['r'], rgb['g'], rgb['b'])
        color = scan_arm.read_color()
        print("edge color mapped to", cu.color2str(color))

        scan_arm.reset()
        pause()
