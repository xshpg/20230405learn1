from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('4bian')
label = QLabel('4bian')
label.setParent(window)





window.show()

sys.exit(app.exec())