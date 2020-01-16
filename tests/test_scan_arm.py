#
# Unit test.
#

from scan_arm import *
from asserts import *

init()
assertEqual("init", scan_min_angle, scan_motor.angle())

assertEqual("read_rgb", { 'r':100, 'g':100, 'b':100 }, read_rgb())

reset()
assertEqual("reset", scan_min_angle, scan_motor.angle())