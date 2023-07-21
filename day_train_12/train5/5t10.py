from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon,QMovie


import sys


app = QApplication(sys.argv)

window = QWidget()


window.setWindowTitle('10bian')
label = QLabel()
movie = QMovie('2.gif')
label.setMovie(movie)
label.setParent(window)
movie.start()




window.show()

sys.exit(app.exec())