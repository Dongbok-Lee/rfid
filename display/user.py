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
    if response.status_code == 200:
        data = response.json()  # JSON 응답 데이터 파싱
        print(data)
        return data
    else:
        print("Error:", response.status_code, response.text)

my_info("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0eXBvb24wODIwQGdtYWlsLmNvbSIsInJvbGUiOiJST0xFX1VTRVIiLCJpZCI6MjksImlzcyI6IlNTbWFydE9mZmljZSIsImlhdCI6MTczMTkyOTYzNiwiZXhwIjoxNzMzMjI1NjM2fQ.DAaJSnZ3gyy0IWx0oBaVrs8lPdvJQ4sikVVa5cHkKaA")
