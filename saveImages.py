import os
import pandas as pd
import requests
import re

# Function to clean filename by removing problematic characters
def clean_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '', filename)

# Read the CSV file
data = pd.read_csv('data.csv')

# Create a folder named 'images' if it doesn't exist
images_folder = 'images'
os.makedirs(images_folder, exist_ok=True)

# Iterate through the rows
for index, row in data.iterrows():
    card_set_id = row['card_set_id']
    card_id = row['id']
    name = row['name']
    image_url = row['image']

    # Create a folder for the card_set_id if it doesn't exist
    card_set_folder = os.path.join(images_folder, str(card_set_id))
    os.makedirs(card_set_folder, exist_ok=True)

    # Get the image
    response = requests.get(image_url)
    if response.status_code == 200:
        # Clean the filename
        image_filename = clean_filename(f"{card_id} - {name}.webp")  # Adjust the extension if needed
        image_path = os.path.join(card_set_folder, image_filename)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved: {image_filename}")
    else:
        print(f"Failed to download image for {name}")
