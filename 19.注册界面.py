from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFormLayout,QVBoxLayout,QLineEdit,QRadioButton,QCheckBox,QTextEdit,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


import sys

def func():
    name = nameEdit.text()
    pwd = pwdEdit.text()
    sex = None
    if rb1.isChecked():
        sex = 'man'
    elif rb2.isChecked():
        sex = 'women'
    else:
        sex = 'no man and women'

    hobby = []
    if ck1.isChecked():
        hobby.append(ck1.text())
    if ck2.isChecked():
        hobby.append(ck2.text())
    if ck3.isChecked():
        hobby.append(ck3.text())

    sig = signEdit.text()
    label = labelEdit.toPlainText()
    print(name,pwd,sex,hobby,sig,label)




app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('注册界面')
wholelayout = QVBoxLayout()
window.setLayout(wholelayout)
formlayout = QFormLayout()
nameEdit = QLineEdit()
nameEdit.setPlaceholderText('请输入用户名')
pwdEdit = QLineEdit()
pwdEdit.setPlaceholderText('请输入密码')

sexlayout = QHBoxLayout()
rb1 = QRadioButton('man')
rb2 = QRadioButton('women')
rb3 = QRadioButton('no man and no women')
sexlayout.addWidget(rb1)
sexlayout.addWidget(rb2)
sexlayout.addWidget(rb3)
rb1.setChecked(True)

ck1 = QCheckBox('smoking')
ck2 = QCheckBox('which tv')
ck3 = QCheckBox('shopping')
hobbylayout = QHBoxLayout()
hobbylayout.addWidget(ck1)
hobbylayout.addWidget(ck2)
hobbylayout.addWidget(ck3)

signEdit = QLineEdit()
signEdit.setPlaceholderText('')

formlayout.addRow('username：',nameEdit)
formlayout.addRow('password:',pwdEdit)
formlayout.addRow('sex:',sexlayout)
formlayout.addRow('hobby:',hobbylayout)
formlayout.addRow('sign:',signEdit)

layout2 = QHBoxLayout()
label = QLabel('择偶要求:')
labelEdit = QTextEdit()
layout2.addWidget(label)
layout2.addWidget(labelEdit)
btn = QPushButton('register')
btn.setFixedSize(100,30)



wholelayout.addLayout(formlayout)
wholelayout.addLayout(layout2)
wholelayout.addWidget(btn,alignment=Qt.AlignHCenter)
btn.clicked.connect(func)
window.show()

sys.exit(app.exec())