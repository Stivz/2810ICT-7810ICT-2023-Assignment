
from Top_Rated import TopRatedFrame  # Import the TopRatedFrame class from Top_Rated.py
from price_distribution import PriceDistribution  # Import the PriceDistributionFrame class from price_distribution.py
from Listings import listings
import wx
import os
import pandas as pd

class MainMenu(wx.Frame):
    def __init__(self, parent, data):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition, size=wx.Size(1980, 1080),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.data = data  # Store the data DataFrame

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        gSizer51 = wx.GridSizer(0, 12, 0, 0)

        self.m_searchCtrl2 = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_searchCtrl2.ShowSearchButton(True)
        self.m_searchCtrl2.ShowCancelButton(False)
        gSizer51.Add(self.m_searchCtrl2, 0, wx.ALIGN_CENTER | wx.ALL, 20)

        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)
        gSizer51.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer18.Add(gSizer51, 1, 0, 5)
        bSizer12.Add(bSizer18, 1, wx.EXPAND, 5)
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(
            wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)
        bSizer12.Add(bSizer15, 1, wx.EXPAND, 5)
        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)
        gSizer2 = wx.GridSizer(0, 1, 0, 0)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button14, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        bSizer19.Add(gSizer2, 1, 0, 5)
        gSizer4 = wx.GridSizer(0, 1, 0, 0)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"Top Rated", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button15, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        bSizer19.Add(gSizer4, 1, 0, 5)
        gSizer5 = wx.GridSizer(0, 1, 0, 0)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Price Distribution", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.m_button16, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        bSizer19.Add(gSizer5, 1, 0, 5)
        gSizer6 = wx.GridSizer(0, 1, 0, 0)

        self.m_button17 = wx.Button(self, wx.ID_ANY, u"Calender", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer6.Add(self.m_button17, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        bSizer19.Add(gSizer6, 1, 0, 5)
        bSizer12.Add(bSizer19, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        bSizer1.Add(bSizer12, 1, wx.EXPAND, 5)
        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer14.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        bSizer1.Add(bSizer14, 1, wx.EXPAND, 5)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_simplebook3 = wx.Simplebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_simplebook3, 1, wx.EXPAND | wx.ALL, 5)
        bSizer1.Add(bSizer17, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        self.top_rated_clicked = False  # Initialize the flag to False
        self.listings_clicked = False  # Initialize the flag to False
        self.price_distribution_button_clicked = False  # Initialize the flag to False
        # Bind the "Top Rated" button to the event handler
        self.m_button14.Bind(wx.EVT_BUTTON, self.on_listings_button_click)
        self.m_button15.Bind(wx.EVT_BUTTON, self.on_top_rated_button_click)
        self.m_button16.Bind(wx.EVT_BUTTON, self.on_price_distribution_button_click)

    def on_top_rated_button_click(self, event):
        # Set the flag to True when the button is clicked
        self.top_rated_clicked = True
        # Create and show the "Top Rated" frame
        top_rated_frame = TopRatedFrame(None, self)
        top_rated_frame.Show()
        # Close the MainFrame
        self.Close()

    def on_price_distribution_button_click(self, event):
        self.price_distribution_button_clicked = True
        # Create and show the PriceDistributionFrame
        price_distribution_frame = PriceDistribution(None, data)
        price_distribution_frame.Show()
        # Close the MainMenu frame
        self.Close()

    def on_listings_button_click(self, event):
        self.listings_clicked = True
        listings_frame = listings(None, data)
        listings_frame.Show()
        self.Close()

    def close_top_rated_frame(self):
        self.Close()
        self.main_frame.Show()
    # Add this method to handle the event when TopRatedFrame is closed
    def on_top_rated_frame_closed(self):
        self.top_rated_clicked = False  # Reset the flag when TopRatedFrame is closed
        self.Show()  # Show the MainFrame again

if __name__ == "__main__":
    app = wx.App(False)

    # Construct the full path to the CSV file using an absolute path
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_directory, "..", "csv files", "listings_dec18.csv")
    data = pd.read_csv(data_file_path)  # Load your DataFrame from a CSV file
    frame = MainMenu(None, data)  # Pass the DataFrame as an argument
    frame.Show()
    app.MainLoop()

