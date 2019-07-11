from PyQt5.QtWidgets import QApplication,QWidget

from Ui_calc import Ui_Form


def on_click(self):
    value1 = int(ui.lineEdit.text())
    value2 = int(ui.lineEdit_2.text())

    operation = ui.comboBox.currentText()

    if operation=='+':
        value3 = value1 + value2
    elif operation == '-':
        value3 = value1 - value2
    elif operation == '*':
        value3 = value1 * value2
    elif operation == '/':
        value3 = value1/value2

    ui.lineEdit_3.setText(str(value3))            
    #print("button clicked")


if __name__ =='__main__':

    app = QApplication([])

    window = QWidget()

    ui = Ui_Form()

    ui.setupUi(window)

    ui.pushButton.clicked.connect(on_click)


    window.show()

    app.exec()