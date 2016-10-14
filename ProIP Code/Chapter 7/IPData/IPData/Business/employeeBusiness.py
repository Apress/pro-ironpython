from employeeData import *

class employeeBusiness:
    "The business class for the Employee table."
    
    def GetEmployeeNameByID(self, employeeID):
        emData = employeeData()
        return emData.GetEmployeeNameByID(employeeID)
        
    def InsertNewEmployee(self, employeeName):
        emData = employeeData()
        emData.InsertNewEmployee(employeeName)

    def DeleteEmployee(self, employeeID):
        emData = employeeData()
        emData.DeleteEmployee(employeeID)