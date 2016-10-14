class SpecialResource:
	class Singleton:
		def identifyMyself(self):
			return id(self)
	__singletonInstance = None
	def __init__(self):
		if SpecialResource.__singletonInstance is None:
			SpecialResource.__singletonInstance = SpecialResource.Singleton()
	def __getattr__(self, attr):
		return getattr(self.__singletonInstance, attr)

	resourceOne = SpecialResource()
	print resourceOne.identifyMyself()
	resourceTwo = SpecialResource()
	print resourceTwo.identifyMyself()
	resourceThree = SpecialResource()
	print resourceThree.identifyMyself()