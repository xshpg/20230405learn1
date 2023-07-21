from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

import sys

app = QApplication(sys.argv)

window = QWidget()
icon = QIcon('10.png')
window.setWindowIcon(icon)
window.setWindowTitle('课程2练习第五遍')
window.setFixedSize(600,800)
window.show()
sys.exit(app.exec())