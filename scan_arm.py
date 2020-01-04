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
scan_center_angle = 250 
scan_edge_angle = scan_center_angle - 60

# color sensor #2, to scan the cube
scan_sensor = ColorSensor(Port.S2)

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
# Move the arm to scan the center facelet
def move_center() :
    _move(scan_center_angle)

##############################################################################
# Read the color underneath the sensor
def read_color() :
    return scan_sensor.color()
