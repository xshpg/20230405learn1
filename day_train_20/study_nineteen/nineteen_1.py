from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFormLayout,QVBoxLayout,QLineEdit,QRadioButton,QCheckBox,QTextEdit,QPushButton,QLabel
from PyQt5.QtGui import QIcon


import sys



app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('1train')
wholelayout = QVBoxLayout()
window.setLayout(wholelayout)
formlayout = QFormLayout()
nameEdit = QLineEdit()
nameEdit.setPlaceholderText('请输入用户名')
pwdEdit = QLineEdit()
pwdEdit.setPlaceholderText('请输入密码')
sexlayout = QHBoxLayout
rb1 = QRadioButton('man')
rb2 = QRadioButton('women')
rb3 = QRadioButton('no plople')
sexlayout.addWidget(rb1)
sexlayout.addWidget(rb2)
sexlayout.addWidget(rb3)
rb1.setChecked(True)

ck1 = QCheckBox('smoking')
ck2 = QCheckBox('shopping')
ck3 = QCheckBox('playing water')
hobbylayout = QHBoxLayout()
hobbylayout.addWidget(ck1)
hobbylayout.addWidget(ck2)
hobbylayout.addWidget(ck3)
signEdit = QLineEdit()
signEdit.setPlaceholderText('')
formlayout.addRow('username',nameEdit)
formlayout.addRow('password',pwdEdit)
formlayout.addRow('sex',sexlayout)
formlayout.addRow('hobby',hobbylayout)
formlayout.addRow('hobby',signEdit)

window.show()

sys.exit(app.exec())