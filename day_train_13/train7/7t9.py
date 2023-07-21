from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('9bian')
edit = QTextEdit()
edit.setPlainText('发不内容')
edit.clear()
edit.setParent(window)




window.show()

sys.exit(app.exec())