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