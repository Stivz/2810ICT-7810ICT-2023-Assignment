import pandas as pd
import wx
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class PriceDistribution(wx.Frame):
    def __init__(self, parent, data, reviews_data, calendardata):
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
        bSizer_top.Add(bSizer18, 0, wx.EXPAND, 5)

        # Create a BoxSizer for the top 1/3
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        # Create a BoxSizer for the top 1/3
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        # Add some empty space before the static text
        bSizer15.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(
            wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Price Distribution Chart", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)

        # Add some empty space after the static text
        bSizer15.Add((0, 20), 0, wx.EXPAND, 5)
        bSizer15.Add((0, 20), 0, wx.EXPAND, 5)

        # Add the BoxSizer for static text to the main sizer (vertical)
        bSizer12.Add(bSizer15, 0, wx.EXPAND, 5)

        # Create a BoxSizer for the dropdowns, text fields, date pickers, and the "Generate Graph" button (vertical)
        bSizer_vertical = wx.BoxSizer(wx.HORIZONTAL)

        # Create wx.Choice widgets for selecting suburbs
        suburb_choices = data['neighbourhood_cleansed'].unique()
        suburb_choices1 = ["Select suburb 1"] + list(suburb_choices)
        suburb_choices2 = ["Select suburb 2"] + list(suburb_choices)
        self.suburb_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choices=suburb_choices1)
        self.suburb_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choices=suburb_choices2)
        # Set "Select a suburb" as the initial selection
        self.suburb_choice1.SetSelection(0)
        self.suburb_choice2.SetSelection(0)

        # Create text fields for entering minimum and maximum price
        self.min_price_text = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize)
        self.max_price_text = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize)

        # Set default text for text fields and bind focus events
        self.set_default_text(self.min_price_text, "Enter Min Value")
        self.set_default_text(self.max_price_text, "Enter Max Value")

        # Create a BoxSizer for the date pickers and "Generate Graph" button (horizontal)
        bSizer_horizontal = wx.BoxSizer(wx.HORIZONTAL)

        # Create date pickers and a "Generate Graph" button
        self.start_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                       wx.DefaultSize, style=wx.adv.DP_DEFAULT)
        self.end_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                     wx.DefaultSize, style=wx.adv.DP_DEFAULT)

        # Create a valid wx.DateTime object for January 1, 2019
        default_date = wx.DateTime.Now()
        default_date.SetYear(2019)
        default_date.SetMonth(1)
        default_date.SetDay(1)

        self.start_date_picker.SetValue(default_date)
        self.end_date_picker.SetValue(default_date)

        self.generate_graph_button = wx.Button(self, wx.ID_ANY, u"Generate Graph", wx.DefaultPosition, wx.DefaultSize, 0)
        self.generate_graph_button.Bind(wx.EVT_BUTTON, self.on_generate_graph_button_click)

        # Add the suburb selector and min/max value inputs to the horizontal sizer
        bSizer_horizontal.Add(self.suburb_choice1, 0, wx.ALL, 5)
        bSizer_horizontal.Add(self.suburb_choice2, 0, wx.ALL, 5)
        bSizer_horizontal.Add(self.min_price_text, 0, wx.ALL, 5)
        bSizer_horizontal.Add(self.max_price_text, 0, wx.ALL, 5)

        # Add the date pickers and "Generate Graph" button to the horizontal sizer
        bSizer_horizontal.Add(self.start_date_picker, 0, wx.ALL, 5)
        bSizer_horizontal.Add(self.end_date_picker, 0, wx.ALL, 5)
        bSizer_horizontal.Add(self.generate_graph_button, 0, wx.ALL, 5)

        # Add both the vertical and horizontal sizers to a parent sizer
        bSizer_parent = wx.BoxSizer(wx.VERTICAL)
        bSizer_parent.Add(bSizer_vertical, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        bSizer_parent.Add(bSizer_horizontal, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        # Add the parent sizer to the main sizer (bSizer_top in your code)
        bSizer12.Add(bSizer_parent, 0, wx.EXPAND, 5)
        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        # Create a BoxSizer for the panel to display the graph
        bSizer_panel = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_panel.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 6)

        bSizer14.Add(bSizer_panel, 1, wx.EXPAND, 5)
        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer_top.Add(bSizer12, 0, wx.EXPAND, 5)
        bSizer_top.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer_top, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        self.m_button5.Bind(wx.EVT_BUTTON, self.on_back_button_click)

        self.data = data  # Store the listings DataFrame for later use
        self.calendardata = calendardata  # Store the calendar DataFrame for date information
        self.reviews_data = reviews_data

        # Rename the "id" column in the listings DataFrame to "listing_id"
        self.data.rename(columns={'id': 'listing_id'}, inplace=True)

        # Create a Figure and a canvas for displaying the plot
        self.figure = Figure(figsize=(7, 6))
        self.canvas = FigureCanvas(self.m_panel1, -1, self.figure)

    def compare_neighborhoods(self, neighborhood1_input, neighborhood2_input, min_price_range, max_price_range,
                              start_date_str, end_date_str):

        self.figure.clf()
        ax = self.figure.add_subplot(111)

        date_range_label = f'Date Range: {start_date_str} to {end_date_str}'
        ax.text(0.5, 1.05, date_range_label, horizontalalignment='center', verticalalignment='center',
                transform=ax.transAxes, fontsize=12, color='black')

        neighborhood1_data = self.data[self.data['neighbourhood_cleansed'] == neighborhood1_input].copy()
        neighborhood2_data = self.data[self.data['neighbourhood_cleansed'] == neighborhood2_input].copy()

        if neighborhood1_data.empty or neighborhood2_data.empty:
            wx.MessageBox("No listings found for one or both of the specified neighborhoods.", "Error",
                          wx.OK | wx.ICON_ERROR)
            return

        neighborhood1_data.loc[:, 'price'] = neighborhood1_data['price'].str.replace('[$,]', '', regex=True).astype(
            float)
        neighborhood2_data.loc[:, 'price'] = neighborhood2_data['price'].str.replace('[$,]', '', regex=True).astype(
            float)

        start_date = pd.to_datetime(start_date_str)
        end_date = pd.to_datetime(end_date_str)

        if start_date > end_date:
            wx.MessageBox("Start date should be earlier than end date.", "Date Error", wx.OK | wx.ICON_ERROR)
            return

        neighborhood1_data = neighborhood1_data[
            (neighborhood1_data['listing_id'].isin(self.calendardata['listing_id'])) &
            (pd.to_datetime(self.calendardata['date']) >= start_date) &
            (pd.to_datetime(self.calendardata['date']) <= end_date)]
        neighborhood2_data = neighborhood2_data[
            (neighborhood2_data['listing_id'].isin(self.calendardata['listing_id'])) &
            (pd.to_datetime(self.calendardata['date']) >= start_date) &
            (pd.to_datetime(self.calendardata['date']) <= end_date)]

        bin_step = 50
        bins = [x for x in range(int(min_price_range), int(max_price_range) + 1, bin_step)]

        ax.hist(neighborhood1_data['price'], bins=bins, alpha=0.8, label=neighborhood1_input, edgecolor='k',
                color='blue',
                width=bin_step)
        ax.hist(neighborhood2_data['price'], bins=bins, alpha=0.5, label=neighborhood2_input, edgecolor='k',
                color='orange',
                width=bin_step)

        ax.set_xlabel('Price')
        ax.set_ylabel("Number of Airbnb's")
        ax.set_title(f'Price Distribution between {neighborhood1_input} and {neighborhood2_input}', y=1.1)

        if not neighborhood1_data.empty and not neighborhood2_data.empty:
            ax.legend()

        self.canvas.draw()

    def on_generate_graph_button_click(self, event):

        neighborhood1_input = self.suburb_choice1.GetStringSelection()
        neighborhood2_input = self.suburb_choice2.GetStringSelection()
        min_price_input = self.min_price_text.GetValue()
        max_price_input = self.max_price_text.GetValue()

        try:
            min_price_range = float(min_price_input)
            max_price_range = float(max_price_input)
        except ValueError:
            wx.MessageBox("Please enter valid numerical values for minimum and maximum prices.", "Error",
                          wx.OK | wx.ICON_ERROR)
            return

        if not neighborhood1_input or not neighborhood2_input:
            wx.MessageBox("Please select two suburbs for comparison.", "Error", wx.OK | wx.ICON_ERROR)
            return
        if neighborhood1_input == neighborhood2_input:
            wx.MessageBox("Please select two different suburbs for comparison.", "Error", wx.OK | wx.ICON_ERROR)
            return

        if min_price_range > max_price_range:
            wx.MessageBox("Minimum price cannot be greater than maximum price.", "Error", wx.OK | wx.ICON_ERROR)
            return

        start_date = self.start_date_picker.GetValue()
        end_date = self.end_date_picker.GetValue()

        start_date_str = start_date.Format('%Y-%m-%d')
        end_date_str = end_date.Format('%Y-%m-%d')

        self.compare_neighborhoods(neighborhood1_input, neighborhood2_input, min_price_range, max_price_range,
                                   start_date_str, end_date_str)

    def on_back_button_click(self, event):
        from Main_Menu import MainMenu
        self.Close()
        app = wx.App(False)
        main_frame = MainMenu(None, self.data, self.reviews_data, self.calendardata)
        main_frame.Show()
        app.MainLoop()

    def set_default_text(self, text_ctrl, default_text):
        text_ctrl.SetValue(default_text)
        text_ctrl.Bind(wx.EVT_SET_FOCUS, lambda event: self.on_text_ctrl_focus(event, text_ctrl, default_text))
        text_ctrl.Bind(wx.EVT_KILL_FOCUS, lambda event: self.on_text_ctrl_kill_focus(event, text_ctrl, default_text))

    def on_text_ctrl_focus(self, event, text_ctrl, default_text):
        if text_ctrl.GetValue() == default_text:
            text_ctrl.SetValue("")

    def on_text_ctrl_kill_focus(self, event, text_ctrl, default_text):
        if text_ctrl.GetValue() == "":
            text_ctrl.SetValue(default_text)

if __name__ == "__main__":
    calendar_data_file_path = os.path.join("..", 'csv files', "calendar_dec18.csv")
    data_file_path = os.path.join("csv files", "listings_dec18.csv")

    calendardata = pd.read_csv(calendar_data_file_path)
    data = pd.read_csv(data_file_path)

    app = wx.App(False)
    main_frame = PriceDistribution(None, data, None, calendardata)
    main_frame.Show()
    app.MainLoop()
