'''A sample startup script showing output stream redirection'''
import wx
import sys


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print("Frame __init__")
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print("App __init__")
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print("OnInit")
        self.frame = Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend error message", file=sys.stderr)
        return True

    def OnExit(self):
        print("OnExit")


if __name__ == '__main__':
    # app = App(redirect=True)
    # app = App(False)
    app = App(True, "2.1_listing.txt")
    print("before MainLoop")
    app.MainLoop()
    print("after MainLoop")
