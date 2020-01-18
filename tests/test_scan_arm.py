#
# Unit test.
#

from scan_arm import *
from asserts import *

init()
assertEqual("init", scan_min_angle, scan_motor.angle())

assertEqual("read_rgb", color_utils.RGB_WHITE, read_rgb())

reset()
assertEqual("reset", scan_min_angle, scan_motor.angle())