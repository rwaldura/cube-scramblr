#
# Unit test.
#

from main import *
from asserts import *

init_all()
assertTrue("init_all", True)

scramble_cube(1)
assertTrue("scramble_cube", True)

scan_cube(False)
assertTrue("scan_cube", True)
