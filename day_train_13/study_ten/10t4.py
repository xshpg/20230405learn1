from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('4train')
btn = QPushButton('关闭窗口')
btn.setParent(window)
btn.clicked.connect(QApplication.quit)




window.show()

sys.exit(app.exec())