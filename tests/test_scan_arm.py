#
# Unit test.
#

from scan_arm import *
from asserts import *

init()
assertEqual("init", scan_min_angle, scan_motor.angle())

assertEqual("read_rgb", { 'r':0, 'g':0, 'b':0 }, read_rgb())

reset()
assertEqual("reset", scan_min_angle, scan_motor.angle())