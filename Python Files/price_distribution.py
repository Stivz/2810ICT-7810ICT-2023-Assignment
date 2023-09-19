import pandas as pd
import wx
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class PriceDistribution(wx.Frame):
    def __init__(self, parent, data):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1980, 1080), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # Create a BoxSizer for the top 1/3
        bSizer_top = wx.BoxSizer(wx.VERTICAL)

        # Create a BoxSizer for the bottom 2/3
        bSizer_bottom = wx.BoxSizer(wx.VERTICAL)

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

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Back To Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer51.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, 5)
        bSizer18.Add(gSizer51, 1, 0, 5)

        # Add the BoxSizer for the top 1/3 to the main sizer
        bSizer_top.Add(bSizer18, 1, wx.EXPAND, 5)

        # Create a BoxSizer for the top 1/3
        bSizer12 = wx.BoxSizer(wx.VERTICAL)
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(
            wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Price Distribution Chart", wx.DefaultPosition,
                                           wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)
        bSizer12.Add(bSizer15, 0, wx.EXPAND, 5)

        # Create a button to generate the graph
        self.generate_graph_button = wx.Button(self, wx.ID_ANY, u"Generate Graph", wx.DefaultPosition, wx.DefaultSize,
                                               0)
        self.generate_graph_button.Bind(wx.EVT_BUTTON, self.on_generate_graph_button_click)
        bSizer12.Add(self.generate_graph_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Add the BoxSizer for the top 1/3 to the main sizer
        bSizer_top.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer14.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer_top, 1, wx.EXPAND, 5)  # Add the BoxSizer for the top 1/3 to the main sizer
        bSizer1.Add(bSizer14, 2, wx.EXPAND, 5)  # Add the BoxSizer for the bottom 2/3 to the main sizer

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        self.m_button5.Bind(wx.EVT_BUTTON, self.on_back_button_click)

        self.data = data  # Store the DataFrame for later use

        # Create a Figure and a canvas for displaying the plot
        self.figure = Figure(figsize=(7, 5))
        self.canvas = FigureCanvas(self.m_panel1, -1, self.figure)

    def compare_neighborhoods(self, neighborhood1_input, neighborhood2_input, min_price_range, max_price_range):
        # Filter rows based on the user input for the first neighborhood
        neighborhood1_data = self.data[self.data['neighbourhood_cleansed'] == neighborhood1_input]

        # Filter rows based on the user input for the second neighborhood
        neighborhood2_data = self.data[self.data['neighbourhood_cleansed'] == neighborhood2_input]

        # Check if any listings were found for the specified neighborhoods
        if neighborhood1_data.empty or neighborhood2_data.empty:
            wx.MessageBox("No listings found for one or both of the specified neighborhoods.", "Error",
                          wx.OK | wx.ICON_ERROR)
        else:
            # Extract the 'price' columns for the selected neighborhoods
            price1_data = neighborhood1_data['price'].str.replace('[$,]', '', regex=True).astype(float)
            price2_data = neighborhood2_data['price'].str.replace('[$,]', '', regex=True).astype(float)

            # Create histograms of the 'price' data for both neighborhoods
            ax = self.figure.add_subplot(111)
            bin_step = 50  # Set the desired increment step size
            bins = [x for x in
                    range(int(min_price_range), int(max_price_range) + 1,
                          bin_step)]  # Adjust the bin width as needed

            ax.hist(price1_data, bins=bins, alpha=0.8, label=neighborhood1_input, edgecolor='k', color='blue',
                    width=bin_step)
            ax.hist(price2_data, bins=bins, alpha=0.5, label=neighborhood2_input, edgecolor='k', color='orange',
                    width=bin_step)

            ax.set_xlabel('Price')
            ax.set_ylabel('Frequency')
            ax.set_title(f'Price Distribution Comparison between {neighborhood1_input} and {neighborhood2_input}')
            ax.legend()

            # Draw the new plot on the canvas
            self.canvas.draw()

    def on_generate_graph_button_click(self, event):
        # Get user input for the first neighborhood
        neighborhood1_input = wx.GetTextFromUser("Enter the first neighborhood name (e.g., 'Sydney', 'Waverley'):",
                                                 "Neighborhood 1")
        # Get user input for the second neighborhood
        neighborhood2_input = wx.GetTextFromUser("Enter the second neighborhood name (e.g., 'Sydney', 'Waverley'):",
                                                 "Neighborhood 2")

        if not neighborhood1_input or not neighborhood2_input:
            wx.MessageBox("Please enter valid neighborhood names.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Prompt the user to enter the minimum and maximum price range
        min_price_range = wx.GetNumberFromUser("Enter the minimum price (e.g., 0):", "Minimum Price", "Minimum Price",
                                               0, 0, 10000)
        max_price_range = wx.GetNumberFromUser("Enter the maximum price (e.g., 1000):", "Maximum Price",
                                               "Maximum Price", 1000, 0, 10000)

        if min_price_range > max_price_range:
            wx.MessageBox("Minimum price cannot be greater than maximum price.", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.compare_neighborhoods(neighborhood1_input, neighborhood2_input, min_price_range, max_price_range)

    def on_back_button_click(self, event):
        from Main_Menu import MainMenu  # Import the MainMenu class from Main_Menu.py
        self.Close()
        # Create and show a new instance of the MainMenu class
        app = wx.App(False)
        main_frame = MainMenu(None)
        main_frame.Show()
        app.MainLoop()

if __name__ == "__main__":
    data_file_path = os.path.join("csv files", "listings_dec18.csv")
    data = pd.read_csv(data_file_path)  # Load your DataFrame from a CSV file
    app = wx.App(False)
    main_frame = PriceDistribution(None, data)  # Pass the DataFrame as an argument
    main_frame.Show()
    app.MainLoop()
