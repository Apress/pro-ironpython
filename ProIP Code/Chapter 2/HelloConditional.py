def HelloConditional():
	firstName = raw_input("Please enter your first name: ")
	lastName = raw_input("Please enter your last name: ")
	age = int(raw_input("Please enter your age: "))
	# change the program output based on the user's age
	if age < 25:
		print "You, ", firstName, lastName, ", are younger than the author."
	elif age == 25:
		print "You, ", firstName, lastName, ", are the same age as the author."
	else:
		print "You, ", firstName, lastName, ", are older than the author."
HelloConditional()