from System import *
from System.Windows.Forms import *
from System.Windows import *
from System.IO import *
from System.Drawing.Printing import *
from document import *

class fileOperations:
    "Contains file system operations for NotQuitePad."
    
    doc = document()
    
    def New(self):
        "Creates a new file within NotQuitePad."
        if self._CheckIfFileIsDirty() == True:
	        msg = MessageBox.Show("Do you want to save the changes to your file?", "NotQuitePad", MessageBoxButtons.YesNo)
	        if msg == DialogResult.Yes:
	            return False
	        else:
	            return True
        else:
	        return True
    
    def _CheckIfFileIsDirty(self):
        "Call the document class to find out if a document has been marked dirty and needs to be saved."
        return self.doc.IsDirty()
        
    def SetDirty(self, value):
        "Call the document class to set the dirty property of a document."
        self.doc.SetDirty(value)
    
    def Open(self):
        "Handles the Open dialog window."
        dialog = OpenFileDialog()
        dialog.Title = "Load File"
        if dialog.ShowDialog() == DialogResult.OK:
                contents = self._OpenFileFromDisk(dialog.FileName)
                return contents
        
    def _OpenFileFromDisk(self, fileName):
        "Opens a connection to the file system."
        file = File.OpenText(fileName)
        data = file.ReadToEnd().ToString()
        file.Close()
        return data

   
    def Save(self, fileContents):
        "Handles the Save dialog window."
        dialog = SaveFileDialog()
        dialog.Title = "Save File"
        if dialog.ShowDialog() == DialogResult.OK:
	        self._WriteFileToDisk(dialog.FileName, fileContents)
	        return True
 
    def _WriteFileToDisk(self, fileName, fileContents):
        "After executing the Save method, write the file and contents to the desired location."
        file = File.CreateText(fileName)
        file.Write(fileContents)
        file.Close()

    def Print(self, fileContents):
        "Handles the Print dialog window."
        dialog = PrintDialog()
        if dialog.ShowDialog() == DialogResult.OK:
            doc = PrintDocument()
            dialog.Document = doc
            self._PrintDocument(doc)
    
    def _PrintDocument(self, printDocument):
        "Sends a document to the selected printing device."
        printDocument.Print()