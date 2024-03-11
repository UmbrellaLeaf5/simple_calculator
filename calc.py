from PyQt6 import QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import Qt
from calc_ui import Ui_Form

class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()


        # uic.loadUi("calc.ui", self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.cur = '0'
        self.op = ''
        self.next = 0

        self.ui.pushButton_0.clicked.connect(lambda: self.change_number{0})

        # uic.loadUi("calc.ui", self)
    
    def change_number(self, number):
        self.next *= 10
        self.next += number


if __name__ == "main":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()