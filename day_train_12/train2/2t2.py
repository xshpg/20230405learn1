from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

import sys

app = QApplication(sys.argv)
window = QWidget()
icon = QIcon('10.jpeg')
window.setWindowIcon(icon)
window.setWindowTitle('课程2联系2')
window.setFixedSize(600,800)
window.show()
sys.exit(app.exec())