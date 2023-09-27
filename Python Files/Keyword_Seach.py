import wx
import wx.adv
import os
import pandas as pd
import wx.grid
import random


class keyword(wx.Frame):
    def __init__(self, parent, data, reviews_data, calendardata):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1980, 1080), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.calendardata = calendardata  # Store the DataFrame for later use
        self.data = data
        self.reviews_data = reviews_data

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

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Back To Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer51.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, 5)

        bSizer18.Add(gSizer51, 1, 0, 5)
        bSizer12.Add(bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(
            wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Keyword search for available properties", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        bSizer15.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)
        bSizer12.Add(bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)
        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        # Create a panel for the date pickers, search box, and confirm button
        panel = wx.Panel(self)
        panel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create the date pickers and "Confirm" button
        self.start_date_picker = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                       wx.DefaultSize, style=wx.adv.DP_DEFAULT)
        self.end_date_picker = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                     wx.DefaultSize, style=wx.adv.DP_DEFAULT)
        self.confirm_button = wx.Button(panel, wx.ID_ANY, u"Confirm")

        # Add the date pickers and "Confirm" button to the panel_sizer
        panel_sizer.Add(self.start_date_picker, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        panel_sizer.Add(self.end_date_picker, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # Create a text box for keyword search
        self.keyword_textbox = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        panel_sizer.Add(self.keyword_textbox, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        panel_sizer.Add(self.confirm_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        panel.SetSizer(panel_sizer)

        # Add the panel with date pickers, search box, and confirm button to the main button sizer
        bSizer19.Add(panel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer12.Add(bSizer19, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer1.Add(bSizer12, 0, wx.EXPAND, 5)

        # Additional space at the bottom
        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_back_button_click)
        self.confirm_button.Bind(wx.EVT_BUTTON, self.on_confirm_button_click)

    def on_confirm_button_click(self, event):
        start_date = self.start_date_picker.GetValue()
        end_date = self.end_date_picker.GetValue()
        keyword = self.keyword_textbox.GetValue().strip().lower()  # Get the keyword from the text box and convert to lowercase

        # Ensure start_date is earlier than end_date
        if start_date > end_date:
            wx.MessageBox("Start date should be earlier than end date.", "Date Error", wx.OK | wx.ICON_ERROR)
            return

        start_date_str = start_date.Format('%Y-%m-%d')
        end_date_str = end_date.Format('%Y-%m-%d')

        # Filter the DataFrame to get available properties within the selected date range
        available_properties = self.calendardata[
            (self.calendardata['date'] >= start_date_str) &
            (self.calendardata['date'] <= end_date_str) &
            (self.calendardata['available'] == 't')
            ]

        # Create a set to keep track of unique property IDs
        unique_property_ids = set()

        # Create a list to store the unique property data
        unique_property_data = []

        # Iterate through the available_properties DataFrame
        for _, row in available_properties.iterrows():
            property_id = row['listing_id']

            # Check if this property ID has already been added to the unique_property_ids set
            if property_id not in unique_property_ids:
                # Add the property ID to the set to mark it as seen
                unique_property_ids.add(property_id)

                # Get the corresponding data from the listings DataFrame
                listing_data = self.data.loc[self.data['id'] == property_id, ['id', 'name', 'amenities']].iloc[0]

                # Check if the keyword is present in the amenities (converted to lowercase)
                if keyword in listing_data['amenities'].lower():
                    # Create a list of searched amenities
                    searched_amenities = [keyword]

                    # Split the amenities string into a list and remove leading/trailing spaces
                    all_amenities = [amenity.strip() for amenity in listing_data['amenities'].split(',')]

                    # Randomly select 5 additional amenities from the property
                    additional_amenities = random.sample(all_amenities, min(5, len(all_amenities)))

                    # Combine the searched and additional amenities
                    combined_amenities = searched_amenities + additional_amenities

                    # Create a new row with combined data
                    combined_row = pd.Series({
                        'listing_id': property_id,
                        'name': listing_data['name'],
                        'available': row['available'],
                        'price': row['price'],
                        'amenities': ', '.join(combined_amenities)  # Include the combined amenities information
                    })

                    # Append the combined row to the unique_property_data list
                    unique_property_data.append(combined_row)

        # Create a DataFrame from the unique_property_data list
        merged_data = pd.DataFrame(unique_property_data)

        # Create a new frame to display the table with a larger size
        available_properties_frame = wx.Frame(None, wx.ID_ANY, "Available Properties", size=(1200, 600))
        available_properties_panel = wx.Panel(available_properties_frame)
        available_properties_sizer = wx.BoxSizer(wx.VERTICAL)

        # Display the selected date range
        date_range_text = wx.StaticText(available_properties_panel, wx.ID_ANY,
                                        f"Selected Date Range: {start_date_str} to {end_date_str}")
        available_properties_sizer.Add(date_range_text, 0, wx.ALIGN_LEFT | wx.ALL, 10)

        # Create a data grid to display the merged data
        grid = wx.grid.Grid(available_properties_panel)
        grid.CreateGrid(len(merged_data), len(merged_data.columns))  # Remove +1 for the amenities column

        # Set column labels
        for col, column_name in enumerate(merged_data.columns):
            grid.SetColLabelValue(col, column_name)

        # Populate the grid with data
        for row, (_, row_data) in enumerate(merged_data.iterrows()):
            for col, value in enumerate(row_data):
                grid.SetCellValue(row, col, str(value))

        # Auto-size columns to fit content
        grid.AutoSizeColumns()

        available_properties_sizer.Add(grid, 1, wx.EXPAND | wx.ALL, 10)
        available_properties_panel.SetSizerAndFit(available_properties_sizer)

        # Calculate the position to center the frame on the screen
        screen_size = wx.DisplaySize()
        frame_size = available_properties_frame.GetSize()
        x = (screen_size[0] - frame_size[0]) // 2
        y = (screen_size[1] - frame_size[1]) // 2

        # Set the frame position
        available_properties_frame.SetPosition((x, y))
        available_properties_frame.Show()

    def on_back_button_click(self, event):
        from Main_Menu import MainMenu  # Import the MainMenu class from Main_Menu.py
        self.Close()
        # Create and show a new instance of the MainMenu class
        app = wx.App(False)
        main_frame = MainMenu(None, self.data, self.reviews_data, self.calendardata)
        main_frame.Show()
        app.MainLoop()


if __name__ == "__main__":
    calendar_data_file_path = os.path.join("..", 'csv files', "calendar_dec18.csv")
    data_file_path = os.path.join("..", "csv files", "listings_dec18.csv")
    data = pd.read_csv(data_file_path)  # Load your DataFrame from a CSV file
    calendardata = pd.read_csv(calendar_data_file_path)

    app = wx.App(False)
    main_frame = keyword(None, data, keyword, dtype={'price': str})  # Pass both dataframes as arguments
    main_frame.Show()
    app.MainLoop()
