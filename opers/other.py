from utils.utils import CalcFormat, IsFloat, ViewOutputFormat


def Equalize(calc_window):
  try:
    if calc_window.buffer.Size() > 1:
      # если стек больше одного, значит,
      # происходит какая-то операция, которую надо обработать

      if IsFloat(calc_window.buffer[-1]):
        # если там было число, то выражение полное, считаем, как положено

        # достаем их стека всё и пихаем в одно выражение
        evaluation: list = [calc_window.buffer.Pop()]
        evaluation.append(calc_window.buffer.Pop())
        evaluation.append(calc_window.buffer.Pop())

        try:
          # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
          calc_window.buffer.Push(CalcFormat(eval("".join(reversed(evaluation)))))
          calc_window.ui.labelExpression.setText(
            ViewOutputFormat(calc_window.buffer[-1] + " =")
          )
          calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))

        except ZeroDivisionError:
          calc_window.ui.labelEval.setText("Zero division")
          calc_window.buffer.MathReset()

      else:
        # если там была операция, то выражение дополняем тем же числом

        evaluation: list = [calc_window.buffer.Pop()]
        number: str = calc_window.buffer.Pop()
        evaluation.append(number)
        evaluation = [number, *evaluation]

        try:
          # разворот необходим, так как из стека мы вытаскиваем в обратном порядке
          calc_window.buffer.Push(CalcFormat(eval("".join(reversed(evaluation)))))
          calc_window.ui.labelExpression.setText(
            ViewOutputFormat(calc_window.buffer[-1] + " =")
          )
          calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))

        except ZeroDivisionError:
          calc_window.ui.labelEval.setText("Zero division")
          calc_window.buffer.MathReset()

    else:
      # если нажали с маленьким стеком (т.е. просто так), то просто форматируем число
      calc_window.buffer[-1] = CalcFormat(float(calc_window.buffer[-1]))
      calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))
      calc_window.ui.labelExpression.setText(
        ViewOutputFormat(calc_window.buffer[-1]) + " ="
      )

  except OverflowError:
    calc_window.ui.labelEval.setText("Too large number")


def ChangeNumber(calc_window, number: int):
  if IsFloat(calc_window.buffer[-1]):
    if calc_window.buffer[-1] != "0":  # лишние цифры к нулю не добавляем
      calc_window.buffer[-1] = calc_window.buffer[-1] + CalcFormat(number)

    else:  # ноль мы просто меняем
      calc_window.buffer[-1] = CalcFormat(number)

  else:
    calc_window.buffer.Push(CalcFormat(number))

  calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))


def MakeDot(calc_window):
  if IsFloat(calc_window.buffer[-1]):
    # если точка уже есть, её ставить не надо
    if calc_window.buffer[-1].count(".") == 0:
      calc_window.buffer[-1] += "."
      calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))
