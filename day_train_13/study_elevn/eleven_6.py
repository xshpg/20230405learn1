from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('six')
layout = QHBoxLayout()
window.setLayout(layout)
bt1 = QPushButton('login')
bt2 = QPushButton('register')
layout.addWidget(bt1)
layout.addWidget(bt2)


window.show()

sys.exit(app.exec())