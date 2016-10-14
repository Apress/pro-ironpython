def GetFirstName():
	firstName = raw_input("Please enter your first name: ")
	return firstName
def GetLastName():
	lastName = raw_input("Please enter your last name: ")
	return lastName
def DisplayResult(firstName, lastName):
	print "Your name is", len(firstName) + len(lastName), "characters long."
DisplayResult(GetFirstName(), GetLastName())