'''Creating toolbars'''
import wx
import wx.py.images as images


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.NewIdRef(), "New", images.getPyBitmap(),
                        "Long help for 'New'")
        toolbar.Realize()
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, "&File")
        editMenu = wx.Menu()
        editMenu.Append(wx.NewIdRef(), "&Copy", "Copy in status bar")
        editMenu.Append(wx.NewIdRef(), "C&ut", "Cut in status bar")
        editMenu.Append(wx.NewIdRef(), "Paste", "Paste in status bar")
        editMenu.AppendSeparator()
        editMenu.Append(wx.NewIdRef(), "&Options...", "Display Options")
        menuBar.Append(editMenu, "&Edit")
        self.SetMenuBar(menuBar)


if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
