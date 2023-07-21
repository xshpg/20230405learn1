from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('10遍了')
icon = QIcon('10.png')
window.setWindowIcon(icon)
window.setFixedSize(300,200)
window.setToolTip('10遍了')



window.show()

sys.exit(app.exec())