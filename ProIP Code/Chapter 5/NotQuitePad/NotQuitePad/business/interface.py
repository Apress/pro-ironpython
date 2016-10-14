from System import *
from System.Windows.Forms import *
from System.Drawing import *

class interface:
    "Code related to the user interface logic of NotQuitePad"
        
    def MoveInputBox(self, box):
        "Changes the location of an object to the origin (point 0, 0)"
        box.Location = Point(0,24)

    def ResizeInputBox(self, box, windowSize):
        "Resizes an object to equal the size of another object"
        windowSize.Height = windowSize.Height - 60
        windowSize.Width = windowSize.Width - 15
        box.Size = windowSize
        
    def AppExit(self):
        "Exits the current application"
        Application.Exit()