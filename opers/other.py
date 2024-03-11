from inspect import currentframe, getframeinfo

from utils import *


def equalize(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (calc_window.buffer.size() > 1):
            # если стек больше одного, значит, происходит какая-то операция, которую надо обработать

            if (is_float(calc_window.buffer[-1])):
                # если там было число, то выражение полное, считаем, как положено

                # достаем их стека всё и пихаем в одно выражение
                evaluation: list = [calc_window.buffer.pop()]
                evaluation.append(calc_window.buffer.pop())
                evaluation.append(calc_window.buffer.pop())

                try:
                    # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
                    calc_window.buffer.push(calc_format(eval("".join(reversed(evaluation)))))
                    calc_window.ui.labelExpression.setText(
                        view_output_format(calc_window.buffer[-1] + " ="))
                    calc_window.ui.labelEval.setText(
                        view_output_format(calc_window.buffer[-1]))

                except ZeroDivisionError:
                    calc_window.ui.labelEval.setText("Zero division")
                    calc_window.buffer.math_reset()

            else:
                # если там была операция, то выражение дополняем тем же числом

                evaluation: list = [calc_window.buffer.pop()]
                number: str = calc_window.buffer.pop()
                evaluation.append(number)
                evaluation = [number] + evaluation

                try:
                    # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
                    calc_window.buffer.push(calc_format(eval("".join(reversed(evaluation)))))
                    calc_window.ui.labelExpression.setText(
                        view_output_format(calc_window.buffer[-1] + " ="))
                    calc_window.ui.labelEval.setText(
                        view_output_format(calc_window.buffer[-1]))

                except ZeroDivisionError:
                    calc_window.ui.labelEval.setText("Zero division")
                    calc_window.buffer.math_reset()

        else:
            # если нажали с маленьким стеком (т.е. просто так), то просто форматируем число
            calc_window.buffer[-1] = calc_format(float(calc_window.buffer[-1]))
            calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))
            calc_window.ui.labelExpression.setText(
                view_output_format(calc_window.buffer[-1]) + " =")

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")


def change_number(calc_window, number: int):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1])):
        if (calc_window.buffer[-1] != "0"):  # лишние цифры к нулю не добавляем
            calc_window.buffer[-1] = calc_window.buffer[-1] + calc_format(number)

        else:  # ноль мы просто меняем
            calc_window.buffer[-1] = calc_format(number)

    else:
        calc_window.buffer.push(calc_format(number))

    calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))


def make_dot(calc_window):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    if (is_float(calc_window.buffer[-1])):
        if calc_window.buffer[-1].count(".") == 0:  # если точка уже есть, её ставить не надо
            calc_window.buffer[-1] += "."
            calc_window.ui.labelEval.setText(view_output_format(calc_window.buffer[-1]))
