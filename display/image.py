import requests
import os

def download_image(image_url, save_dir="images", file_name="image.png"):
    """
    이미지 URL을 받아 다운로드하고 저장된 경로를 반환.

    Args:
        image_url (str): 이미지 URL.
        save_dir (str): 이미지를 저장할 디렉토리 경로 (기본값: 'images').
        file_name (str): 저장할 파일 이름 (기본값: 'image.png').

    Returns:
        str: 저장된 이미지 경로.
    """
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
        raise Exception(f"이미지 다운로드 실패: {response.status_code}")

# 사용 예제
image_url = "https://sfdssafy.s3.amazonaws.com/%EC%9B%90%EB%B9%88.pngd47eed7d-564a-4b45-8773-7efa41514133"  # 실제 이미지 URL로 변경
try:
    saved_path = download_image(image_url, file_name="downloaded_image.jpg")
    print(f"이미지가 저장되었습니다: {saved_path}")
except Exception as e:
    print(f"오류 발생: {e}")