'''Single choice dialog'''
import wx


if __name__ == '__main__':
    app = wx.App()
    dlg = wx.SingleChoiceDialog(None,
                                'What version of Python are you using?',
                                'Single Choice',
                                ['1.5.2', '2.0', '2.1.3', '2.2', '2.3.1'])
    if dlg.ShowModal() == wx.ID_OK:
        response = dlg.GetStringSelection()

    print(response)
    dlg.Destroy()
    app.MainLoop()
