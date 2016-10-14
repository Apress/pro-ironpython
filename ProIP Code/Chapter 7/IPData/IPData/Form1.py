import System
from System.Windows.Forms import *
from System.ComponentModel import *
from System.Drawing import *
from clr import *
from employeeBusiness import *
class IPData: # namespace
    
    class Form1(System.Windows.Forms.Form):
        """type(_txtEmployeeID) == System.Windows.Forms.TextBox, type(_txtNewEmployee) == System.Windows.Forms.TextBox, type(_btnAdd) == System.Windows.Forms.Button, type(_txtDelEmployee) == System.Windows.Forms.TextBox, type(_btnDelete) == System.Windows.Forms.Button, type(_btnSubmit) == System.Windows.Forms.Button"""
        __slots__ = ['_txtEmployeeID', '_txtNewEmployee', '_btnAdd', '_txtDelEmployee', '_btnDelete', '_btnSubmit']
        def __init__(self):
            self.InitializeComponent()
        
        @accepts(Self(), bool)
        @returns(None)
        def Dispose(self, disposing):
            
            
            
            super(type(self), self).Dispose(disposing)
        
        @returns(None)
        def InitializeComponent(self):
            self._txtEmployeeID = System.Windows.Forms.TextBox()
            self._btnSubmit = System.Windows.Forms.Button()
            self._txtNewEmployee = System.Windows.Forms.TextBox()
            self._btnAdd = System.Windows.Forms.Button()
            self._txtDelEmployee = System.Windows.Forms.TextBox()
            self._btnDelete = System.Windows.Forms.Button()
            self.SuspendLayout()
            # 
            # txtEmployeeID
            # 
            self._txtEmployeeID.Location = System.Drawing.Point(12, 12)
            self._txtEmployeeID.Name = 'txtEmployeeID'
            self._txtEmployeeID.Size = System.Drawing.Size(260, 20)
            self._txtEmployeeID.TabIndex = 0
            # 
            # btnSubmit
            # 
            self._btnSubmit.Location = System.Drawing.Point(108, 38)
            self._btnSubmit.Name = 'btnSubmit'
            self._btnSubmit.Size = System.Drawing.Size(75, 23)
            self._btnSubmit.TabIndex = 1
            self._btnSubmit.Text = 'Get Name'
            self._btnSubmit.UseVisualStyleBackColor = True
            self._btnSubmit.Click += self._btnSubmit_Click
            # 
            # txtNewEmployee
            # 
            self._txtNewEmployee.Location = System.Drawing.Point(12, 67)
            self._txtNewEmployee.Name = 'txtNewEmployee'
            self._txtNewEmployee.Size = System.Drawing.Size(260, 20)
            self._txtNewEmployee.TabIndex = 2
            # 
            # btnAdd
            # 
            self._btnAdd.Location = System.Drawing.Point(108, 93)
            self._btnAdd.Name = 'btnAdd'
            self._btnAdd.Size = System.Drawing.Size(75, 23)
            self._btnAdd.TabIndex = 3
            self._btnAdd.Text = 'Add Name'
            self._btnAdd.UseVisualStyleBackColor = True
            self._btnAdd.Click += self._btnAdd_Click
            # 
            # txtDelEmployee
            # 
            self._txtDelEmployee.Location = System.Drawing.Point(12, 122)
            self._txtDelEmployee.Name = 'txtDelEmployee'
            self._txtDelEmployee.Size = System.Drawing.Size(260, 20)
            self._txtDelEmployee.TabIndex = 4
            # 
            # btnDelete
            # 
            self._btnDelete.Location = System.Drawing.Point(99, 148)
            self._btnDelete.Name = 'btnDelete'
            self._btnDelete.Size = System.Drawing.Size(93, 23)
            self._btnDelete.TabIndex = 5
            self._btnDelete.Text = 'Delete Name'
            self._btnDelete.UseVisualStyleBackColor = True
            self._btnDelete.Click += self._btnDelete_Click
            # 
            # Form1
            # 
            self.ClientSize = System.Drawing.Size(284, 264)
            self.Controls.Add(self._btnDelete)
            self.Controls.Add(self._txtDelEmployee)
            self.Controls.Add(self._btnAdd)
            self.Controls.Add(self._txtNewEmployee)
            self.Controls.Add(self._btnSubmit)
            self.Controls.Add(self._txtEmployeeID)
            self.Name = 'Form1'
            self.Text = 'Form1'
            self.Load += self._Form1_Load
            self.ResumeLayout(False)
            self.PerformLayout()
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _Form1_Load(self, sender, e):
            pass
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _btnSubmit_Click(self, sender, e):
            employee = employeeBusiness()
            self._txtEmployeeID.Text = employee.GetEmployeeNameByID(self._txtEmployeeID.Text)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _btnAdd_Click(self, sender, e):
            employee = employeeBusiness()
            employee.InsertNewEmployee(self._txtNewEmployee.Text)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _btnDelete_Click(self, sender, e):
            employee = employeeBusiness()
            employee.DeleteEmployee(self._txtDelEmployee.Text)
        
    

