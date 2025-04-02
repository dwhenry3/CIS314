#pip install wxPython
import wx

class CISFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="CIS 314 GUI")
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl = wx.StaticText(self.panel, label="Hello CIS 314")        
        self.exit_button = wx.Button(self.panel, label="Exit")

        self.sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)    
        self.sizer.Add(self.exit_button, 0, wx.ALL | wx.CENTER, 10)
        self.panel.SetSizer(self.sizer)

        self.exit_button.Bind(wx.EVT_BUTTON, self.on_close)
    
    def on_close(self, event):
        wx.Exit()

if __name__ == "__main__":
    app = wx.App()
    frame = CISFrame(None)
    frame.Show()
    app.MainLoop()