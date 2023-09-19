import wx
import wx.xrc
import pandas as pd
import tkinter as tk
from tkinter import ttk
import os

class listings(wx.Frame):

    def __init__(self, parent, data):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1980, 1080), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
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
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_back_button_click)

        self.data = data
        data_file_path = os.path.join("csv files", "listings_dec18.csv")
        self.df = pd.read_csv(data_file_path)
        # Create a function to update the table based on user input
        def update_table():
            selected_neighborhood = self.neighborhood_var.get()
            filtered_data = self.df[self.df['neighbourhood_cleansed'] == selected_neighborhood]

            # Clear the existing table
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert data into the table
            for index, row in filtered_data.iterrows():
                self.tree.insert("", "end", values=(
                    row["name"], row["neighbourhood_cleansed"], row["property_type"], row["price"], row["listing_url"]))

        # Create a tkinter window
        root = tk.Tk()
        root.title("Listings Table")

        # Create a frame for user input
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10)

        # Create a label and a dropdown for selecting a neighborhood
        neighborhood_label = ttk.Label(input_frame, text="Select a Neighborhood:")
        neighborhood_label.grid(row=0, column=0, padx=10, pady=5)

        # Remove quotation marks from neighborhood names
        neighborhoods = [neighborhood.strip("'") for neighborhood in self.df['neighbourhood_cleansed'].unique()]

        self.neighborhood_var = tk.StringVar()
        neighborhood_dropdown = ttk.Combobox(input_frame, textvariable=self.neighborhood_var, values=neighborhoods)
        neighborhood_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Create a button to update the table
        update_button = ttk.Button(input_frame, text="Update Table", command=update_table)
        update_button.grid(row=0, column=2, padx=10, pady=5)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Treeview widget (table)
        self.tree = ttk.Treeview(root, columns=("Name", "Neighborhood", "Property Type", "Price", "Listing URL"),
                                yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        # Set column headings
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Neighborhood")
        self.tree.heading("#3", text="Property Type")
        self.tree.heading("#4", text="Price")
        self.tree.heading("#5", text="Listing URL")

        # Pack the Treeview widget
        self.tree.pack()

        # Start the tkinter main loop
        root.mainloop()

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
    main_frame = listings(None, data)  # Pass the DataFrame as an argument
    main_frame.Show()
    app.MainLoop()
