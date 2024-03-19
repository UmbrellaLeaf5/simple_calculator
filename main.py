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

        # коннект кнопок с цифрами к соотв. функциям
        for i in range(10):
            self.connect_digit_button(digits_buttons[i], i)

        # список кнопок, обозначающих бинарные операции
        bin_opered_buttons = [self.ui.pushButton_div, self.ui.pushButton_minus,
                              self.ui.pushButton_mul, self.ui.pushButton_percent, self.ui.pushButton_plus]

        # коннект кнопок, отвечающих за бинарные операции к соотв. функциям
        for i in range(5):
            self.connect_bin_oper_button(
                bin_opered_buttons[i], [" / ", " - ", " * ", " % ", " + "][i])

        # коннект кнопок, отвечающих за унарные операции к соотв. функциям
        self.ui.pushButton_neg.clicked.connect(
            lambda: opers.unary.turn_to_neg(self))
        self.ui.pushButton_rev.clicked.connect(
            lambda: opers.unary.turn_to_rev(self))
        self.ui.pushButton_sqr.clicked.connect(
            lambda: opers.unary.take_square(self))
        self.ui.pushButton_sqrt.clicked.connect(
            lambda: opers.unary.take_square_root(self))

        # коннект кнопок, отвечающих за чистку к соотв. функциям
        self.ui.pushButton_C.clicked.connect(
            lambda: opers.clearing.clear(self))
        self.ui.pushButton_CE.clicked.connect(
            lambda: opers.clearing.clear_eval(self))
        self.ui.pushButton_del.clicked.connect(
            lambda: opers.clearing.delete(self))

        # коннект остальных кнопок к соотв. функциям
        self.ui.pushButton_eq.clicked.connect(
            lambda: opers.other.equalize(self))
        self.ui.pushButton_dot.clicked.connect(
            lambda: opers.other.make_dot(self))

    def connect_digit_button(self, button: QtWidgets.QPushButton, number: int):
        """
        Does:
            коннектит кнопку, обозначающую цифру, к соотв. функции

        Args:
            button (QPushButton): кнопка, которую коннектят
            number (int): цифра
        """

        button.clicked.connect(lambda: opers.other.change_number(self, number))

    def connect_bin_oper_button(self, button: QtWidgets.QPushButton, oper: str):
        """
        Does:
            коннектит кнопку, обозначающую бинарную операцию, к соотв. функции

        Args:
            button (QPushButton): кнопка, которую коннектят
            oper (str): операция
        """

        button.clicked.connect(lambda: opers.binary.do_bin_oper(self, oper))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
