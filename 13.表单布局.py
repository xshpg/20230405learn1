from PyQt5.QtWidgets import QApplication,QWidget,QFormLayout,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon


import sys

def regist():
    name = nameEdit.text()
    age = ageEdit.text()
    phone = phoneEdit.text()
    print('姓名：%s,年龄：%s,电话号码：%s'%(name,age,phone))

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('表单布局')
layout = QFormLayout()
window.setLayout(layout)
nameEdit = QLineEdit()
ageEdit = QLineEdit()
phoneEdit = QLineEdit()
btn= QPushButton('注册')
layout.addRow('姓名',nameEdit)
layout.addRow('年龄',ageEdit)
layout.addRow('电话',phoneEdit)
layout.addRow('',btn)
btn.clicked.connect(regist)


window.show()

sys.exit(app.exec())