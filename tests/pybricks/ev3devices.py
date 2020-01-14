# mock objects for unit testing

class Motor :
    # Motor(Port.B, Direction.CLOCKWISE, [12, 36])
    def __init__(self, port, direction=0, gears=None) :
        self._angle = 90
    def angle(self) : 
        return self._angle
    def reset_angle(self, value) :
        self._angle = value
    def run(self, speed, direction=0, stop=0) :
        self._angle += 10 
    def run_angle(self, speed, angle, stop=0, wait=True) :
        self._angle += angle
    def run_target(self, speed, angle, stop=0, wait=True) :
        self._angle = angle
    def run_until_stalled(self, speed) :
        self._angle = 99
    def stop(self) :
        pass 

class ColorSensor :
    def __init__(self, port) :
        pass
    def color(self) :
        return None
    def rgb(self) :
        return (0,0,0)
    def reflection(self) :
        return 0
