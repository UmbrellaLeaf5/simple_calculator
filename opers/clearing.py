from inspect import currentframe, getframeinfo

from utils import *


def Clear(calc_window):
    """
    DOES
        очищает всё: и буфер, и текущую строку
    """

    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    calc_window.buffer.MathReset()
    calc_window.ui.labelExpression.setText("")
    calc_window.ui.labelEval.setText("0")


def ClearEvaluation(calc_window):
    """
    DOES
        очищает текущую строку
    """

    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    if (IsFloat(calc_window.buffer[-1])):
        calc_window.buffer[-1] = "0"

    else:
        calc_window.buffer.Push("0")

    calc_window.ui.labelEval.setText("0")


def Delete(calc_window):
    """
    DOES
        удаляет последний символ
    """

    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    if (IsFloat(calc_window.buffer[-1])):

        if calc_window.buffer[-1] == "0":
            Clear(calc_window)

        calc_window.buffer[-1] = calc_window.buffer[-1][0:-1]

        if calc_window.buffer[-1] == "":
            calc_window.buffer[-1] = "0"

        calc_window.ui.labelEval.setText(
            ViewOutputFormat(calc_window.buffer[-1]))
