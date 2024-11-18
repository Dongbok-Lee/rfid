#-*- coding: utf-8 -*-
#-*- coding: euc-kr -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#5도 동일하게 QtCore

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        Title = QLabel(unicode("솔직하게 작성해 주세요",'utf-8'))
        ID = QLabel("ID")
        IDText = QLineEdit()
        Gender = QLabel(unicode("성별", 'utf-8'))
        GenderGroupBox = QGroupBox()
        Men = QRadioButton(unicode("남자", 'utf-8')) 
        Women = QRadioButton(unicode("여자", 'utf-8'))
        Age = QLabel(unicode("나이", 'utf-8'))
        age = QComboBox()
        age.addItems(["22", "23", "24", "25", "26"])
        Capa = QLabel(unicode("주량", 'utf-8'))
        capa = QSlider(Qt.Horizontal)
        capa.setMinimum(0)
        capa.setMaximum(4)
        capa.setValue(2)
        capa.setTickPosition(QSlider.TicksBelow)
        capa.setTickInterval(1)
        Text = QLabel(unicode("자기소개","utf-8"))
        test = QTextEdit()
        Ok = QPushButton("Submit")

        layout = QGridLayout()
        layout.addWidget(Title, 0, 0,)
        layout.addWidget(ID, 1, 0)
        layout.addWidget(IDText, 1, 1, 1, 2)
        layout.addWidget(Gender, 2, 0)
        layout.addWidget(GenderGroupBox, 2, 1, 1, 2)
        layout.addWidget(Men, 2, 1)
        layout.addWidget(Women, 2, 2)
        layout.addWidget(Age, 3, 0)
        layout.addWidget(age, 3, 1, 1, 2)
        layout.addWidget(Capa, 4, 0)
        layout.addWidget(capa, 4, 1, 1, 2)
        layout.addWidget(Text, 5, 0, 1, 3)
        layout.addWidget(test, 6, 1)
        layout.addWidget(Ok, 7, 1)



        self.setLayout(layout)

app = QApplication([])
dialog = MyDialog()
dialog.setWindowTitle(unicode("자기소개서",'utf-8'))
dialog.show()
app.exec_()