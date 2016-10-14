from System import *
from System.Windows.Forms import *
from Form1 import *

class IPData0: # namespace
    
    @staticmethod
    def RealEntryPoint():
        Application.EnableVisualStyles()
        Application.Run(IPData.Form1())

if __name__ == "Program":
    IPData0.RealEntryPoint();