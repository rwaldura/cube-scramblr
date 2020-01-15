#
# Unit test.
#

from flip_arm import *
from asserts import *

init()
assertEqual("init", 0, flip_motor.angle())

hold()
assertEqual("hold", flip_hold_angle, flip_motor.angle())

reset()
assertEqual("reset", 0, flip_motor.angle())

flip_cube(1, False)
assertEqual("flip1", flip_hold_angle, flip_motor.angle())

flip_cube(2, True)
assertEqual("flip2", 0, flip_motor.angle())
