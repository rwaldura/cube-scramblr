#
# The flipping arm is used to "flip" or "tilt": the cube: tumble it by a
# quarter turn. It uses a large motor on port A.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.ev3devices import (Motor)
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import print, wait, StopWatch

##############################################################################
# globals and constants

# "A" motor flips arm
flip_motor = Motor(Port.A)
flip_max_angle = 200
flip_hold_angle = 120
flip_min_angle = 0
flip_speed = 300

##############################################################################
def init() :
    print("initializing flipping arm...")

    # bring it to its lowest position
    flip_motor.run_until_stalled(-flip_speed)
    flip_motor.reset_angle(0)
    print("zero found on flipping arm")

##############################################################################
def reset() :
    print("resetting flipping arm")

    if (flip_motor.angle() > flip_min_angle) :
        _move(flip_min_angle)

##############################################################################
# Move the flipping arm to an angle that blocks the cube in place,
# and lets us rotate its bottom layer.
def hold() :
    _move(flip_hold_angle, Stop.HOLD)

##############################################################################
# Move the flipping arm TO the given angle.
# (internal method, hence the underscore prefix)
def _move(angle, stop = Stop.COAST) :
    flip_motor.run_target(flip_speed, angle, stop)

##############################################################################
# Flip the cube, i.e. tilt it by a quarter-turn
def flip_cube(n = 1) :
    print("flipping cube:", n)

    hold()

    for i in range(n) :
        _move(flip_max_angle)
        hold()
