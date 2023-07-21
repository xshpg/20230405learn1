from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()

icon = QIcon('10.png')
window.setWindowTitle('文本展示')
# label = QLabel()
# label.setText('第一个文本')
# label.setParent(window)
# label = QLabel('第一个文本',window)
label = QLabel('第一个文本')
label.setParent(window)


window.setWindowIcon(icon)


# window.setFixedSize(600,800)

window.show()

sys.exit(app.exec())