# -*- coding: utf-8 -*-

import sys
import time
from PyQt4.QtGui import QApplication, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QWidget, QPushButton, QPixmap, QFont, QFontDatabase
from PyQt4.QtCore import QThread, pyqtSignal, Qt
import read
import user

user_duty = ""
user_name = ""
user_phone_number = ""
user_profile_image_url = ""
user_employee_number = ""
user_position = ""
user_email = ""


class SignalThread(QThread):



    toggle_signal = pyqtSignal()  # 신호 정의

    def run(self):

        global user_duty
        global user_name
        global user_phone_number
        global user_profile_image_url
        global user_employee_number
        global user_position
        global user_email

        while True:
            time.sleep(2)
            token = read.read_token()
            info = user.my_info(token)
            user_duty = info[u'data'][u'duty']
            user_name = info[u'data'][u'name']
            user_phone_number = info[u'data'][u'phoneNumber']
            user_profile_image_url = info[u'data'][u'profileImageUrl']
            user_employee_number = info[u'data'][u'employeeNumber']
            user_position = info[u'data'][u'position']
            user_email =  info[u'data'][u'email']

            print(user_duty)
            print(user_name)
            print(user_phone_number)
            print(user_profile_image_url)
            self.toggle_signal.emit()  # 신호 방출

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(unicode("전자 명함","utf-8"))
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #f4f4f4;")  # 배경색 설정

        # 메인 위젯 설정
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        nanumB = QFontDatabase.addApplicationFont("./font/NanumSquareB.otf")
        nanumL = QFontDatabase.addApplicationFont("./font/NanumSquareL.otf")
        nanumB_font = QFontDatabase.applicationFontFamilies(nanumB)[0]
        nanumL_font = QFontDatabase.applicationFontFamilies(nanumL)[0]

        # 레이아웃 설정
        main_layout = QHBoxLayout(self.central_widget)

        # 사진 영역
        self.photo_label = QLabel()
        self.photo_label.setPixmap(
            QPixmap("user_photo.jpg").scaled(280, 280, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        self.photo_label.setAlignment(Qt.AlignCenter)

        # 정보 영역
        info_layout = QVBoxLayout()

        # 이름
        self.name_label = QLabel(unicode(user_name,'utf-8'))
        self.name_label.setFont(QFont(nanumB_font, 18, QFont.Bold))
        self.name_label.setStyleSheet("color: #333333;")
        self.name_label.setAlignment(Qt.AlignCenter)

        # 사원번호
        self.id_label = QLabel("사원번호: " + unicode(user_employee_number,'utf-8'))
        self.id_label.setFont(QFont(nanumB_font, 12))
        self.id_label.setStyleSheet("color: #555555;")
        self.id_label.setAlignment(Qt.AlignCenter)

        # 팀 이름
        self.team_label = QLabel("직급: " + unicode(user_duty,'utf-8'))
        self.team_label.setFont(QFont(nanumB_font, 12))
        self.team_label.setStyleSheet("color: #555555;")
        self.team_label.setAlignment(Qt.AlignCenter)

        # 직책
        self.position_label = QLabel("직책: " + unicode(user_position,'utf-8'))
        self.position_label.setFont(QFont(nanumB_font, 12))
        self.position_label.setStyleSheet("color: #555555;")
        self.position_label.setAlignment(Qt.AlignCenter)

        # 전화번호
        self.phone_label = QLabel("전화번호: " + unicode(user_phone_number,'utf-8'))
        self.phone_label.setFont(QFont(nanumB_font, 12))
        self.phone_label.setStyleSheet("color: #555555;")
        self.phone_label.setAlignment(Qt.AlignCenter)

        # 이메일
        self.email_label = QLabel("이메일: " + unicode(user_email,'utf-8'))
        self.email_label.setFont(QFont(nanumB_font, 12))
        self.email_label.setStyleSheet("color: #555555;")
        self.email_label.setAlignment(Qt.AlignCenter)

        # 정보 레이아웃에 추가
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.id_label)
        info_layout.addWidget(self.team_label)
        info_layout.addWidget(self.position_label)
        info_layout.addWidget(self.phone_label)
        info_layout.addWidget(self.email_label)

        self.layout.addWidget(self.photo_label, alignment=Qt.AlignLeft)  # 사진 왼쪽 정렬
        self.layout.addLayout(info_layout)

        # 최상위 이미지 레이블 생성
        self.image_label = QLabel(self)
        self.image_label.setPixmap(
            QPixmap("user_image.jpg").scaled(
                self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
        )
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setGeometry(0, 0, self.width(), self.height())

        # 이미지 표시 여부 초기화
        self.image_visible = True

        # 스레드 시작
        self.signal_thread = SignalThread()
        self.signal_thread.toggle_signal.connect(self.toggle_image)  # 신호 연결
        self.signal_thread.start()

        # 창 크기 조정 시 이미지 업데이트
        self.central_widget.resizeEvent = self.resize_event

    def toggle_image(self):

        global user_duty
        global user_name
        global user_phone_number
        global user_profile_image_url
        global user_employee_number
        global user_position
        global user_email

        """이미지를 숨기거나 보이게 하는 함수."""
        print(user_name)
        print(user_duty)
        if self.image_visible:
            self.image_label.hide()  # 이미지 숨기기
            self.name_label.setText("이름: " + user_name)
            self.id_label.setText("사원번호: " + user_employee_number)
            self.team_label.setText("직급: " + user_duty)
            self.position_label.setText("직책: " + user_position)
            self.phone_label.setText("전화번호: " + user_phone_number)
            self.email_label.setText("이메일: " + user_email)
        else:
            self.image_label.show()  # 이미지 보이기
        self.image_visible = not self.image_visible

    def resize_event(self, event):
        """창 크기 변경 시 이미지 크기 재조정."""
        self.image_label.setPixmap(
            QPixmap("nfc.jpg").scaled(
                self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
        )
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        super(MainWindow, self).resizeEvent(event)

    def closeEvent(self, event):
        """창 종료 시 스레드 종료."""
        self.signal_thread.terminate()  # 스레드 강제 종료 (주의: 안전하게 종료하려면 추가 로직 필요)
        self.signal_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
