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
from pybricks.parameters import Button
from pybricks.tools import print, wait

import sys
sys.path.append('src')

from main import * 

##############################################################################
# main
init_all()

display("CUBE SCRAMBL3R")
display("Insert cube")
display("Press UP button to")
display("scramble, DOWN button")
display("to resolve")
brick.sound.beep()

do_scramble = False
do_resolve = False

while not any(brick.buttons()):
    wait(100)
    if (Button.UP in brick.buttons()) :
        do_scramble = True
        break
    elif (Button.DOWN in brick.buttons()) :
        do_resolve = True
        break
    elif (Button.CENTER in brick.buttons()) :
        do_calibrate = True
        break

if (do_scramble) :
    scramble_cube()
elif (do_resolve) :
    scan_cube(False)
    map_cube_colors(True)
elif (do_calibrate) :        
    calibrate_color_sensor()
else :
    pass

