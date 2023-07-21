from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('多汗输入框')
edit = QTextEdit()
# edit.setPlainText('发内容')
edit.setPlaceholderText('请输入内容')
edit.clear()




edit.setParent(window)






window.show()

sys.exit(app.exec())