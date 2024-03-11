from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt
from custom_button import CalcButton
from calc import Ui_Window
from utils import Stack, is_float, sci_round


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
            self.connect_bin_opered_button(opers[i], [" / ", " - ", " * ", " % ", " + "][i])

        self.ui.pushButton_eq.clicked.connect(self.realize_equal)

        self.ui.pushButton_C.clicked.connect(self.realize_clear)
        self.ui.pushButton_CE.clicked.connect(self.realize_clear_eval)
        self.ui.pushButton_del.clicked.connect(self.realize_del)

        self.ui.pushButton_dot.clicked.connect(self.realize_dot)

    def connect_numbed_button(self, button: QPushButton, number: int):
        button.clicked.connect(lambda: self.change_number(number))

    def connect_bin_opered_button(self, button: QPushButton, oper: str):
        button.clicked.connect(lambda: self.realize_bin_oper(oper))

    def change_number(self, number):
        print(self.calc_stack.stack)

        if (is_float(self.calc_stack[-1]) and self.calc_stack[-1] != "0"):
            self.calc_stack[-1] = self.calc_stack[-1] + str(number)
        elif self.calc_stack[-1] == "0":
            self.calc_stack[-1] = str(number)
        else:
            self.calc_stack.push(str(number))

        self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))

    def realize_bin_oper(self, oper):
        print(self.calc_stack.stack)

        if (is_float(self.calc_stack[-1])):
            if (self.calc_stack.size() > 2):
                evaluation: list = [self.calc_stack.pop()]
                evaluation.append(self.calc_stack.pop())
                evaluation.append(self.calc_stack.pop())
                # print("".join(reversed(evaluation)))
                self.calc_stack.push(str(eval("".join(reversed(evaluation)))))
                # print(str(eval("".join(reversed(evaluation)))))
                self.ui.labelEnteredExpression.setText(sci_round(self.calc_stack[-1]) + oper)
                self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))
            else:
                self.ui.labelEnteredExpression.setText(sci_round(self.calc_stack[-1]) + oper)
            self.calc_stack.push(oper)

        else:
            self.calc_stack.pop()
            number: str = self.calc_stack[-1]
            self.calc_stack.push(oper)

            self.ui.labelEnteredExpression.setText(sci_round(number) + oper)

    def realize_equal(self):
        print(self.calc_stack.stack)

        if (is_float(self.calc_stack[-1]) and self.calc_stack.size() > 1):
            evaluation: list = [self.calc_stack.pop()]
            evaluation.append(self.calc_stack.pop())
            evaluation.append(self.calc_stack.pop())

            try:
                self.calc_stack.push(str(eval("".join(reversed(evaluation)))))
                self.ui.labelEnteredExpression.setText(
                    sci_round("".join(reversed(evaluation))) + " =")
                self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))
            except ZeroDivisionError:
                self.ui.labelEnter.setText("Zero division")

        elif (self.calc_stack.size() > 1):
            evaluation: list = [self.calc_stack.pop()]
            number: str = self.calc_stack.pop()
            evaluation.append(number)
            evaluation = [number] + evaluation
            # print("".join(reversed(evaluation)))
            self.calc_stack.push(str(eval("".join(reversed(evaluation)))))
            # print(str(eval("".join(reversed(evaluation)))))
            self.ui.labelEnteredExpression.setText(sci_round("".join(reversed(evaluation))) + " =")
            self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))
        else:
            self.ui.labelEnteredExpression.setText(sci_round(self.calc_stack[-1]) + " =")

    def realize_clear(self):
        print(self.calc_stack.stack)

        self.calc_stack.clear()
        self.calc_stack.push("0")
        self.ui.labelEnteredExpression.setText("")
        self.ui.labelEnter.setText("0")

    def realize_clear_eval(self):
        print(self.calc_stack.stack)

        if (is_float(self.calc_stack[-1])):
            self.calc_stack[-1] = "0"
        else:
            self.calc_stack.push("0")

        self.ui.labelEnter.setText("0")

    def realize_del(self):
        print(self.calc_stack.stack)
        if (is_float(self.calc_stack[-1])):
            self.calc_stack[-1] = self.calc_stack[-1][0:-1]
            if self.calc_stack[-1] == "":
                self.calc_stack[-1] = "0"
            self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))

    def realize_dot(self):
        if (is_float(self.calc_stack[-1])):
            if self.calc_stack[-1].count(".") == 0:
                self.calc_stack[-1] += "."
                self.ui.labelEnter.setText(sci_round(self.calc_stack[-1]))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
