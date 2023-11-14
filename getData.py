from bs4 import BeautifulSoup
import csv
import requests
import json

# Iterate through card IDs from 1 to 448
for card_id in range(1, 449):
    # URL of the HTML page for each card ID
    url = f'https://lorcania.com/cards/{card_id}'

    # Fetch the HTML content
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the div containing the data
        data_div = soup.find('div', {'id': 'app'})

        # Extract the data-page attribute
        data_page = data_div['data-page']

        # Convert the data-page attribute from JSON to Python dictionary
        data_json = json.loads(data_page)

        # Extract card information
        data_draft = data_json['props']['card']

        # Define headers for CSV file
        if card_id == 1:  # Write headers only for the first card
            headers = list(data_draft.keys())
            with open('data_draft.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

        # Define rows for CSV file
        rows = [list(data_draft.values())]

        # Append data to CSV file
        with open('data_draft.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"Card {card_id} information added to CSV file.")
    else:
        print(f"Card {card_id} not found.")

print("CSV file created successfully!")
