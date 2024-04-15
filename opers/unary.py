from inspect import currentframe, getframeinfo

from utils import *


# тут все функции работают однообразно, но в одну их не засунешь: разные ОДЗ

def turn_to_neg(calc_window):

    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (is_float(calc_window.buffer[-1])):
            if (float(calc_window.buffer[-1]) != 0):
                calc_window.buffer[-1] = calc_format(-float(
                    calc_window.buffer[-1]))
                calc_window.ui.labelEval.setText(
                    view_output_format(calc_window.buffer[-1]))

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def turn_to_rev(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (is_float(calc_window.buffer[-1])):
            try:
                calc_window.ui.labelExpression.setText(
                    view_output_format("1/" + calc_window.buffer[-1]))
                calc_window.buffer[-1] = calc_format(
                    1/float(calc_window.buffer[-1]))
                calc_window.ui.labelEval.setText(
                    view_output_format(calc_window.buffer[-1]))

            except ZeroDivisionError:
                calc_window.ui.labelEval.setText("Zero division")
                calc_window.buffer.math_reset()

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def take_square(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (is_float(calc_window.buffer[-1])):
            if (float(calc_window.buffer[-1]) != 0):
                calc_window.ui.labelExpression.setText(
                    view_output_format(calc_window.buffer[-1]) + "²")
                calc_window.buffer[-1] = calc_format(
                    float(calc_window.buffer[-1])**2)
                calc_window.ui.labelEval.setText(
                    view_output_format(calc_window.buffer[-1]))

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def take_square_root(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (is_float(calc_window.buffer[-1])):
            calc_window.ui.labelExpression.setText(
                view_output_format("√" + calc_window.buffer[-1]))

            if float(calc_window.buffer[-1]) >= 0:
                calc_window.buffer[-1] = calc_format(
                    float(calc_window.buffer[-1])**0.5)
                calc_window.ui.labelEval.setText(
                    view_output_format(calc_window.buffer[-1]))

            else:
                calc_window.ui.labelEval.setText("Invalid operation")
                calc_window.buffer.math_reset()

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")
