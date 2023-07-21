from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('水平布局')
layout = QHBoxLayout()
window.setLayout(layout)
bt1 = QPushButton('1')
bt2 = QPushButton('2')
bt3 = QPushButton('3')
bt4 = QPushButton('4')
bt5 = QPushButton('5')

layout.addWidget(bt1)
layout.addWidget(bt2)
layout.addWidget(bt3)
layout.addWidget(bt4)
layout.addWidget(bt5)




window.show()

sys.exit(app.exec())