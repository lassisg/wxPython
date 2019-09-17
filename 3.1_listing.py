'''Sample event binding both with and without source objects'''
import wx


class MenuEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                          size=(300, 100))
        panel = wx.Panel(self, -1)
        button = wx.Button(panel, -1, "Close", pos=(130, 15),
                           size=(40, 40))
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MenuEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
