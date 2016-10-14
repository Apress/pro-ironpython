import sys
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Form
class IronPythonForm(Form):
	def __init__(self):
		self.Text = 'IronPython Forms Application'
		self.Name = 'FormApp'
form = IronPythonForm()
Application.Run(form)