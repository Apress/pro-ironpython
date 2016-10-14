from System import *

class document:
    "Represents a document in NotQuitePad."
    
    # properties of the document
    _isDirty = False
    _contents = String.Empty
    
    def IsDirty(self):
        "Gets whether or not a document has been saved since modification."
        return self._isDirty
    
    def SetDirty(self, value):
        "Sets whether or not a document has been saved since modification."
        self._isDirty = value