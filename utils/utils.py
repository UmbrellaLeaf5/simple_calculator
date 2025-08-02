from re import sub


class Stack:
  """
  Means:
      класс, представляющий собой стек строк (реализован на листе)
  """

  def __init__(self, items_list: list[str] | None = None):
    if items_list is None:
      items_list = [""]

    self.stack_ = items_list

  def IsEmpty(self) -> bool:
    """
    Returns:
        bool: пуст ли стек
    """

    return len(self.stack_) == 0

  def Push(self, item: str):
    """
    Does:
        добавляет элемент в стек

    Args:
        item (str): добавляемый элемент
    """

    self.stack_.append(item)

  def Pop(self) -> str:
    """
    Means:
        функция, которая удаляет последний элемент из стека

    RAISES:
        ValueError: в том случае, если стек пуст

    Returns:
        str: удаляемый элемент
    """

    if self.IsEmpty():
      raise ValueError("Stack is empty")

    return self.stack_.pop()

  def Size(self) -> int:
    """
    Returns:
        int: размер стека
    """

    return len(self.stack_)

  def Clear(self):
    """
    Does:
        удаляет все элементы из стека
    """

    self.stack_ = []

  def MathReset(self):
    """
    Does:
        удаляет все элементы из стека, оставляя "0"
    """

    self.stack_ = ["0"]

  def __setitem__(self, index: int, item: str):
    """
    Does:
        меняет элемент по определенному индексу
        (обращаться можно только к последнему)

    Args:
        index (int): индекс
        item (str): изменяемый элемент

    RAISES:
        IndexError: в том случае, если индекс не последний
    """

    if index == len(self.stack_) - 1 or index == -1:
      self.stack_[index] = item

    else:
      raise IndexError("Invalid index")

  def __getitem__(self, index: int) -> str:
    """
    Args:
        index (int): индекс (обращаться можно только к последнему)

    RAISES:
        IndexError: в том случае, если индекс не последний

    Returns:
        str: элемент по индексу
    """

    if index == len(self.stack_) - 1 or index == -1:
      return self.stack_[index]

    else:
      raise IndexError("Invalid index")


def IsFloat(string: str) -> bool:
  try:
    float(string)
    return True

  except ValueError:
    return False


def RemoveTrailingZeros(number: str) -> str:
  """
  Means:
      функция, которая удаляет незначащие нули из числа, представленного строкой

  Args:
      number (str): изменяемое число

  Returns:
      str: обрезанное число
  """

  if "." in number:
    number = number.rstrip("0").rstrip(".")

  return number


def ScientificFormat(expression: str) -> str:
  """
  Means:
      функция, которая переводит числа внутри выражения в научный стиль
      (меняет на экспоненциальную запись, если числа длиннее 16 символов)

  Args:
      expression (str): математическое выражение

  Returns:
      str: отформатированное математическое выражение
  """

  def Convert(match: str) -> str:
    """
    Means:
        функция, которая 1 число в научный стиль
        (меняет на экспоненциальную запись, если число длиннее 16 символов)

    Args:
        match (str): изменяемое число

    Returns:
        str: отформатированное число
    """

    max_beauty_chars_amount: int = 15  # большее кол-во символов плохо помещается

    if len(match) > max_beauty_chars_amount:
      return f"{float(match):e}"

    return match

  # я без понятия, как работают регулярные выражения, но они работают :)
  pattern = r"\b[+-]?\d+\.\d+(?:[eE][+-]?\d+)?\b|\b\d+(?:[eE][+-]?\d+)?\b"
  converted_expression = sub(pattern, lambda match: Convert(match.group()), expression)

  return converted_expression


def ViewOutputFormat(text: str) -> str:
  """
  Means:
      функция, которая приводит строку в формат для пользователя

  Args:
      text (str): строка

  Returns:
      str: отформатированная строка
  """

  res: str = ScientificFormat(text)
  res = res.replace("*", "×")
  res = res.replace("/", "÷")
  res = res.replace(".", ",")

  return res


def CalcFormat(number: float) -> str:
  """
  Means:
      функция, которая приводит число в формат для представления в стеке

  Args:
      number (float): число

  Returns:
      str: отформатированная строка
  """

  return RemoveTrailingZeros(str(f"{number:.10f}"))
