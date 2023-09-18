import wx


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition, size=wx.Size(1980, 1080),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_searchCtrl2 = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_searchCtrl2.ShowSearchButton(True)
        self.m_searchCtrl2.ShowCancelButton(False)
        bSizer18.Add(self.m_searchCtrl2, 0, wx.ALL, 20)

        bSizer12.Add(bSizer18, 1, wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        # Create a larger font for m_staticText7
        font = wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(font)  # Set the larger font here

        bSizer15.Add(self.m_staticText7, 0, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer2 = wx.GridSizer(0, 1, 0, 0)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"Listings",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button14, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer19.Add(gSizer2, 1, 0, 5)

        gSizer4 = wx.GridSizer(0, 1, 0, 0)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"Top Rated",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button15, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer19.Add(gSizer4, 1, wx.EXPAND, 5)

        gSizer5 = wx.GridSizer(0, 1, 0, 0)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Price Distribution",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.m_button16, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer19.Add(gSizer5, 1, wx.EXPAND, 5)

        gSizer6 = wx.GridSizer(0, 1, 0, 0)

        self.m_button17 = wx.Button(self, wx.ID_ANY, u"Calendar",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer6.Add(self.m_button17, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer19.Add(gSizer6, 1, wx.EXPAND, 5)

        bSizer12.Add(bSizer19, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                 wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer14.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_simplebook3 = wx.Simplebook(self, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, 0)

        bSizer17.Add(self.m_simplebook3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer17, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)


app = wx.App(False)
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
