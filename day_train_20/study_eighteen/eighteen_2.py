from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel,QCheckBox
from PyQt5.QtGui import QIcon


import sys
def func(ck):
    print(ck)

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('2train')
layout = QHBoxLayout()
window.setLayout(layout)
lab = QLabel('hobby')
layout.addWidget(lab)
ck1 = QCheckBox('egg')
ck2 = QCheckBox('pig')
ck3 = QCheckBox('dog')
layout.addWidget(ck1)
layout.addWidget(ck2)
layout.addWidget(ck3)
ck1.setChecked(True)
ck1.toggled.connect(func)

window.show()

sys.exit(app.exec())