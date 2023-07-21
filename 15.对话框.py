from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon


import sys


def func():

    result = QMessageBox.information(window,'警告','确认删除吗',QMessageBox.OK|QMessageBox.Cancel,QMessageBox.Cancel)
    print('测试中')
    if result == QMessageBox.OK:
        print('确认删除')
    elif result == QMessageBox.Cancel:
        print('取消删除')

app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('对话框')
btn = QPushButton('显示对话框')
btn.setParent(window)
btn.clicked.connect(func)






window.show()

sys.exit(app.exec())