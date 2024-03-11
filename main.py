from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QSize, Qt
from custom_button import CalcButton
from calc import Ui_Window


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        self.ui.labelEnter.setText('')

        self.cur = 0
        self.next = 0

        self.ops = ['+', '-', '*', '/', '%']

        numbers = [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2,
                   self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5,
                   self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                   self.ui.pushButton_9]

        for i in range(10):
            self.connect_button(numbers[i], i)

        self.ui.pushButton_plus.clicked.connect(self.sum)
        self.ui.pushButton_eq.clicked.connect(self.eq)

    def eq(self):
        text = self.ui.labelEnter.getText()

        self.cur = eval(text)
        self.next = 0

        self.ui.labelEnter.setText(str(self.cur))

    def sum(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.labelEnter.displayText()

        if text[-1] not in self.ops:
            text += '+'
            self.ui.labelEnter.setText(text)

    def connect_button(self, button, number):
        button.clicked.connect(lambda: self.change_number(number))

    def change_number(self, number):
        text = self.ui.labelEnter.displayText()
        last_num = self.next

        self.next *= 10
        self.next += number

        new_text = text + str(self.next)[-1]

        if self.next != last_num:
            if text == '0':
                self.ui.labelEnter.setText(str(self.next)[-1])
            else:
                self.ui.labelEnter.setText(new_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
