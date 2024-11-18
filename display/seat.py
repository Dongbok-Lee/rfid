import requests
# 자리 앉기
def seat_in():
    request_seat("IN_USE")

def seat_out():
    request_seat("NOT_OCCUPIED")

def request_seat(status):
    # API URL
    url = "https://k11b202.p.ssafy.io/api/v1/seats/2"

    # Bearer Token
    token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzZW1pbmtpbTE0MzJAZ21haWwuY29tIiwicm9sZSI6IlJPTEVfVVNFUiIsImlkIjoyLCJpc3MiOiJTU21hcnRPZmZpY2UiLCJpYXQiOjE3MzEzMDcxMjUsImV4cCI6MTczMjYwMzEyNX0.k1DJeQIMgaHw-MHo9QM3w8sgteb843wyV-zerGgJ0MU"

    # Headers에 Authorization 추가
    headers = {
        "Authorization": f"Bearer {token}",  # Bearer 토큰 추가
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
    else:
        print("Error:", response.status_code, response.text)

seat_in()