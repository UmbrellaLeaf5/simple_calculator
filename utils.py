from re import sub


class Stack:
    """
    Means:
        класс, представляющий собой стек строк (реализован на листе)
    """

    def __init__(self, items_list: list[str] = [""]):
        self.stack_ = items_list

    def is_empty(self) -> bool:
        """
        Returns:
            bool: пуст ли стек
        """

        return len(self.stack_) == 0

    def push(self, item: str):
        """
        Does: 
            добавляет элемент в стек

        Args:
            item (str): добавляемый элемент
        """

        self.stack_.append(item)

    def pop(self) -> str:
        """
        Means: 
            функция, которая удаляет последний элемент из стека

        RAISES:
            ValueError: в том случае, если стек пуст

        Returns:
            str: удаляемый элемент
        """

        if self.is_empty():
            raise ValueError("Stack is empty")

        return self.stack_.pop()

    def size(self) -> int:
        """
        Returns:
            int: размер стека
        """

        return len(self.stack_)

    def clear(self):
        """
        Does: 
            удаляет все элементы из стека
        """

        self.stack_ = []

    def math_reset(self):
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


def is_float(string: str) -> bool:
    try:
        float(string)
        return True

    except ValueError:
        return False


def remove_trailing_zeros(number: str) -> str:
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


def sci_format(expression: str) -> str:
    """
    Means:
        функция, которая переводит числа внутри выражения в научный стиль
        (меняет на экспоненциальную запись, если числа длиннее 16 символов)

    Args:
        expression (str): математическое выражение

    Returns:
        str: отформатированное математическое выражение
    """

    def convert(match: str) -> str:
        """
        Means:
            функция, которая 1 число в научный стиль
            (меняет на экспоненциальную запись, если число длиннее 16 символов)

        Args:
            match (str): изменяемое число

        Returns:
            str: отформатированное число
        """

        if len(match) > 15:  # большее кол-во символов плохо помещается
            return "{:e}".format(float(match))

        return match

    # я без понятия, как работают регулярные выражения, но они работают :)
    pattern = r"\b[+-]?\d+\.\d+(?:[eE][+-]?\d+)?\b|\b\d+(?:[eE][+-]?\d+)?\b"
    converted_expression = sub(
        pattern, lambda match: convert(match.group()), expression)

    return converted_expression


def view_output_format(text: str) -> str:
    """
    Means:
        функция, которая приводит строку в формат для пользователя

    Args:
        text (str): строка

    Returns:
        str: отформатированная строка
    """

    res: str = sci_format(text)
    res = res.replace('*', '×')
    res = res.replace("/", "÷")
    res = res.replace(".", ",")

    return res


def calc_format(number: float) -> str:
    """
    Means:
        функция, которая приводит число в формат для представления в стеке

    Args:
        number (float): число

    Returns:
        str: отформатированная строка
    """

    return remove_trailing_zeros(str(f"{number:.10f}"))
