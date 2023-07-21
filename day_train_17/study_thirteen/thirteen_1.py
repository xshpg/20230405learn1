from PyQt5.QtWidgets import QApplication,QWidget,QFormLayout,QLineEdit
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('1trian')
layout = QFormLayout()
window.setLayout(layout)
nameEdit = QLineEdit()
ageEdit = QLineEdit()
phoneEdit = QLineEdit()
layout.addRow('姓名',nameEdit)
layout.addRow('年龄',ageEdit)
layout.addRow('手机号',phoneEdit)






window.show()

sys.exit(app.exec())