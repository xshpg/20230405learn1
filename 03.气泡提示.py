from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()

icon = QIcon('10.png')
window.setWindowTitle('黑马窗口')


window.setWindowIcon(icon)


window.setFixedSize(600,800)
window.setToolTip('这是第一个窗口')

window.show()

sys.exit(app.exec())