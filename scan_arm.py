#
# The scanning arm reads cube face colors.
# It uses a motor on port C, and a color sensor on port 2.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import print, wait, StopWatch

##############################################################################
# globals and constants

# "C" motor moves the scanning arm
scan_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
scan_max_angle = -1
scan_speed = 50
scan_edge_angle = 10

# color sensor #2, to scan the cube
scan_sensor = ColorSensor(Port.S2)

##############################################################################
def init() :
    print("initializing scanning arm...")

    scan_motor.run_until_stalled(-scan_speed)
    scan_motor.reset_angle(0)
    print("zero found on scanning arm")

    scan_motor.run_until_stalled(+scan_speed)
    scan_max_angle = scan_motor.angle()
    print("max angle for scanning arm", scan_max_angle)

    # scan_max_angle is where we're looking at the center of the cube;
    # (scan_max_angle - scan_edge_angle) lets us look at the edge

    reset()

##############################################################################
def reset() :
    _move(0)

##############################################################################
# Move the scanning arm TO the given angle
def _move(angle) :
    scan_motor.run_target(scan_speed, angle, Stop.BRAKE)

##############################################################################
# Move the scanning arm to 
def move_edge(angle) :
    _move(scan_max_angle - scan_edge_angle)

##############################################################################
# Move the scanning arm to 
def move_center(angle) :
    _move(scan_max_angle)

##############################################################################
# Read the color underneath the sensor
def read_color() :
    return scan_sensor.read_color()
