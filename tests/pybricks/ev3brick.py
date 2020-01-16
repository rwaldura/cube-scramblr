# mock objects

from pybricks.parameters import Button

class Display :
    def __init__(self) :
        pass
    def clear(self) :
        pass
    def text(self, mesg) :
        print(">>>", mesg)

class Sound :
    def __init__(self) :
        pass
    def beep(self) :
        pass

display = Display()
sound = Sound()
buttons = ()

# to drive unit tests
def set_buttons(b) :
    buttons = b

def buttons() :
    return buttons

