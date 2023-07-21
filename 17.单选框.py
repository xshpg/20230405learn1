from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QRadioButton
from PyQt5.QtGui import QIcon


import sys
def func(ck):
    print(ck)

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('单选框')
layout = QHBoxLayout()
window.setLayout(layout)
rb1 = QRadioButton('男')
rb2 = QRadioButton('女')
layout.addWidget(rb1)
layout.addWidget(rb2)
rb1.setChecked(True)

rb1.toggled.connect(func)


window.show()

sys.exit(app.exec())