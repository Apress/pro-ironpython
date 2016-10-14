def SetFlag():
	flagEnabled = True
	return flagEnabled
def DisplayFlag(flagEnabled):
	if flagEnabled == True:
		print "The flag is set to true."
	else:
		print "The flag is set to false."
DisplayFlag(SetFlag())