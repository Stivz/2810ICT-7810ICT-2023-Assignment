import pandas as pd
import matplotlib.pyplot as plt
from pandas.errors import DtypeWarning
import warnings
warnings.filterwarnings("ignore", category=DtypeWarning)

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('listings_dec18.csv')

# Get user input for the first neighborhood
neighborhood1_input = input("Enter the first neighborhood name (e.g., 'Sydney', 'Waverley'): ")

# Get user input for the second neighborhood
neighborhood2_input = input("Enter the second neighborhood name (e.g., 'Sydney', 'Waverley'): ")

# Filter rows based on the user input for the first neighborhood
neighborhood1_data = df[df['neighbourhood_cleansed'] == neighborhood1_input]

# Filter rows based on the user input for the second neighborhood
neighborhood2_data = df[df['neighbourhood_cleansed'] == neighborhood2_input]

# Check if any listings were found for the specified neighborhoods
if neighborhood1_data.empty or neighborhood2_data.empty:
    print("No listings found for one or both of the specified neighborhoods.")
else:
    # Extract the 'price' columns for the selected neighborhoods
    price1_data = neighborhood1_data['price'].str.replace('[$,]', '', regex=True).astype(float)
    price2_data = neighborhood2_data['price'].str.replace('[$,]', '', regex=True).astype(float)

    # Determine the maximum price to set as the upper limit for the histograms
    max_price = max(price1_data.max(), price2_data.max())

    # Create histograms of the 'price' data for both neighborhoods with specified range and bins
    bins = [x for x in range(0, int(max_price) + 1, 50)]
    plt.hist(price1_data, bins=20, alpha=1, label=neighborhood1_input, edgecolor='k', range=(0, max_price))
    plt.hist(price2_data, bins=20, alpha=1, label=neighborhood2_input, edgecolor='k', range=(0, max_price))

    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title(f'Price Distribution Comparison between {neighborhood1_input} and {neighborhood2_input}')
    plt.legend()
    plt.show()
