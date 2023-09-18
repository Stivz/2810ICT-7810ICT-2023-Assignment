import pandas as pd

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('reviews_dec18.csv')

# Filter rows where the review text contains the keyword "Ditto"
clean_reviews = df[df['comments'].str.contains('Ditto', case=False, na=False)]

# Extract the unique listing IDs from the filtered reviews
listing_ids_with_clean_reviews = clean_reviews['listing_id'].unique()

# Iterate through the listing IDs and display the comments
for listing_id in listing_ids_with_clean_reviews:
    comments_for_listing = clean_reviews[clean_reviews['listing_id'] == listing_id]['comments']
    print(f"Listing ID: {listing_id}")
    for comment in comments_for_listing:
        print(comment)
    print("\n")  # Add a separator between comments for different listings
