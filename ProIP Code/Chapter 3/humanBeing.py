class Human:
	# some data about our human, with default values for convenience
	age = 25
	name = 'Alan Harris'
	weight = 190

	# methods for setting attributes about our human
	def setAge(self, age):
		self.age = age
	def setName(self, name):
		self.name = name
	def setWeight(self, weight):
		self.weight = weight

	# methods for getting attributes about our human
	def getAge(self):
		return self.age
	def getName(self):
		return self.name
	def getWeight(self):
		return self.weight
	def getInfo(self):
		print "Human being", self.name, "is", self.age, "years old and weighs", self.weight, "pounds."