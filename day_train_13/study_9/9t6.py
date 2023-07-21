from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys
def func():
    print('i am fine thank you')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('6train')
btn = QPushButton()
btn.setText('查询')
btn.clicked.connect(func)
btn.setParent(window)




window.show()

sys.exit(app.exec())