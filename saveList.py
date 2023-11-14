from selenium import webdriver
import csv
import requests
import os
import zipfile
from io import BytesIO
from selenium.webdriver.common.by import By


def scrape_and_save_data(url, output_csv_path):
    # Define the directory path and URLs for Chrome and Chromedriver
    chrome_directory = 'c:/tmp/chrome'
    chrome_exe_path = 'c:/tmp/chrome/chrome-win64/chrome.exe'  # Modify this path as needed
    chrome_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.92/win64/chrome-win64.zip'

    # Check if the Chrome directory exists, and if not, create it
    if not os.path.exists(chrome_directory):
        os.makedirs(chrome_directory)

    # Check if Chrome.exe and Chromedriver.exe exist in the directory
    if not os.path.exists(os.path.join(chrome_exe_path)):
        # Download and extract Chrome
        chrome_response = requests.get(chrome_url)
        with zipfile.ZipFile(BytesIO(chrome_response.content), 'r') as zip_ref:
            zip_ref.extractall(chrome_directory)

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_exe_path

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the webpage
    driver.get(url)

    # Find all elements with the specified class names
    name_elements = driver.find_elements(By.CSS_SELECTOR, '.card-list-name-txt')
    number_elements = driver.find_elements(By.CSS_SELECTOR, '.card-list-num')


    # Extract data and store it in a list of dictionaries
    data = [{'Name': name.text, 'Number': number.text} for name, number in zip(name_elements, number_elements)]

    # Save data to CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name', 'Number']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)



    # Close the browser
    driver.quit()

if __name__ == "__main__":
    # Replace these values with your actual URL, ChromeDriver path, and output CSV path
    webpage_url = 'https://www.lorcanawiz.com/cards/the-first-chapter'
    output_csv_path = 'setlist1.csv'

    # Call the function to scrape and save data
    scrape_and_save_data(webpage_url, output_csv_path)
