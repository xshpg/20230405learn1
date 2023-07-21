from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QRadioButton
from PyQt5.QtGui import QIcon


import sys

def func(ck):
    print(ck)

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('3train')
layout = QHBoxLayout()
window.setLayout(layout)
rb1 = QRadioButton('man')
rb2 = QRadioButton('women')
layout.addWidget(rb1)
layout.addWidget(rb2)
rb1.toggled.connect(func)


window.show()

sys.exit(app.exec())