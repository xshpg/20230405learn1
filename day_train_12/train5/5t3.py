from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QMovie


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('3bian')
label = QLabel()
pixmap = QPixmap('10.png')
label.setPixmap(pixmap)
window.setFixedSize(pixmap.width(),pixmap.height())
label.setParent(window)







window.show()

sys.exit(app.exec())