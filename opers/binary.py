from inspect import currentframe, getframeinfo

from utils import *


def do_bin_oper(calc_window, oper: str):
    # вывод названия функции
    # current_frame = currentframe()
    # if current_frame is not None:
    #     print(getframeinfo(current_frame).function)
    # print(calc_window.buffer.stack_)

    try:
        if (is_float(calc_window.buffer[-1])):
            if (calc_window.buffer.size() > 2):
                # если стек больше двух, значит, происходит какая-то операция, которую надо обработать

                # достаем их стека всё и пихаем в одно выражение
                evaluation: list = [calc_window.buffer.pop()]
                evaluation.append(calc_window.buffer.pop())
                evaluation.append(calc_window.buffer.pop())

                try:
                    # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
                    calc_window.buffer.push(calc_format(
                        eval("".join(reversed(evaluation)))))
                    calc_window.ui.labelExpression.setText(
                        view_output_format(calc_window.buffer[-1] + oper))
                    calc_window.ui.labelEval.setText(
                        view_output_format(calc_window.buffer[-1]))

                except ZeroDivisionError:
                    calc_window.ui.labelEval.setText("Zero division")
                    calc_window.buffer.math_reset()

            else:
                # иначе просто дописываем
                calc_window.ui.labelExpression.setText(
                    view_output_format(calc_window.buffer[-1] + oper))

            # но в любом случае добавляем в буфер операцию, чтобы потом отработал eval
            calc_window.buffer.push(oper)

        else:
            # если это не число, то просто меняем операцию
            calc_window.buffer.pop()
            number: str = calc_window.buffer[-1]
            calc_window.buffer.push(oper)

            calc_window.ui.labelExpression.setText(
                view_output_format(number + oper))

    except OverflowError:
        calc_window.ui.labelEval.setText("Too large number")
