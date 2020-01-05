#
# Utility functions to deal with EV3 colors.
#
# by Ren Waldura ren+lego@waldura.org, 2020
#
# See LICENSE file for licensing information
#

from pybricks.parameters import Color

##############################################################################
# Return the name of a given Color
def color2str(color) :
    if (color == Color.BLACK) : # 1
        return "black"
    elif (color == Color.BLUE) : # 2
        return "blue"
    elif (color == Color.GREEN) : # 3
        return "green",        
    elif (color == Color.YELLOW) : # 4
        return "yellow" 
    elif (color == Color.RED) : # 5
        return "red"
    elif (color == Color.WHITE) : # 6
        return "white"   
    elif (color == Color.BROWN) : # 7
        return "brown"     
    elif (color == Color.ORANGE) : # 8
        return "orange"
    elif (color == Color.PURPLE) : # 9
        return "purple"    
    else :
        return ""

##############################################################################
# Map a R/G/B dict to a known Color constant
def rgb2color(rgb) :
    return Color.PURPLE
