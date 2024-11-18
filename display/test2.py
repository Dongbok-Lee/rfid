# -*- coding: utf-8 -*-
import sys
from qtpy.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from qtpy.QtWebEngineWidgets import QWebEngineView


class NaverBrowser(QMainWindow):
    def __init__(self):
        super(NaverBrowser, self).__init__()
        self.setWindowTitle("네이버 보기")
        self.setGeometry(100, 100, 800, 600)

        # 메인 위젯 설정
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 레이아웃
        layout = QVBoxLayout(self.central_widget)

        # QWebEngineView를 사용하여 웹 페이지 로드
        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.naver.com")  # 네이버 주소
        layout.addWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaverBrowser()
    window.show()
    sys.exit(app.exec_())
