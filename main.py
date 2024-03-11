from PyQt6 import QtWidgets

from calcui import Ui_Window
from utils import *

import opers.binary
import opers.unary
import opers.clearing
import opers.other


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # начальная настройка лейблов
        self.ui.labelEval.setText('0')
        self.ui.labelExpression.setText('')

        # создаём стек, который будем использовать для подсчета
        self.buffer = Stack()
        self.buffer.math_reset()

        # список кнопок, обозначающих цифры
        digits_buttons = [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2,
                          self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5,
                          self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                          self.ui.pushButton_9]

        for i in range(10):
            self.connect_digit_button(digits_buttons[i], i)

        # список кнопок, обозначающих бинарные операции
        bin_opered_buttons = [self.ui.pushButton_div, self.ui.pushButton_minus,
                              self.ui.pushButton_mul, self.ui.pushButton_percent, self.ui.pushButton_plus]

        for i in range(5):
            self.connect_bin_oper_button(
                bin_opered_buttons[i], [" / ", " - ", " * ", " % ", " + "][i])

        # коннект остальных кнопок к соотв. функциям
        self.ui.pushButton_eq.clicked.connect(self.equalize)
        self.ui.pushButton_dot.clicked.connect(self.make_dot)

        self.ui.pushButton_C.clicked.connect(self.clear)
        self.ui.pushButton_CE.clicked.connect(self.clear_eval)
        self.ui.pushButton_del.clicked.connect(self.delete)

        self.ui.pushButton_neg.clicked.connect(self.turn_to_neg)
        self.ui.pushButton_rev.clicked.connect(self.turn_to_rev)
        self.ui.pushButton_sqr.clicked.connect(self.take_square)
        self.ui.pushButton_sqrt.clicked.connect(self.take_square_root)

    def connect_digit_button(self, button: QtWidgets.QPushButton, number: int):
        """
        DOES:
            коннектит кнопку, обозначающую цифру, к соотв. функции

        ARGS:
            button (QPushButton): кнопка, которую коннектят
            number (int): цифра
        """

        button.clicked.connect(lambda: self.change_number(number))

    def connect_bin_oper_button(self, button: QtWidgets.QPushButton, oper: str):
        """
        DOES:
            коннектит кнопку, обозначающую бинарную операцию, к соотв. функции

        ARGS:
            button (QPushButton): кнопка, которую коннектят
            oper (str): операция
        """

        button.clicked.connect(lambda: self.do_bin_oper(oper))

    def change_number(self, number: int):
        opers.other.change_number(self, number)

    def equalize(self):
        opers.other.equalize(self)

    def make_dot(self):
        opers.other.make_dot(self)

    def do_bin_oper(self, oper: str):
        opers.binary.do_bin_oper(self, oper)

    def turn_to_neg(self):
        opers.unary.turn_to_neg(self)

    def turn_to_rev(self):
        opers.unary.turn_to_rev(self)

    def take_square(self):
        opers.unary.take_square(self)

    def take_square_root(self):
        opers.unary.take_square_root(self)

    def clear(self):
        opers.clearing.clear(self)

    def clear_eval(self):
        opers.clearing.clear_eval(self)

    def delete(self):
        opers.clearing.delete(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
