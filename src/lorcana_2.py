import os
import requests

def download_images(base_url, set_name, num_images, local_folder):
    # Ensure the local folder exists
    os.makedirs(local_folder, exist_ok=True)

    for i in range(1, num_images + 1):
        image_url = f"{base_url}/{set_name}/{i}.png"
        response = requests.get(image_url)

        if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
            with open(os.path.join(local_folder, f"{i}.png"), 'wb') as file:
                file.write(response.content)
                print(f"Downloaded {i}.png")
        elif response.status_code == 404:
            print(f"Image {i}.png not found - Status code: {response.status_code}")
        else:
            print(f"Failed to download {i}.png - Status code: {response.status_code}")

if __name__ == "__main__":
    base_url = "https://www.lorcanawiz.com/images"
    set_name = "riseofthefloodborn"
    num_images = 250
    local_folder = f"images/{set_name}/"

    download_images(base_url, set_name, num_images, local_folder)
