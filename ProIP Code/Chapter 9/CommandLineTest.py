import clr
clr.AddReference("System")
import System

class CommandLineTest:
	cmds = System.Environment.GetCommandLineArgs()
	print cmds
	print cmds.Length
	if cmds.Length < 3:
		print "You did not specify an argument for this program."
	else:
		print cmds[2]

CommandLineTest()