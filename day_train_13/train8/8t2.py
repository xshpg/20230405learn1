from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('2bian')
btn = QPushButton()
btn.setText('登录')
icon = QIcon('10.png')
btn.setIcon(icon)
btn.setParent(window)





window.show()

sys.exit(app.exec())