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

##############################################################################
# globals and constants

# "C" motor moves the scanning arm
scan_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
scan_speed = 100
scan_center_angle = 260 # positions the head on top of center facelet
scan_edge_angle = scan_center_angle - 60
scan_corner_angle = scan_center_angle - 80

# color sensor #2, to scan the cube
scan_sensor = ColorSensor(Port.S2)
scan_sensor_max_attempts = 5
scan_read_epsilon = 2 # to re-try color reads

##############################################################################
def init() :
    print("initializing scanning arm...")

    scan_motor.run_until_stalled(-scan_speed)
    scan_motor.reset_angle(0)
    print("zero found on scanning arm")

##############################################################################
def reset() :
    _move(0)

##############################################################################
# Move the scanning arm TO the given angle
def _move(angle) :
    print("moving scanning arm to", angle)
    scan_motor.run_target(scan_speed, angle, Stop.BRAKE)

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
# Read the color underneath the sensor
def read_color() :
    color = None
    attempts = 0
    
    while (True) :
        color = scan_sensor.color()
        attempts += 1

        if (color != None) :
            break # success
        elif (attempts >= scan_sensor_max_attempts) :
            print("no color read after multiple attempts, giving up")
            break
        else : # try again
            print("no color read, trying again")

            epsilon = 0
            if (attempts % 2 == 0) :
                epsilon = (-1) * attempts * scan_read_epsilon
            else :
                epsilon = attempts * scan_read_epsilon

            # adjust scanning head by a small amount
            _move_offset(epsilon)

    return color
