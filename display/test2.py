# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt4.QtCore import Qt

class SimpleUI(QMainWindow):
    def __init__(self):
        super(SimpleUI, self).__init__()

        # 윈도우 설정
        self.setWindowTitle("PyQt4 간단 UI")
        self.setGeometry(100, 100, 400, 300)

        # 메인 위젯 및 레이아웃
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 라벨
        self.label = QLabel("안녕하세요! 버튼을 눌러보세요.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # 버튼
        self.button = QPushButton("클릭", self)
        self.button.clicked.connect(self.on_button_click)  # 버튼 클릭 이벤트 연결
        self.layout.addWidget(self.button)

    def on_button_click(self):
        """버튼 클릭 시 호출되는 메서드"""
        self.label.setText("버튼이 눌렸습니다!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec_())
