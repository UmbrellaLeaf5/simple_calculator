from inspect import currentframe, getframeinfo

from utils import *


def clear(calc_window):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    calc_window.buffer.clear()
    calc_window.buffer.push("0")
    calc_window.ui.labelExpression.setText("")
    calc_window.ui.labelEval.setText("0")


def clear_eval(calc_window):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1])):
        calc_window.buffer[-1] = "0"

    else:
        calc_window.buffer.push("0")

    calc_window.ui.labelEval.setText("0")


def delete(calc_window):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1])):
        calc_window.buffer[-1] = calc_window.buffer[-1][0:-1]

        if calc_window.buffer[-1] == "":
            calc_window.buffer[-1] = "0"

        calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))
