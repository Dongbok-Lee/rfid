# 원본 데이터
data = ('Response Data:', {
    u'status': 200,
    u'msg': u'내 정보 조회에 성공했습니다.',
    u'data': {
        u'duty': u'주임',
        u'status': u'OFF_DUTY',
        u'name': u'이동복',
        u'phoneNumber': None,
        u'userId': 29,
        u'profileImageUrl': u'https://sfdssafy.s3.amazonaws.com/동복.pngd5863b2d-d43d-4989-9f15-0da9af50f956',
        u'role': u'USER',
        u'employeeNumber': u'S24000006',
        u'position': u'개발자',
        u'email': u'typoon0820@gmail.com'
    }
})

print(data[1])


# 사용자 정보 변수에 담기


# 확인
print("Response Label:", response_label)
print("Response Status:", response_status)
print("Response Message:", response_message)
print("User Duty:", user_duty)
print("User Status:", user_status)
print("User Name:", user_name)
print("User Phone Number:", user_phone_number)
print("User ID:", user_id)
print("User Profile Image URL:", user_profile_image_url)
print("User Role:", user_role)
print("User Employee Number:", user_employee_number)
print("User Position:", user_position)
print("User Email:", user_email)