from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('five')

layout = QHBoxLayout()
window.setLayout(layout)
bt1 = QPushButton('login')
bt2 = QPushButton('update')
layout.addWidget(bt1)
layout.addWidget(bt2)


window.show()

sys.exit(app.exec())