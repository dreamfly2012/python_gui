from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QCheckBox,QSlider,QLabel,QLCDNumber
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()

window.setWindowTitle('hello')

window.setWindowIcon(QIcon('icon.jpg'))

window.setMinimumSize(500,500)

window.button = QPushButton('点击我',window)

window.button.move(50,50)

window.button.setStyleSheet("QPushButton{background:green;color:red;font-size:20px;}")

window.checkbox = QCheckBox("我是checkbox",window)

window.checkbox.move(50,100)

window.qslider = QSlider(Qt.Horizontal,window)

window.qslider.move(50,200)

window.label = QLabel('label',window)

window.label.setGeometry(50,250,50,50)

pixmap = QPixmap('bg3.jpg')

window.label.setPixmap(pixmap)

window.label.setScaledContents(True)

window.lcd = QLCDNumber(window)

window.lcd.setGeometry(50,300,200,100)

window.qslider.valueChanged.connect(window.lcd.display)

window.button.clicked.connect(window.close)


window.show()

app.exec()