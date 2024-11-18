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
    return response[1]()