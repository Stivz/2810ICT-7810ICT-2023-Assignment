import wx
import wx.adv
import wx.xrc
import pandas as pd
import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal
from datetime import datetime
import os
import webbrowser
class TopRatedFrame(wx.Frame):
    def __init__(self, parent, data, reviews_data, calendardata):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1980, 1080), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # Create the date pickers and set initial values to valid default dates
        self.start_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                       wx.DefaultSize, style=wx.adv.DP_DEFAULT)
        self.end_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                     wx.DefaultSize, style=wx.adv.DP_DEFAULT)

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

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Back To Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer51.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, 5)

        bSizer18.Add(gSizer51, 1, 0, 5)

        bSizer12.Add(bSizer18, 1, wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Sydney Stayz", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetFont(
            wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer15.Add(self.m_staticText7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Top Rated", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer15.Add(self.m_staticText2, 0, wx.ALIGN_CENTER, 5)

        bSizer12.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer2 = wx.GridSizer(0, 1, 0, 0)


        gSizer4 = wx.GridSizer(0, 1, 0, 0)
        #
        self.m_button15 = wx.Button(self, wx.ID_ANY, u"View Top Rated Properties", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button15, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer19.Add(gSizer4, 1, 0, 5)

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
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_back_button_click)

        self.data = data  # Store the DataFrame for later use
        self.reviews_data = reviews_data
        self.calendardata = calendardata
        # self.filtered_data = None

        # Create a wx.Panel to contain the tkinter table
        self.table_frame = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.table_frame.Show()

        # Create a button for showing the tkinter table
        self.m_button15.Bind(wx.EVT_BUTTON, self.show_table)




    def create_table(self):
        # Create a tkinter window for the table
        self.table_window = tk.Tk()
        self.table_window.title("Top Rated Table")

        # Get the screen width and height
        screen_width = self.table_window.winfo_screenwidth()
        screen_height = self.table_window.winfo_screenheight()

        self.table_window.geometry("1300x400+280+345")  # Adjust the size and coordinates as needed

        # Create a frame for user input
        input_frame = ttk.Frame(self.table_window)
        input_frame.pack(pady=10)

        # Create a label and a dropdown for selecting a neighborhood
        neighborhood_label = ttk.Label(input_frame, text="Select a Neighbourhood:")
        neighborhood_label.grid(row=0, column=0, padx=10, pady=5)

        # Remove quotation marks from neighborhood names
        neighborhoods = [neighborhood.strip("'") for neighborhood in self.data['neighbourhood_cleansed'].unique()]

        self.neighborhood_var = tk.StringVar()
        neighborhood_dropdown = ttk.Combobox(input_frame, textvariable=self.neighborhood_var, values=neighborhoods)
        neighborhood_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Create a button to update the table
        update_button = ttk.Button(input_frame, text="Update Table", command=self.update_table)
        update_button.grid(row=0, column=2, padx=(5, 60), pady=5)


        # Create a Start Date Entry widget using DateEntry
        self.start_date_str = tk.StringVar()

        start_date_entry = tkcal.DateEntry(input_frame, textvariable=self.start_date_str, date_pattern='yyyy-mm-dd')
        start_date_entry.grid(row=2, column=1, padx=(5, 50), pady=5)  # Adjust the padding as needed

        # Create a label for "to" between start and end dates
        to_label = ttk.Label(input_frame, text="to")
        to_label.grid(row=2, column=1, padx=(5, 20), pady=5, sticky="e")  # Adjust the padding as needed

        self.end_date_str = tk.StringVar()
        # Create an End Date Entry widget using DateEntry
        end_date_entry = tkcal.DateEntry(input_frame, textvariable=self.end_date_str, date_pattern='yyyy-mm-dd')
        end_date_entry.grid(row=2, column=2, padx=(5, 50), pady=5)

        # Create a "Confirm" button for date range
        # confirm_date_button = ttk.Button(input_frame, text="Confirm Date Range", command=self.apply_date_range_filter)
        # confirm_date_button.grid(row=3, column=1, padx=(5, 60), pady=5)



        # Create a scrollbar
        scrollbar = ttk.Scrollbar(self.table_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a label and a dropdown for selecting a property type
        property_type_label = ttk.Label(input_frame, text="Select a Property Type (Optional):")
        property_type_label.grid(row=1, column=0, padx=10, pady=5)

        # Remove quotation marks from property type names
        property_types = [ptype.strip("'") for ptype in self.data['property_type'].unique()]

        self.property_type_var = tk.StringVar()
        property_type_dropdown = ttk.Combobox(input_frame, textvariable=self.property_type_var, values=property_types)
        property_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Create a Treeview widget (table)
        self.tree = ttk.Treeview(self.table_window,
                                 columns=("Name", "Neighbourhood", "Property Type", "Review Scores Rating", "Date", "Listing URL"),
                                 yscrollcommand=scrollbar.set, show="headings")
        scrollbar.config(command=self.tree.yview)

        # Set column headings
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Neighbourhood")
        self.tree.heading("#3", text="Property Type")
        self.tree.heading("#4", text="Review Scores Rating")
        self.tree.heading("#5", text="Date")
        self.tree.heading("#6", text="Listing URL")

        self.tree.column("#1", width=300)
        self.tree.column("#5", width=100)  # Adjust the width for the date column
        self.tree.column("#6", width=270)

        # Pack the Treeview widget
        self.tree.pack()

        # Bind the double-click event to open the URL
        self.tree.bind("<Double-1>", self.open_url)

        # Start the tkinter main loop
        self.table_window.mainloop()


    def open_url(self, event):
        item = self.tree.selection()
        if item:
            url = self.tree.item(item,"values")[3]  # click URL in the fifth column (index 4)

            if url:
                webbrowser.open(url)  # Open the URL in the default web browser
    def show_table(self, event=None):
        # Refresh the layout
        self.Layout()

        # Check if the tkinter table has already been created
        if not hasattr(self, 'root'):
            # Start the tkinter table creation within the panel
            self.create_table()

    # def apply_date_range_filter(self):
    #     start_date_str = self.start_date_str.get()
    #     end_date_str = self.end_date_str.get()
    #
    #     print("Start Date:", start_date_str)
    #     print("End Date:", end_date_str)
    #
    #     if start_date_str and end_date_str:
    #         # Convert the formatted strings to datetime objects
    #         start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    #         end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    #
    #         # Filter both dataframes based on the date range
    #         # Convert 'date' column in calendardata to datetime objects for comparison
    #         self.calendardata['date'] = pd.to_datetime(self.calendardata['date'])
    #         filtered_listing_ids = self.calendardata[
    #             (self.calendardata['date'] >= start_date) &
    #             (self.calendardata['date'] <= end_date)
    #             ]['listing_id']
    #
    #         self.filtered_data = self.data[
    #             self.data['id'].isin(filtered_listing_ids)
    #         ]
    #
    #         self.filtered_reviews_data = self.reviews_data[
    #             self.reviews_data['listing_id'].isin(self.filtered_data['id'])
    #         ]
    #
    #
    #         # After filtering, update the table to display the filtered results
    #         self.update_table()

    def update_table(self):
        selected_neighborhood = self.neighborhood_var.get()
        selected_property_type = self.property_type_var.get()

        start_date_str = self.start_date_str.get()
        end_date_str = self.end_date_str.get()
        print("Updating table...")
        print("Start Date:", start_date_str)
        print("End Date:", end_date_str)




        if selected_neighborhood:
            if selected_property_type:
                filtered_data = self.data[
                    (self.data['neighbourhood_cleansed'] == selected_neighborhood) &
                    (self.data['property_type'] == selected_property_type)
                    ]
            else:
                filtered_data = self.data[self.data['neighbourhood_cleansed'] == selected_neighborhood]
        else:
            filtered_data = pd.DataFrame()

        # Sort the data by "review_scores_rating" in descending order
        filtered_data = filtered_data.sort_values(by="review_scores_rating", ascending=False)

        for item in self.tree.get_children():
            try:
                self.tree.delete(item)
            except:
                pass  # Ignore any errors when deleting items

            # Check if filtered_data is not None
            if filtered_data is not None:
                # Clear the current table
                for item in self.tree.get_children():
                    self.tree.delete(item)

        for index, row in filtered_data.iterrows():
            listing_id = row["id"]
            listing_date = self.calendardata[self.calendardata['listing_id'] == listing_id]['date'].values[0]

            self.tree.insert("", "end", values=(
                row["name"], row["neighbourhood_cleansed"], row["property_type"], row["review_scores_rating"],
                listing_date, row["listing_url"]))


    def on_back_button_click(self, event):
        from Main_Menu import MainMenu  # Import the MainMenu class from Main_Menu.py
        self.Close()
        # Create and show a new instance of the MainMenu class
        app = wx.App(False)
        main_frame = MainMenu(None, self.data, self.reviews_data, self.calendardata)
        main_frame.Show()
        app.MainLoop()

if __name__ == "__main__":
    data_file_path = os.path.join("..", "csv files", "listings_dec18.csv")
    reviews_file_path = os.path.join("..", "csv files", "reviews_dec18.csv")
    calendar_data_file_path = os.path.join("..", 'csv files', "calendar_dec18.csv")
    data = pd.read_csv(data_file_path)  # Load your DataFrame from a CSV file
    reviews_data = pd.read_csv(reviews_file_path)  # Load your DataFrame from the reviews CSV file
    calendardata = pd.read_csv(calendar_data_file_path)
    app = wx.App(False)
    main_frame = TopRatedFrame(None, data, reviews_data, calendardata)  # Pass the DataFrame as an argument
    main_frame.Show()
    app.MainLoop()
