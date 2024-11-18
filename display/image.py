import requests
import os

def download_image(image_url, save_dir="images", file_name="image.png"):

    # 디렉토리 생성
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 이미지 요청
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        image_path = os.path.join(save_dir, file_name)
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return image_path
    else:
        raise Exception("Failed to download image")