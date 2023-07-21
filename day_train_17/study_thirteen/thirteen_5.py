from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QFormLayout
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('5trian')
layout = QFormLayout()
window.setLayout(layout)
nameEdit = QLineEdit()
ageEdit = QLineEdit()
phoneEdit = QLineEdit()
layout.addRow('name',nameEdit)
layout.addRow('age',ageEdit)
layout.addRow('phone',phoneEdit)




window.show()

sys.exit(app.exec())