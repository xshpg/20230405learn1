from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys
def func():
    print('i can kill orange')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('5train')

btn = QPushButton()
btn.setText('检索')
btn.clicked.connect(func)
btn.setParent(window)




window.show()

sys.exit(app.exec())