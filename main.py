from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt
from custom_button import CalcButton
from calc import Ui_Window
from utils import Stack


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        self.ui.labelEnter.setText('0')
        self.ui.labelEnteredExpression.setText('')

        self.calc_stack = Stack(["0"])

        numbers = [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2,
                   self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5,
                   self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                   self.ui.pushButton_9]

        for i in range(10):
            self.connect_numbed_button(numbers[i], i)

        opers = [self.ui.pushButton_div, self.ui.pushButton_minus,
                 self.ui.pushButton_mul, self.ui.pushButton_percent, self.ui.pushButton_plus]

        for i in range(5):
            self.connect_opered_button(opers[i], ["/", "-", "*", "%", "+"][i])

    def connect_numbed_button(self, button: QPushButton, number: int):
        button.clicked.connect(lambda: self.change_number(number))

    def connect_opered_button(self, button: QPushButton, oper: str):
        button.clicked.connect(lambda: self.realize_oper(oper))

    def change_number(self, number):
        if (self.calc_stack[-1].isdigit() and self.calc_stack[-1] != "0"):
            self.calc_stack[-1] = self.calc_stack[-1] + str(number)
        else:
            self.calc_stack.push(str(number))

        self.ui.labelEnter.setText(self.calc_stack[-1])

    def realize_oper(self, oper):
        if (self.calc_stack[-1].isdigit()):
            if (self.calc_stack.size() > 2):
                evaluation: str = self.calc_stack.pop()
                evaluation += self.calc_stack.pop()
                evaluation += self.calc_stack.pop()
                self.calc_stack.push(str(eval(evaluation)))
                self.ui.labelEnteredExpression.setText(self.calc_stack[-1] + oper)
                self.ui.labelEnter.setText(self.calc_stack[-1])
            else:
                self.ui.labelEnteredExpression.setText(self.calc_stack[-1] + oper)

        else:
            pass

        self.calc_stack.push(" + ")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
