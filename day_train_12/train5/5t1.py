from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QMovie


import sys


app = QApplication(sys.argv)

window = QWidget()

icon = QIcon('10.png')
window.setWindowTitle('图片展示')

label = QLabel()
pixmap = QPixmap('10.png')
label.setPixmap(pixmap)
label.setParent(window)

window.setFixedSize(pixmap.width(),pixmap.height())



window.show()

sys.exit(app.exec())