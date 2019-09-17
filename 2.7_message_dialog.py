'''Message dialog'''
import wx


if __name__ == '__main__':
    app = wx.App()
    dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!',
                           'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
    result = dlg.ShowModal()
    print(result)
    dlg.Destroy()
    app.MainLoop()
