from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('6train')
layout = QVBoxLayout()
window.setLayout(layout)
bt1 = QPushButton('login')
bt2 = QPushButton('delete')
layout.addWidget(bt1)
layout.addWidget(bt2)




window.show()

sys.exit(app.exec())