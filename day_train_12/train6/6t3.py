from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('3bian')
edit = QLineEdit()
edit.setEchoMode(QLineEdit.Normal)
edit.setParent(window)





window.show()

sys.exit(app.exec())