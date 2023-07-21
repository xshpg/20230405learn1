from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel,QCheckBox
from PyQt5.QtGui import QIcon


import sys

def func(ck):
    print(ck)




app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('复选框')
layout = QHBoxLayout()
window.setLayout(layout)
lab = QLabel('爱好：')
layout.addWidget(lab)
ckb1 = QCheckBox('看书')
ckb2 = QCheckBox('打游戏')
ckb3 = QCheckBox('听歌')
layout.addWidget(ckb1)
layout.addWidget(ckb2)
layout.addWidget(ckb3)
ckb1.setChecked(True)

ckb1.toggled.connect(func)



window.show()

sys.exit(app.exec())