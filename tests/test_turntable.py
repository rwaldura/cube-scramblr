#
# Unit test.
#

from turntable import *
from asserts import *

init()
assertEqual("init", 0, table_motor.angle())

rotate(90)
assertEqual("rotate", 90, table_motor.angle())

reset()
assertEqual("reset", 0, table_motor.angle())
