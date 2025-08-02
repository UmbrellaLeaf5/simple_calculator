from PyQt6 import QtGui, QtWidgets

import opers.binary
import opers.clearing
import opers.other
import opers.unary
from calcui import Ui_Window
from utils import *


class Window(QtWidgets.QMainWindow):
  def __init__(self) -> None:
    super().__init__()

    self.ui = Ui_Window()
    self.ui.setupUi(self)

    # начальная настройка лейблов
    self.ui.labelEval.setText("0")
    self.ui.labelExpression.setText("")

    # создаём стек, который будем использовать для подсчета
    self.buffer = Stack()
    self.buffer.MathReset()

    # список кнопок, обозначающих цифры
    digits_buttons = [
      self.ui.pushButton_0,
      self.ui.pushButton_1,
      self.ui.pushButton_2,
      self.ui.pushButton_3,
      self.ui.pushButton_4,
      self.ui.pushButton_5,
      self.ui.pushButton_6,
      self.ui.pushButton_7,
      self.ui.pushButton_8,
      self.ui.pushButton_9,
    ]

    # коннект кнопок с цифрами к соотв. функциям
    for i in range(10):
      self.ConnectDigitButton(digits_buttons[i], i)

    # список кнопок, обозначающих бинарные операции
    bin_opered_buttons = [
      self.ui.pushButton_div,
      self.ui.pushButton_minus,
      self.ui.pushButton_mul,
      self.ui.pushButton_percent,
      self.ui.pushButton_plus,
    ]

    # коннект кнопок, отвечающих за бинарные операции к соотв. функциям
    for i in range(5):
      self.ConnectBinaryOperationButton(
        bin_opered_buttons[i], [" / ", " - ", " * ", " % ", " + "][i]
      )

    # коннект кнопок, отвечающих за унарные операции к соотв. функциям
    self.ui.pushButton_neg.clicked.connect(lambda: opers.unary.TurnToNegative(self))
    self.ui.pushButton_rev.clicked.connect(lambda: opers.unary.TurnToReverse(self))
    self.ui.pushButton_sqr.clicked.connect(lambda: opers.unary.TakeSquare(self))
    self.ui.pushButton_sqrt.clicked.connect(lambda: opers.unary.TakeSquareRoot(self))

    # коннект кнопок, отвечающих за чистку к соотв. функциям
    self.ui.pushButton_C.clicked.connect(lambda: opers.clearing.Clear(self))
    self.ui.pushButton_CE.clicked.connect(lambda: opers.clearing.ClearEvaluation(self))
    self.ui.pushButton_del.clicked.connect(lambda: opers.clearing.Delete(self))

    # коннект остальных кнопок к соотв. функциям
    self.ui.pushButton_eq.clicked.connect(lambda: opers.other.Equalize(self))
    self.ui.pushButton_dot.clicked.connect(lambda: opers.other.MakeDot(self))

  def ConnectDigitButton(self, button: QtWidgets.QPushButton, number: int):
    """
    Does:
        коннектит кнопку, обозначающую цифру, к соотв. функции

    Args:
        button (QPushButton): кнопка, которую коннектят
        number (int): цифра
    """

    button.clicked.connect(lambda: opers.other.ChangeNumber(self, number))

  def ConnectBinaryOperationButton(self, button: QtWidgets.QPushButton, oper: str):
    """
    Does:
        коннектит кнопку, обозначающую бинарную операцию, к соотв. функции

    Args:
        button (QPushButton): кнопка, которую коннектят
        oper (str): операция
    """

    button.clicked.connect(lambda: opers.binary.DoBinaryOperation(self, oper))


if __name__ == "__main__":
  import sys

  app = QtWidgets.QApplication(sys.argv)

  # https://www.flaticon.com/free-icon/calculator_2374370?term=calculator&page=1&position=8&origin=search&related_id=2374370
  icon = QtGui.QIcon("icon.png")
  app.setWindowIcon(icon)

  window = Window()
  window.show()

  sys.exit(app.exec())
