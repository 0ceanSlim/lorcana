import csv
import os
import urllib.request

# Function to download images
def download_image(image_url, folder_path, file_name):
    image_path = os.path.join(folder_path, file_name)
    urllib.request.urlretrieve(image_url, image_path)

# List all .txt files in the Deck Lists folder
txt_files = [file for file in os.listdir('Deck Lists') if file.endswith('.txt')]

# Display the list of .txt files and prompt for selection
print("Available text files:")
for index, file in enumerate(txt_files, start=1):
    print(f"{index}. {file}")

selection = input("Enter the number corresponding to the text file: ")

# Validate the user input and extract the selected text file name
try:
    selection_index = int(selection)
    if 1 <= selection_index <= len(txt_files):
        text_file_name = txt_files[selection_index - 1]

        # Extract the deck name from the text file name
        deck_name = os.path.splitext(text_file_name)[0]

        # Read CSV file and store image URLs and quantities
        image_urls = {}
        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name_title = f"{row['name']} - {row['title']}" if row['title'] else row['name']
                if name_title not in image_urls:
                    image_urls[name_title] = {'image': row['image'], 'qty': int(row['number'])}

        # Create output folder using the deck name
        output_folder = f'images/{deck_name}'
        os.makedirs(output_folder, exist_ok=True)

        # Read text file and organize images
        with open(f'Deck Lists/{text_file_name}', 'r') as textfile:
            for line in textfile:
                line = line.strip()
                parts = line.split(' - ')
                if len(parts) >= 2:
                    quantity, name, title = parts[0].split()[0], ' '.join(parts[0].split()[1:]), parts[1]
                else:
                    quantity, name = line.split()[0], ' '.join(line.split()[1:])
                    title = None  # Set title as None for entries without titles

                name_title = f"{name} - {title}" if title else name

                card_info = image_urls.get(name_title)

                if card_info:
                    qty_needed = int(quantity)
                    qty_available = card_info['qty']

                    # Download images based on quantity needed
                    for i in range(min(qty_needed, qty_available)):
                        file_name = f"{name_title} ({i + 1}).webp"
                        download_image(card_info['image'], output_folder, file_name)
    else:
        print("Invalid selection.")
except ValueError:
    print("Invalid input. Please enter a number.")
