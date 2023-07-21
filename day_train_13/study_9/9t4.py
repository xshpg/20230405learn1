from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys
def func():
    print('hi misss old boy')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('4train')
btn = QPushButton()
btn.setText('登录')
btn.clicked.connect(func)
btn.setParent(window)





window.show()

sys.exit(app.exec())