from inspect import currentframe, getframeinfo

from utils import *


def equalize(calc_window):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    try:
        if (calc_window.buffer.size() > 1):
            if (is_float(calc_window.buffer[-1])):
                evaluation: list = [calc_window.buffer.pop()]
                evaluation.append(calc_window.buffer.pop())
                evaluation.append(calc_window.buffer.pop())

                try:
                    calc_window.buffer.push(calc_format(eval("".join(reversed(evaluation)))))
                    calc_window.ui.labelExpression.setText(
                        view_output_format(calc_window.buffer[-1] + " ="))
                    calc_window.ui.labelEval.setText(
                        view_output_format(calc_window.buffer[-1]))

                except ZeroDivisionError:
                    calc_window.ui.labelEval.setText("Zero division")
                    calc_window.buffer.math_reset()

            else:
                evaluation: list = [calc_window.buffer.pop()]
                number: str = calc_window.buffer.pop()
                evaluation.append(number)
                evaluation = [number] + evaluation

                try:
                    calc_window.buffer.push(calc_format(eval("".join(reversed(evaluation)))))
                    calc_window.ui.labelExpression.setText(
                        view_output_format(calc_window.buffer[-1] + " ="))
                    calc_window.ui.labelEval.setText(
                        view_output_format(calc_window.buffer[-1]))

                except ZeroDivisionError:
                    calc_window.ui.labelEval.setText("Zero division")
                    calc_window.buffer.math_reset()

        else:
            calc_window.buffer[-1] = calc_format(float(calc_window.buffer[-1]))
            calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))
            calc_window.ui.labelExpression.setText(
                view_output_format(calc_window.buffer[-1]) + " =")

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def change_number(calc_window, number: int):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1]) and calc_window.buffer[-1] != "0"):
        calc_window.buffer[-1] = calc_window.buffer[-1] + calc_format(number)

    elif calc_window.buffer[-1] == "0":
        calc_window.buffer[-1] = calc_format(number)

    else:
        calc_window.buffer.push(calc_format(number))

    calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))


def make_dot(calc_window):
    # вывод названия функции
    current_frame = currentframe()
    if current_frame is not None:
        print(getframeinfo(current_frame).function)
    print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1])):
        if calc_window.buffer[-1].count(".") == 0:
            calc_window.buffer[-1] += "."
            calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))
