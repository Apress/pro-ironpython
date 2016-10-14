def AddBigIntegers():
	bigInteger = 123456789098712390847 + 23456789109182743087 + 345678912091873 + 567891230987230987
	return bigInteger
def AddBigFloats():
	bigFloat = 90871234.12341324 + 8917623.987124 + 1987345.987247 + 43793873.9871234
	return bigFloat
def DisplayResult(bigInteger, bigFloat):
	print bigInteger
	print bigFloat
DisplayResult(AddBigIntegers(), AddBigFloats())