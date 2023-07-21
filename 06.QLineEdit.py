from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5.QtGui import QIcon


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('单行输入框')
edit = QLineEdit()
# edit.setEchoMode(QLineEdit.Normal)
# edit.setEchoMode(QLineEdit.NoEcho)
# edit.setEchoMode(QLineEdit.Password)
# edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
# edit.setPlaceholderText('请输入用户名')
# edit.setText('amos')
# print(edit.text())
edit.setMaxLength(10)



edit.setParent(window)






window.show()

sys.exit(app.exec())