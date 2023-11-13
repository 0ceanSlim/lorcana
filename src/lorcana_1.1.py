import os
import requests

def download_images(base_url, set_name, num_images, local_folder):
    # Ensure the local folder exists
    os.makedirs(local_folder, exist_ok=True)

    for i in range(205, num_images + 1):
        image_url = f"{base_url}/{set_name}/{i}.png" #might have to add the set tag here
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(os.path.join(local_folder, f"{i}.png"), 'wb') as file:
                file.write(response.content)
                print(f"Downloaded {i}.png")
        else:
            print(f"Failed to download {i}.png - Status code: {response.status_code}")

if __name__ == "__main__":
    base_url = "https://www.lorcanawiz.com/images" #/thefirstchapter/TFC-205.png
    set_name = "thefirstchapter"
    num_images = 216
    local_folder = f"images/{set_name}/"

    download_images(base_url, set_name, num_images, local_folder)
