from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('第三课练习1')
icon = QIcon('10.png')
window.setWindowIcon(icon)
window.setFixedSize(600,800)
window.setToolTip('这是一个哈哈')






window.show()

sys.exit(app.exec())