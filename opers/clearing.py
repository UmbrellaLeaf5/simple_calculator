from utils.utils import IsFloat, ViewOutputFormat


def Clear(calc_window):
  """
  DOES
      очищает всё: и буфер, и текущую строку
  """

  calc_window.buffer.MathReset()
  calc_window.ui.labelExpression.setText("")
  calc_window.ui.labelEval.setText("0")


def ClearEvaluation(calc_window):
  """
  DOES
      очищает текущую строку
  """

  if IsFloat(calc_window.buffer[-1]):
    calc_window.buffer[-1] = "0"

  else:
    calc_window.buffer.Push("0")

  calc_window.ui.labelEval.setText("0")


def Delete(calc_window):
  """
  DOES
      удаляет последний символ
  """

  if IsFloat(calc_window.buffer[-1]):
    if calc_window.buffer[-1] == "0":
      Clear(calc_window)

    calc_window.buffer[-1] = calc_window.buffer[-1][0:-1]

    if calc_window.buffer[-1] == "":
      calc_window.buffer[-1] = "0"

    calc_window.ui.labelEval.setText(ViewOutputFormat(calc_window.buffer[-1]))
