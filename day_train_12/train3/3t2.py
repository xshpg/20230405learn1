from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('这是三课二遍')
icon =  QIcon('10.png')
window.setWindowIcon(icon)
window.setFixedSize(600,800)
window.setToolTip('三遍了')




window.show()

sys.exit(app.exec())