from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys
def func():
    print('l like amos')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('8train')
btn = QPushButton()
btn.setText('上传')
btn.clicked.connect(func)
btn.setParent(window)




window.show()

sys.exit(app.exec())