from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QPushButton,QCheckBox,QSlider
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()

window.setWindowTitle('hello')

window.setWindowIcon(QIcon('icon.jpg'))

window.setMinimumSize(500,500)

window.button = QPushButton('点击我',window)

window.button.move(50,50)

window.checkbox = QCheckBox("我是checkbox",window)

window.checkbox.move(50,100)

window.qslider = QSlider(Qt.Horizontal,window)

window.qslider.move(50,200)

window.show()

app.exec()