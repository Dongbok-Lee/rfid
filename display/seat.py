# -*- coding: utf-8 -*-

import requests
# 자리 앉기
def seat_in(token):
    return request_seat("IN_USE", token)

def seat_out(token):
    return request_seat("VACANT", token)

def request_seat(status, token):
    # API URL
    url = "https://k11b202.p.ssafy.io/api/v1/seats/26"

    # Headers에 Authorization 추가
    headers = {
        "Authorization": "Bearer " + token,  # Bearer 토큰 추가
        "Content-Type": "application/json",  # JSON 데이터 요청
    }

    body = {
        "status": status  # IN_USE, VACANT, UNAVAILABLE, NOT_OCCUPIED
    }

    # GET 요청 보내기
    response = requests.patch(url, headers=headers, json=body)

    # 응답 처리
    if response.status_code == 200:
        data = response.json()  # JSON 응답 데이터 파싱
        print("Response Data:", data)
        return True
    else:
        print("Error:", response.status_code, response.text)
        return False