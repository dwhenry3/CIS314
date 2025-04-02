import wx

class DrawingPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_click)

    def on_click(self, event):
        dc = wx.ClientDC(self)  # Create a device context for the panel
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 1))  # Set pen color and width
        dc.DrawPoint(event.GetX(), event.GetY())  # Draw a point at the click coordinates

app = wx.App()
frame = wx.Frame(None, title="Drawing Panel", size=(460, 300))
panel = DrawingPanel(frame)
frame.Show()
app.MainLoop()