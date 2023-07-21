from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('2train')
wholelayout = QHBoxLayout()
window.setLayout(wholelayout)
layout1 = QHBoxLayout()
bt1 = QPushButton('one')
bt2 = QPushButton('2')
layout1.addWidget(bt1)
layout1.addWidget(bt2)

layout2 = QVBoxLayout()
bt3 = QPushButton('3')
bt4 = QPushButton('4')
layout2.addWidget(bt3)
layout2.addWidget(bt4)

layout3 = QVBoxLayout()
bt5 = QPushButton('5')
bt6 = QPushButton('6')
layout3.addWidget(bt5)
layout3.addWidget(bt6)

layout4 = QVBoxLayout()
bt7 = QPushButton('7')
bt8 = QPushButton('8')
layout4.addWidget(bt5)
layout4.addWidget(bt6)

layout5 = QVBoxLayout()
bt9 = QPushButton('9')
bt10 = QPushButton('10')
bt11 = QPushButton('11')
bt12 = QPushButton('12')
layout5.addWidget(bt9)
layout5.addWidget(bt10)
layout5.addWidget(bt11)
layout5.addWidget(bt12)

wholelayout.addLayout(layout1)
wholelayout.addLayout(layout2)
wholelayout.addLayout(layout3)
wholelayout.addLayout(layout4)
wholelayout.addLayout(layout5)

window.show()

sys.exit(app.exec())