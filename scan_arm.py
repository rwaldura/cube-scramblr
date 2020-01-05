#
# The scanning arm reads cube face colors.
# It uses a motor on port C, and a color sensor on port 2.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import (Port, Stop, Direction, Color)
from pybricks.tools import print, wait, StopWatch

import color_utils

##############################################################################
# globals and constants

# "C" motor moves the scanning arm
scan_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
scan_speed = 100
scan_center_angle = 250 # positions the head on top of center facelet
scan_min_angle = 130
scan_edge_angle = scan_center_angle - 50
scan_corner_angle = scan_center_angle - 90

# color sensor #2, to scan the cube
scan_sensor = ColorSensor(Port.S2)
scan_sensor_max_attempts = 10
scan_read_epsilon = 5 # to re-try color reads

##############################################################################
def init() :
    print("initializing scanning arm...")

    scan_motor.run_until_stalled(-scan_speed)
    scan_motor.reset_angle(0)
    print("zero found on scanning arm")

    reset()

##############################################################################
def reset() :
    _move(scan_min_angle)

##############################################################################
# Move the scanning arm TO the given angle
def _move(angle) :
    print("moving scanning arm to", angle)
    scan_motor.run_target(scan_speed, angle)

##############################################################################
# Move the scanning arm BY the given angle, expected to be small
def _offset(angle) :
    print("moving scanning arm by", angle)
    scan_motor.run_angle(scan_speed / 2, angle)

##############################################################################
# Move the arm to scan an edge facelet
def move_edge() :
    _move(scan_edge_angle)

##############################################################################
# Move the arm to scan a corner facelet
def move_corner() :
    _move(scan_corner_angle)

##############################################################################
# Move the arm to scan the center facelet
def move_center() :
    _move(scan_center_angle)

##############################################################################
# Sample color 5 times, pick the average
def _read_color_avg() :
    num_samples = 5

    color_samples = [0] * num_samples
    color_samples_rgb = { 
        'r' : [0] * num_samples,
        'g' : [0] * num_samples,
        'b' : [0] * num_samples 
    }

    for i in range(num_samples) :
        color_sample = scan_sensor.color()
        print("read #", i, "color=", color_sample)
        color_samples[i] = color_sample
        
        (r,g,b) = scan_sensor.rgb()
        color_samples_rgb['r'][i] = r
        color_samples_rgb['g'][i] = g
        color_samples_rgb['b'][i] = b        

    avg_color = round(sum(color_samples) / num_samples)
    print("average color", avg_color)
    return avg_color

    avg_color_rgb = {
        'r' : sum(color_samples['r']) / num_samples,
        'g' : sum(color_samples['g']) / num_samples,
        'b' : sum(color_samples['b']) / num_samples
    }

    return _get_color(avg_color)

##############################################################################
# Return a Color constant from a R/G/B color dict.
def _get_color(color) :
    return Color.BLACK

##############################################################################
# Read the color underneath the sensor
def read_color() :
    color = None
    attempts = 0

    while (True) :
        color = _read_color_avg()
    
        attempts += 1

        if (color != None) :
            break # success
        elif (attempts >= scan_sensor_max_attempts) :
            print("no color read after multiple attempts, giving up")
            break
        else :
            print("no color read, trying again; attempt", attempts)

            # adjust scanning head, and try again
            epsilon = attempts * scan_read_epsilon
            if (attempts % 2 == 0) :
                epsilon = -epsilon
            _offset(epsilon)

    return color
