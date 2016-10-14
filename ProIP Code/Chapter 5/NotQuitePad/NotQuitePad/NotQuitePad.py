import System
from System.Windows.Forms import *
from System.ComponentModel import *
from System.Drawing import *
from clr import *
from interface import *
from fileOperations import *
from IPEngine import *
class NotQuitePad: # namespace
    
    class NotQuitePad(System.Windows.Forms.Form):
        """type(_fileToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_newToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_openToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_saveAsToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_exitToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_mainMenu) == System.Windows.Forms.MenuStrip, type(_printToolStripMenuItem) == System.Windows.Forms.ToolStripMenuItem, type(_txtUserText) == System.Windows.Forms.TextBox"""
        __slots__ = ['_fileToolStripMenuItem', '_newToolStripMenuItem', '_openToolStripMenuItem', '_saveAsToolStripMenuItem', '_exitToolStripMenuItem', '_mainMenu', '_printToolStripMenuItem', '_txtUserText']
        def __init__(self):
            self.InitializeComponent()
        
        @accepts(Self(), bool)
        @returns(None)
        def Dispose(self, disposing):
            
            super(type(self), self).Dispose(disposing)
        
        @returns(None)
        def InitializeComponent(self):
            self._txtUserText = System.Windows.Forms.TextBox()
            self._mainMenu = System.Windows.Forms.MenuStrip()
            self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._newToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._openToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._saveAsToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._printToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
            self._mainMenu.SuspendLayout()
            self.SuspendLayout()
            # 
            # txtUserText
            # 
            self._txtUserText.Font = System.Drawing.Font('Lucida Console', 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
            self._txtUserText.Location = System.Drawing.Point(65, 115)
            self._txtUserText.Multiline = True
            self._txtUserText.Name = 'txtUserText'
            self._txtUserText.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
            self._txtUserText.Size = System.Drawing.Size(100, 20)
            self._txtUserText.TabIndex = 0
            self._txtUserText.TextChanged += self._txtUserText_TextChanged
            # 
            # mainMenu
            # 
            self._mainMenu.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem]((self._fileToolStripMenuItem, )))
            self._mainMenu.Location = System.Drawing.Point(0, 0)
            self._mainMenu.Name = 'mainMenu'
            self._mainMenu.Size = System.Drawing.Size(284, 24)
            self._mainMenu.TabIndex = 1
            self._mainMenu.Text = 'menuStrip1'
            # 
            # fileToolStripMenuItem
            # 
            self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem]((self._newToolStripMenuItem, self._openToolStripMenuItem, self._saveAsToolStripMenuItem, self._printToolStripMenuItem, self._exitToolStripMenuItem, )))
            self._fileToolStripMenuItem.Name = 'fileToolStripMenuItem'
            self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 20)
            self._fileToolStripMenuItem.Text = '&File'
            # 
            # newToolStripMenuItem
            # 
            self._newToolStripMenuItem.Name = 'newToolStripMenuItem'
            self._newToolStripMenuItem.Size = System.Drawing.Size(152, 22)
            self._newToolStripMenuItem.Text = 'New'
            self._newToolStripMenuItem.Click += self._newToolStripMenuItem_Click
            # 
            # openToolStripMenuItem
            # 
            self._openToolStripMenuItem.Name = 'openToolStripMenuItem'
            self._openToolStripMenuItem.Size = System.Drawing.Size(152, 22)
            self._openToolStripMenuItem.Text = 'Open'
            self._openToolStripMenuItem.Click += self._openToolStripMenuItem_Click
            # 
            # saveAsToolStripMenuItem
            # 
            self._saveAsToolStripMenuItem.Name = 'saveAsToolStripMenuItem'
            self._saveAsToolStripMenuItem.Size = System.Drawing.Size(152, 22)
            self._saveAsToolStripMenuItem.Text = 'Save As'
            self._saveAsToolStripMenuItem.Click += self._saveAsToolStripMenuItem_Click
            # 
            # printToolStripMenuItem
            # 
            self._printToolStripMenuItem.Name = 'printToolStripMenuItem'
            self._printToolStripMenuItem.Size = System.Drawing.Size(152, 22)
            self._printToolStripMenuItem.Text = 'Print'
            self._printToolStripMenuItem.Click += self._printToolStripMenuItem_Click
            # 
            # exitToolStripMenuItem
            # 
            self._exitToolStripMenuItem.Name = 'exitToolStripMenuItem'
            self._exitToolStripMenuItem.Size = System.Drawing.Size(152, 22)
            self._exitToolStripMenuItem.Text = 'Exit'
            self._exitToolStripMenuItem.Click += self._exitToolStripMenuItem_Click
            # 
            # NotQuitePad
            # 
            self.ClientSize = System.Drawing.Size(284, 264)
            self.Controls.Add(self._txtUserText)
            self.Controls.Add(self._mainMenu)
            self.MainMenuStrip = self._mainMenu
            self.Name = 'NotQuitePad'
            self.Text = 'NotQuitePad'
            self.Load += self._NotQuitePad_Load
            self.Resize += self._ResizeFormEvent
            self._mainMenu.ResumeLayout(False)
            self._mainMenu.PerformLayout()
            self.ResumeLayout(False)
            self.PerformLayout()
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _NotQuitePad_Load(self, sender, e):
            self._HandleResizing()
                    
        def _ResizeFormEvent(self, sender, e):
            self._HandleResizing()
        
        def _HandleResizing(self):
            newDimensions = interface()
            newDimensions.MoveInputBox(self._txtUserText)
            newDimensions.ResizeInputBox(self._txtUserText, self.Size)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _openToolStripMenuItem_Click(self, sender, e):
            openDialog = fileOperations()
            self._txtUserText.Text = openDialog.Open()
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _saveAsToolStripMenuItem_Click(self, sender, e):
            saveDialog = fileOperations()
            saveDialog.Save(self._txtUserText.Text)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _printToolStripMenuItem_Click(self, sender, e):
            printDialog = fileOperations()
            printDialog.Print(self._txtUserText.Text)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _newToolStripMenuItem_Click(self, sender, e):
            newDocument = fileOperations()
            if newDocument.New() == True:
                self._txtUserText.Text = String.Empty
            else:
                newDocument.Save(self._txtUserText.Text)
                self._txtUserText.Text = String.Empty
            newDocument.SetDirty(False)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _txtUserText_TextChanged(self, sender, e):
            file = fileOperations()
            file.SetDirty(True)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _exitToolStripMenuItem_Click(self, sender, e):
            ui = interface()
            ui.AppExit()
        
    

