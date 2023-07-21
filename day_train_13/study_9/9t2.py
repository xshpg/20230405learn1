from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys
def func():
    print('hallo world')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('2train')
btn = QPushButton()
btn.setText('注册')
btn.clicked.connect(func)
btn.setParent(window)





window.show()

sys.exit(app.exec())