import clr
clr.AddReference("System")
clr.AddReference("System.Data")
from System import *
from System.Data import *
from System.Data.SqlClient import *

class dataManager:
    "The data layer manager for our IronPython test application"
    
    def GetConnection(self):
        "Gets a new SqlConnection object"
        conn = SqlConnection("Data Source=YOUR_DATA_SOURCE_HERE;Integrated Security=True;Initial Catalog=IronPython;User Instance=False;Max Pool Size=100;Min Pool Size=5;Pooling=True")
        return conn

    def GetCommand(self, commandString, connection):
        "Gets a new SqlCommand object"
        comm = SqlCommand(commandString, connection)
        return comm