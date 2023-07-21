from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('布局嵌套')
wholelayout = QHBoxLayout()
window.setLayout(wholelayout)
layout1 = QHBoxLayout()
bt1 = QPushButton('1')
bt2 = QPushButton('2')
layout1.addWidget(bt1)
layout1.addWidget(bt2)
layout2 = QVBoxLayout()
btn3 = QPushButton('3')
btn4 = QPushButton('4')
layout2.addWidget(btn3)
layout2.addWidget(btn4)

layout3 = QVBoxLayout()
btn5 = QPushButton('5')
btn7 = QPushButton('7')
layout3.addWidget(btn5)
layout3.addWidget(btn7)

layout4 = QVBoxLayout()
btn6 = QPushButton('6')
btn8 = QPushButton('8')
layout4.addWidget(btn6)
layout4.addWidget(btn8)

layout5 = QVBoxLayout()
btn9 = QPushButton('9')
btn10 = QPushButton('10')
btn11 = QPushButton('11')
btn12 = QPushButton('12')
layout5.addWidget(btn9)
layout5.addWidget(btn10)
layout5.addWidget(btn11)
layout5.addWidget(btn12)

wholelayout.addLayout(layout1)
wholelayout.addLayout(layout2)
wholelayout.addLayout(layout3)
wholelayout.addLayout(layout4)
wholelayout.addLayout(layout5)

window.show()

sys.exit(app.exec())