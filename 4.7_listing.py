import wx
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame

import wx.py.images as images


class ToolbarFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(300, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.NewIdRef(), "New", images.getPyBitmap(),
                        "Long help for 'New'")
        toolbar.Realize()
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewIdRef(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewIdRef(), "C&ut", "")
        menu2.Append(wx.NewIdRef(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewIdRef(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")

        menu3 = wx.Menu()
        shell = menu3.Append(-1, "&wxPython shell",
                             "Open wxPython shell frame")
        filling = menu3.Append(-1, "&Namespace viewer",
                               "Open namespace viewer frame")
        menuBar.Append(menu3, "&Debug")
        self.Bind(wx.EVT_MENU, self.OnShell, shell)
        self.Bind(wx.EVT_MENU, self.OnFilling, filling)
        self.SetMenuBar(menuBar)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnShell(self, event):
        frame = ShellFrame(parent=self)
        frame.Show()

    def OnFilling(self, event):
        frame = FillingFrame(parent=self)
        frame.Show()


if __name__ == '__main__':
    app = wx.App()
    app.frame = ToolbarFrame(parent=None, id=-1)
    app.frame.Show()
    app.MainLoop()
