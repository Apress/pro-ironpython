def CreateDictionary():
	dict = {"Jane":"CEO", "Tom":"CIO", "Susie":"VP", "Bob":"VP"}
	return dict
def GetName():
	name = raw_input("Please enter an employee\'s name: ")
	return name
def DisplayResult(dict, name):
	if dict.has_key(name):
		print name, "is a", dict[name], "in this company."
	else:
		print name, "does not work for this company."
DisplayResult(CreateDictionary(), GetName())