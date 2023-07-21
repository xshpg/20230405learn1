from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('6bian')
label = QLabel('6bain')
label.setParent(window)





window.show()

sys.exit(app.exec())