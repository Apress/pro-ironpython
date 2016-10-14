def HelloConditional():
	# get a few data values from the user
	firstName = raw_input("Please enter your first name: ")
	lastName = raw_input("Please enter your last name: ")
	try:
		age = int(raw_input("Please enter your age: "))
	except ValueError:
		print "You, ", firstName, lastName, ", need to input a valid age before continuing!"
		HelloConditional()
	finally:
		print "This code is executed in the finally block."
	if age < 0:
		print "You, ", firstName, lastName, ", need to input a valid age before continuing!"
		HelloConditional()
	elif age > 150:
		print "You, ", firstName, lastName, ", need to input a valid age before continuing!"
		HelloConditional()
	elif age < 25:
		print "You, ", firstName, lastName, ", are younger than the author."
	elif age == 25:
		print "You, ", firstName, lastName, ", are the same age as the author."
	else:
		print "You, ", firstName, lastName, ", are older than the author."
HelloConditional()