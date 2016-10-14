import clr
clr.AddReference("System")
clr.AddReference("System.Data")
from System import *
from System.Data import *
from System.Data.SqlClient import *
from dataManager import *

class employeeData:
    "The data class for the Employee table."
    
    def GetEmployeeNameByID(self, employeeID):
        result = String.Empty
        dm = dataManager()
        conn = dm.GetConnection()
        comm = dm.GetCommand("GetEmployeeNameByID", conn)
        comm.CommandType = CommandType.StoredProcedure
        try:
            conn.Open()
            comm.Parameters.AddWithValue("@employeeID", employeeID)
            reader = comm.ExecuteReader()
            if (reader.Read()):
	        result = reader.GetString(0)
	        reader.Close()
	        conn.Close()
        except:
	        conn.Close()
        if (conn.State == ConnectionState.Open):
	        conn.Close()
	        return result

	        
    def InsertNewEmployee(self, employeeName):
        dm = dataManager()
        conn = dm.GetConnection()
        comm = dm.GetCommand("INSERT INTO Employee VALUES (1, @name, @birthDate, @hireDate)", conn)
        try:
            conn.Open()
            comm.Parameters.AddWithValue("@name", employeeName)
            comm.Parameters.AddWithValue("@birthDate", DateTime.Now.ToString())
            comm.Parameters.AddWithValue("@hireDate", DateTime.Now.ToString())
            comm.ExecuteNonQuery()
            conn.Close()
        except:
            conn.Close()
        if (conn.State == ConnectionState.Open):
	        conn.Close()

    def DeleteEmployee(self, employeeID):
        dm = dataManager()
        conn = dm.GetConnection()
        comm = dm.GetCommand("DELETE FROM Employee WHERE employeeID = @employeeID", conn)
        try:
            conn.Open()
            comm.Parameters.AddWithValue("@employeeID", employeeName)
            comm.ExecuteNonQuery()
            conn.Close()
        except:
            conn.Close()
        if (conn.State == ConnectionState.Open):
	        conn.Close()