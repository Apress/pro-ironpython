from System import *
from System.Windows.Forms import *
from NotQuitePad import *

class NotQuitePad0: # namespace
    
    @staticmethod
    def RealEntryPoint():
        Application.EnableVisualStyles()
        Application.Run(NotQuitePad.NotQuitePad())

if __name__ == "Program":
    NotQuitePad0.RealEntryPoint();