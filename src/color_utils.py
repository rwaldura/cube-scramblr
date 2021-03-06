#
# Utility functions to deal with EV3 colors.
# The EV3 color sensor does not reliably recognize cube colors.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color
from pybricks.tools import print

##############################################################################
# globals and constants

COLOR_NAMES = (
    None,       # 0 - None
    "black",    # 1 - Color.BLACK
    "blue",     # 2 - Color.BLUE
    "green",    # 3 - Color.GREEN
    "yellow",   # 4 - Color.YELLOW
    "red",      # 5 - Color.RED
    "white",    # 6 - Color.WHITE
    "brown",    # 7 - Color.BROWN
    "orange",   # 8 - Color.ORANGE
    "purple"    # 9 - Color.PURPLE
)

RGB_BLACK  = { 'r':  0, 'g':  0, 'b':  0 }
RGB_RED    = { 'r':100, 'g':  0, 'b':  0 }
RGB_GREEN  = { 'r':  0, 'g':100, 'b':  0 }
RGB_BLUE   = { 'r':  0, 'g':  0, 'b':100 }
RGB_WHITE  = { 'r':100, 'g':100, 'b':100 }
RGB_GREY   = { 'r': 50, 'g': 50, 'b': 50 }
RGB_YELLOW = { 'r':100, 'g':100, 'b':  0 }
RGB_ORANGE = { 'r':100, 'g': 50, 'b':  0 }

##############################################################################
# Return the name of a given Color
def color2str(color) :
    if (color != None and color < len(COLOR_NAMES)) :
        return COLOR_NAMES[color]
    else :
        return None
