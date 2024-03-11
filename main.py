from PyQt6 import QtWidgets
from calc import Ui_Window
from utils import *
from inspect import currentframe, getframeinfo


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # начальная настройка лейблов
        self.ui.labelNumber.setText('0')
        self.ui.labelExpression.setText('')

        # создаём стек, который будем использовать для подсчета
        self.calc_stack = Stack(["0"])

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
            self.connect_bin_opered_button(
                bin_opered_buttons[i], [" / ", " - ", " * ", " % ", " + "][i])

        # коннект остальных кнопок к соотв. функциям
        self.ui.pushButton_eq.clicked.connect(self.equal)

        self.ui.pushButton_C.clicked.connect(self.clear)
        self.ui.pushButton_CE.clicked.connect(self.clear_eval)
        self.ui.pushButton_del.clicked.connect(self.delete)

        self.ui.pushButton_dot.clicked.connect(self.make_dot)

        self.ui.pushButton_neg.clicked.connect(self.turn_to_neg)
        self.ui.pushButton_rev.clicked.connect(self.turn_to_rev)

        self.ui.pushButton_sqr.clicked.connect(self.square)
        self.ui.pushButton_sqrt.clicked.connect(self.square_root)

    def connect_digit_button(self, button: QtWidgets.QPushButton, number: int):
        """
        DOES:
            коннектит кнопку, обозначающую цифру, к соотв. функции

        ARGS:
            button (QPushButton): кнопка, которую коннектят
            number (int): цифра
        """

        button.clicked.connect(lambda: self.change_number(number))

    def connect_bin_opered_button(self, button: QtWidgets.QPushButton, oper: str):
        """
        DOES:
            коннектит кнопку, обозначающую бинарную операцию, к соотв. функции

        ARGS:
            button (QPushButton): кнопка, которую коннектят
            oper (str): операция
        """

        button.clicked.connect(lambda: self.bin_oper(oper))

    def change_number(self, number: int):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        if (is_float(self.calc_stack[-1]) and self.calc_stack[-1] != "0"):
            self.calc_stack[-1] = self.calc_stack[-1] + calc_format(number)

        elif self.calc_stack[-1] == "0":
            self.calc_stack[-1] = calc_format(number)

        else:
            self.calc_stack.push(calc_format(number))

        self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

    def bin_oper(self, oper):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (is_float(self.calc_stack[-1])):
                if (self.calc_stack.size() > 2):
                    # если стек больше двух, значит, происходит какая-то операция, которую надо обработать

                    # достаем их стека всё и пихаем в одно выражение
                    evaluation: list = [self.calc_stack.pop()]
                    evaluation.append(self.calc_stack.pop())
                    evaluation.append(self.calc_stack.pop())

                    try:
                        # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
                        self.calc_stack.push(calc_format(eval("".join(reversed(evaluation)))))
                        self.ui.labelExpression.setText(
                            view_output_format(self.calc_stack[-1] + oper))
                        self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

                    except ZeroDivisionError:
                        self.ui.labelNumber.setText("Zero division")
                        self.calc_stack.math_reset()

                else:
                    self.ui.labelExpression.setText(view_output_format(self.calc_stack[-1] + oper))

                self.calc_stack.push(oper)

            else:
                self.calc_stack.pop()
                number: str = self.calc_stack[-1]
                self.calc_stack.push(oper)

                self.ui.labelExpression.setText(view_output_format(number + oper))

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")

    def equal(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (self.calc_stack.size() > 1):
                if (is_float(self.calc_stack[-1])):
                    evaluation: list = [self.calc_stack.pop()]
                    evaluation.append(self.calc_stack.pop())
                    evaluation.append(self.calc_stack.pop())

                    try:
                        self.calc_stack.push(calc_format(eval("".join(reversed(evaluation)))))
                        self.ui.labelExpression.setText(
                            view_output_format(self.calc_stack[-1] + " ="))
                        self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

                    except ZeroDivisionError:
                        self.ui.labelNumber.setText("Zero division")
                        self.calc_stack.math_reset()

                else:
                    evaluation: list = [self.calc_stack.pop()]
                    number: str = self.calc_stack.pop()
                    evaluation.append(number)
                    evaluation = [number] + evaluation

                    try:
                        self.calc_stack.push(calc_format(eval("".join(reversed(evaluation)))))
                        self.ui.labelExpression.setText(
                            view_output_format(self.calc_stack[-1] + " ="))
                        self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

                    except ZeroDivisionError:
                        self.ui.labelNumber.setText("Zero division")
                        self.calc_stack.math_reset()

            else:
                self.calc_stack[-1] = calc_format(float(self.calc_stack[-1]))
                self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))
                self.ui.labelExpression.setText(view_output_format(self.calc_stack[-1]) + " =")

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")

    def clear(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        self.calc_stack.clear()
        self.calc_stack.push("0")
        self.ui.labelExpression.setText("")
        self.ui.labelNumber.setText("0")

    def clear_eval(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        if (is_float(self.calc_stack[-1])):
            self.calc_stack[-1] = "0"

        else:
            self.calc_stack.push("0")

        self.ui.labelNumber.setText("0")

    def delete(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        if (is_float(self.calc_stack[-1])):
            self.calc_stack[-1] = self.calc_stack[-1][0:-1]

            if self.calc_stack[-1] == "":
                self.calc_stack[-1] = "0"

            self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

    def make_dot(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        if (is_float(self.calc_stack[-1])):
            if self.calc_stack[-1].count(".") == 0:
                self.calc_stack[-1] += "."
                self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

    def turn_to_neg(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (is_float(self.calc_stack[-1])):
                if (float(self.calc_stack[-1]) != 0):
                    self.calc_stack[-1] = calc_format(-float(self.calc_stack[-1]))
                    self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")

    def turn_to_rev(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (is_float(self.calc_stack[-1])):
                try:
                    self.ui.labelExpression.setText(view_output_format("1/" + self.calc_stack[-1]))
                    self.calc_stack[-1] = calc_format(1/float(self.calc_stack[-1]))
                    self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

                except ZeroDivisionError:
                    self.ui.labelNumber.setText("Zero division")
                    self.calc_stack.math_reset()

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")

    def square(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (is_float(self.calc_stack[-1])):
                if (float(self.calc_stack[-1]) != 0):
                    self.ui.labelExpression.setText(view_output_format(self.calc_stack[-1]) + "²")
                    self.calc_stack[-1] = calc_format(float(self.calc_stack[-1])**2)
                    self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")

    def square_root(self):
        # вывод названия функции
        current_frame = currentframe()
        if current_frame is not None:
            print(getframeinfo(current_frame).function)
        print(self.calc_stack.stack_)

        try:
            if (is_float(self.calc_stack[-1])):
                self.ui.labelExpression.setText(view_output_format("√" + self.calc_stack[-1]))

                if float(self.calc_stack[-1]) >= 0:
                    self.calc_stack[-1] = calc_format(float(self.calc_stack[-1])**0.5)
                    self.ui.labelNumber.setText(view_output_format(self.calc_stack[-1]))

                else:
                    self.ui.labelNumber.setText("Invalid operation")
                    self.calc_stack.math_reset()

        except OverflowError:
            self.ui.labelNumber.setText("Too large number")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
