def GetWord():
	word = raw_input("Please enter the word you want to find: ")
	return word
def GetText():
	text = raw_input("Please enter the text block: ")
	return text
def DisplayResult(word, text):
	position = text.find(word)
	if position > -1:
		print "The word", word, "was found at position", position, "."
	else:
		print "The word", word, "was not found in this string."
DisplayResult(GetWord(), GetText())