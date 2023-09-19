import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('../csv files/listings_dec18.csv')


# Create a function to update the table based on user input
def update_table():
    selected_neighborhood = neighborhood_var.get()
    filtered_data = df[df['neighbourhood_cleansed'] == selected_neighborhood]

    # Clear the existing table
    for item in tree.get_children():
        tree.delete(item)

    # Insert data into the table
    for index, row in filtered_data.iterrows():
        tree.insert("", "end", values=(
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
neighborhoods = [neighborhood.strip("'") for neighborhood in df['neighbourhood_cleansed'].unique()]

neighborhood_var = tk.StringVar()
neighborhood_dropdown = ttk.Combobox(input_frame, textvariable=neighborhood_var, values=neighborhoods)
neighborhood_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Create a button to update the table
update_button = ttk.Button(input_frame, text="Update Table", command=update_table)
update_button.grid(row=0, column=2, padx=10, pady=5)

# Create a scrollbar
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Treeview widget (table)
tree = ttk.Treeview(root, columns=("Name", "Neighborhood", "Property Type", "Price", "Listing URL"),
                    yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)

# Set column headings
tree.heading("#1", text="Name")
tree.heading("#2", text="Neighborhood")
tree.heading("#3", text="Property Type")
tree.heading("#4", text="Price")
tree.heading("#5", text="Listing URL")

# Pack the Treeview widget
tree.pack()

# Start the tkinter main loop
root.mainloop()