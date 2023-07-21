from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton,QLineEdit,QInputDialog
from PyQt5.QtGui import QIcon


import sys

def func():
    str1,result = QInputDialog.getText(window,'提示','请输入角色名')
    if result:
        edit.setText(str1)
    


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('输入对话框')
layout = QHBoxLayout()
window.setLayout(layout)

btn = QPushButton('创建角色')
edit = QLineEdit()
layout.addWidget(btn)
layout.addWidget(edit)
btn.clicked.connect(func)



window.show()

sys.exit(app.exec())