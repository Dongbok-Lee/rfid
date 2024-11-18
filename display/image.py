import requests
import os

def download_image(image_url, save_dir="images", file_name="image.png"):

    
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        image_path = os.path.join(file_name)
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return image_path
    else:
        raise Exception("Failed to download image")