import wx

class ModernFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(ModernFrame, self).__init__(*args, **kw)

        self.SetSize((400, 300))
        self.SetTitle("Modern GUI with wxPython")
        self.SetBackgroundColour("#f0f0f0")  # Light background for a modern look

        # Add main panel
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#ffffff")  # White panel for contrast

        # Custom font for labels and buttons
        font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Add title label
        title = wx.StaticText(panel, label="Welcome to Modern GUI", pos=(20, 20))
        title.SetFont(font)
        title.SetForegroundColour("#4a4a4a")

        # Custom text input with padding and rounded corners
        text_input = wx.TextCtrl(panel, pos=(20, 60), size=(340, 30))
        text_input.SetBackgroundColour("#e8e8e8")
        text_input.SetForegroundColour("#333333")
        text_input.SetHint("Enter something...")

        # Add a button with rounded corners
        button = wx.Button(panel, label="Submit", pos=(20, 110), size=(340, 35))
        button.SetBackgroundColour("#0078D7")
        button.SetForegroundColour("#ffffff")
        button.SetFont(font)

        # Handle button click event
        button.Bind(wx.EVT_BUTTON, self.on_submit)

    def on_submit(self, event):
        wx.MessageBox("Button clicked!", "Info", wx.OK | wx.ICON_INFORMATION)

app = wx.App(False)
frame = ModernFrame(None)
frame.Show(True)
app.MainLoop()
