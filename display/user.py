# -*- coding: utf-8 -*-

import requests
# 자리 앉기
def my_info(token):
    return request_info(token)

def request_info(token):
    # API URL
    url = "https://k11b202.p.ssafy.io/api/v1/users/me"

    # Headers에 Authorization 추가
    headers = {
        "Authorization": "Bearer " + token,  # Bearer 토큰 추가
        "Content-Type": "application/json",  # JSON 데이터 요청
    }

    # GET 요청 보내기
    response = requests.get(url, headers=headers)

    # 응답 처리
    if response.status_code == 200:
        response_data = response.json()  # JSON 응답 데이터 파싱
        print("Response Data:", response_data)

        name = response_data['data']['name'].encode('utf-8').decode('unicode_escape')
        employee_number = response_data['data']['employeeNumber']
        duty = response_data['data']['duty'].encode('utf-8').decode('unicode_escape')
        position = response_data['data']['position'].encode('utf-8').decode('unicode_escape')
        phone_number = response_data['data']['phoneNumber']
        email = response_data['data']['email']
        profile_image_url = response_data['data']['profileImageUrl']

        # 결과 출력 (확인용)
        print(f"이름: {name}")
        print(f"사원번호: {employee_number}")
        print(f"직급: {duty}")
        print(f"직책: {position}")
        print(f"전화번호: {phone_number}")
        print(f"이메일: {email}")
        print(f"프로필 이미지 URL: {profile_image_url}")
    else:
        print("Error:", response.status_code, response.text)