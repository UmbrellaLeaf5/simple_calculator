from inspect import currentframe, getframeinfo

from utils import *


# тут все функции работают однообразно, но в одну их не засунешь: разные ОДЗ

def TurnToNegative(calc_window):

    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (IsFloat(calc_window.buffer[-1])):
            if (float(calc_window.buffer[-1]) != 0):
                calc_window.buffer[-1] = CalcFormat(-float(
                    calc_window.buffer[-1]))
                calc_window.ui.labelEval.setText(
                    ViewOutputFormat(calc_window.buffer[-1]))

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def TurnToReverse(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (IsFloat(calc_window.buffer[-1])):
            try:
                calc_window.ui.labelExpression.setText(
                    ViewOutputFormat("1/" + calc_window.buffer[-1]))
                calc_window.buffer[-1] = CalcFormat(
                    1/float(calc_window.buffer[-1]))
                calc_window.ui.labelEval.setText(
                    ViewOutputFormat(calc_window.buffer[-1]))

            except ZeroDivisionError:
                calc_window.ui.labelEval.setText("Zero division")
                calc_window.buffer.MathReset()

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def TakeSquare(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (IsFloat(calc_window.buffer[-1])):
            if (float(calc_window.buffer[-1]) != 0):
                calc_window.ui.labelExpression.setText(
                    ViewOutputFormat(calc_window.buffer[-1]) + "²")
                calc_window.buffer[-1] = CalcFormat(
                    float(calc_window.buffer[-1])**2)
                calc_window.ui.labelEval.setText(
                    ViewOutputFormat(calc_window.buffer[-1]))

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def TakeSquareRoot(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (IsFloat(calc_window.buffer[-1])):
            calc_window.ui.labelExpression.setText(
                ViewOutputFormat("√" + calc_window.buffer[-1]))

            if float(calc_window.buffer[-1]) >= 0:
                calc_window.buffer[-1] = CalcFormat(
                    float(calc_window.buffer[-1])**0.5)
                calc_window.ui.labelEval.setText(
                    ViewOutputFormat(calc_window.buffer[-1]))

            else:
                calc_window.ui.labelEval.setText("Invalid operation")
                calc_window.buffer.MathReset()

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")
