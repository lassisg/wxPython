'''Text entry dialog'''
import wx


if __name__ == '__main__':
    app = wx.App()
    dlg = wx.TextEntryDialog(None, "Who is buried in Grant's tomb?",
                             'A Question', 'Cary Grant')
    if dlg.ShowModal() == wx.ID_OK:
        response = dlg.GetValue()

    print(response)
    dlg.Destroy()
    app.MainLoop()
