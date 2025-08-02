from utils.utils import CalcFormat, IsFloat, ViewOutputFormat


def DoBinaryOperation(calc_window, oper: str):
  try:
    if IsFloat(calc_window.buffer[-1]):
      if calc_window.buffer.Size() > 2:  # noqa: PLR2004
        # если стек больше двух, значит,
        # происходит какая-то операция, которую надо обработать

        # достаем их стека всё и пихаем в одно выражение
        evaluation: list = [calc_window.buffer.Pop()]
        evaluation.append(calc_window.buffer.Pop())
        evaluation.append(calc_window.buffer.Pop())

        try:
          # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
          calc_window.buffer.Push(CalcFormat(eval("".join(reversed(evaluation)))))

          calc_window.ui.labelExpression.setText(
            ViewOutputFormat(calc_window.buffer[-1] + oper)
          )

          calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))

        except ZeroDivisionError:
          calc_window.ui.labelEval.setText("Zero division")
          calc_window.buffer.MathReset()

      else:
        # иначе просто дописываем
        calc_window.ui.labelExpression.setText(
          ViewOutputFormat(calc_window.buffer[-1] + oper)
        )

      # но в любом случае добавляем в буфер операцию, чтобы потом отработал eval
      calc_window.buffer.Push(oper)

    else:
      # если это не число, то просто меняем операцию
      calc_window.buffer.Pop()
      number: str = calc_window.buffer[-1]
      calc_window.buffer.Push(oper)

      calc_window.ui.labelExpression.setText(ViewOutputFormat(number + oper))

  except OverflowError:
    calc_window.ui.labelEval.setText("Too large number")
