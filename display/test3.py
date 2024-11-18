import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('Test', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # Show  image
        self.pic = QtGui.QLabel(self)
        self.pic.setGeometry(10, 10, 800, 800)
        self.pic.setPixmap(QtGui.QPixmap("/home/lpp/Desktop/image1.png"))

        # Show button 
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.fun)
        btn.move(50, 50)


        self.setGeometry(300, 300, 2000, 1500)
        self.setWindowTitle('Tooltips')
        self.show()

    # Connect button to image updating 
    def fun(self):
        self.pic.setPixmap(QtGui.QPixmap( "/home/lpp/Desktop/image2.png"))

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()