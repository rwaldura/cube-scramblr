#
# Turntable: the rotating platform that holds the cube, and rotates it 
# in the horizontal plane, i.e. along its vertical axis.
#
# It uses a large motor on port B, and a color sensor on port 1.
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

# "B" motor rotates the turntable
table_motor = Motor(Port.B, Direction.CLOCKWISE, [12, 36])
table_speed = 90
#table_motor.set_run_settings(table_speed, 2 * table_speed)
table_epsilon = 22

# color sensor #1, to align the turntable
table_sensor = ColorSensor(Port.S1)

##############################################################################
def init() :
    print("initializing turntable...")

    # go through a full rotation, seeking to maximize the reflection 
    # returned by the sensor
    table_motor.run(table_speed / 2)

    # record the reflection for each angle
    reflect = [0] * 400

    while (table_motor.angle() < 360) :
        wait(100) # sample 10 times per second
        r = table_sensor.reflection()
        a = table_motor.angle()
        # print("reflect", r, "at angle", a)
        reflect[a] = r

    table_motor.stop()

    # find the angle with the highest reflection: it's the closest
    max_angle = reflect.index(max(reflect))
    print("found highest reflection", reflect[max_angle], "at angle", max_angle)

    # correct to get a straight angle on the table
    angle_reflection_epsilon = 7

    _rotate(max_angle + angle_reflection_epsilon)
    table_motor.reset_angle(0)

##############################################################################
# Rotate the turntable BY the given angle
def rotate(angle, correct = False) :
    print("rotating angle:", angle)

    if (angle == 0) : 
        return

    # because the cube is not snug on the turntable, we must
    # overcorrect a bit to get the cube to align correctly
    if (correct) :
        if (angle > 0) : 
            angle += table_epsilon
        else :
            angle -= table_epsilon

    print("corrected angle:", angle)
    
    _rotate(angle)

    if (correct) :
        if (angle > 0) : 
            angle = -table_epsilon
        else :
            angle = +table_epsilon

        _rotate(angle)

##############################################################################
# Rotate the turntable BY the given angle
# (internal method, hence the underscore in prefix)
def _rotate(angle, speed = table_speed) :
    print("rotating turntable by", angle)
    table_motor.run_angle(speed, angle, Stop.BRAKE)

##############################################################################
# Free lap run: 6.5 turns
def spin() :
    _rotate(6 * 90 + 45, table_speed * 2)

##############################################################################
# Move to the next facelet; used while scanning each of the 9 facelets on a 
# cube face
def next_facelet() :
    _rotate(45, table_speed / 2)
