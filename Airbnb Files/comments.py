import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table  # Import the table module


df = pd.read_csv('reviews_dec18.csv')

# Filter rows where the review text contains the keyword "Ditto"
clean_reviews = df[df['comments'].str.contains('Ditto', case=False, na=False)]

# Select the columns of interest
selected_columns = ["listing_id", "id", "date", "reviewer_id", "reviewer_name"]

# Create a table with the selected columns and hide the index column
table_data = clean_reviews[selected_columns]
table_data.reset_index(drop=True, inplace=True)  # Reset the index and drop the old index

# Create a figure and axis for displaying the table
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')  # Turn off the axis

# Create the table and display it
tab = table(ax, table_data, loc='center', cellLoc='center', colWidths=[0.2, 0.2, 0.2, 0.2, 0.2])
tab.auto_set_font_size(False)
tab.set_fontsize(10)
tab.scale(1, 1.5)  # Adjust the table size as needed

# Show the table in a pop-up window
plt.show()
