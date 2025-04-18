import wx

class MyPanel(wx.Panel):
    """ class MyPanel creates a panel to draw on, inherits wx.Panel """

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")

        self.Bind(wx.EVT_PAINT, self.OnPaint)


    def OnPaint(self, event):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)

        #red filled rectangle
        dc.SetPen(wx.Pen("red"))
        dc.SetBrush(wx.Brush("red"))
        dc.DrawRectangle(30, 10, 120, 80)

        #green filled rectangle
        dc.SetPen(wx.Pen("green"))
        dc.SetBrush(wx.Brush("green"))
        dc.DrawRectangle(150, 10, 120, 80)

        #blue filled rectangle
        dc.SetPen(wx.Pen("blue"))
        dc.SetBrush(wx.Brush("blue"))
        dc.DrawRectangle(270, 10, 120, 80)

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, -1, "CIS 314 Rectangles", size=(460, 300))
    panel = MyPanel(frame,-1)
    frame.Show()        
    frame.Centre()
    app.MainLoop()