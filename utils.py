from re import sub


class Stack:
    """
    MEANS:
        класс, представляющий собой стек строк (реализован на листе)
    """

    def __init__(self, items_list: list[str] = []):
        self.stack_ = items_list

    def is_empty(self) -> bool:
        """
        RETURNS:
            bool: пуст ли стек
        """

        return len(self.stack_) == 0

    def push(self, item: str):
        """
        DOES: 
            добавляет элемент в стек

        ARGS:
            item (str): добавляемый элемент
        """

        self.stack_.append(item)

    def pop(self) -> str:
        """
        MEANS: 
            функция, которая удаляет последний элемент из стека

        RAISES:
            ValueError: в том случае, если стек пуст

        RETURNS:
            str: удаляемый элемент
        """

        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack_.pop()

    def size(self) -> int:
        """
        RETURNS:
            int: размер стека
        """

        return len(self.stack_)

    def clear(self):
        """
        DOES: 
            удаляет все элементы из стека
        """

        self.stack_ = []

    def math_reset(self):
        """
        DOES: 
            удаляет все элементы из стека, оставляя "0"
        """

        self.stack_ = ["0"]

    def __setitem__(self, index: int, item: str):
        """
        DOES:
            меняет элемент по определенному индексу
            (обращаться можно только к последнему)

        ARGS:
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
        ARGS:
            index (int): индекс (обращаться можно только к последнему)

        RAISES:
            IndexError: в том случае, если индекс не последний

        RETURNS:
            str: элемент по индексу
        """

        if index == len(self.stack_) - 1 or index == -1:
            return self.stack_[index]

        else:
            raise IndexError("Invalid index")


def is_float(string):
    try:
        float(string)
        return True

    except ValueError:
        return False


def remove_trailing_zeros(number: str) -> str:
    """
    MEANS:
        функция, которая удаляет незначащие нули из числа, представленного строкой

    ARGS:
        number (str): изменяемое число

    RETURNS:
        str: обрезанное число
    """

    if "." in number:
        number = number.rstrip("0").rstrip(".")

    return number


def sci_format(expression: str) -> str:
    """
    MEANS:
        функция, которая переводит числа внутри выражения в научный стиль
        (меняет на экспоненциальную запись, если числа длиннее 16 символов)

    ARGS:
        expression (str): математическое выражение

    RETURNS:
        str: отформатированное математическое выражение
    """

    def convert(match: str) -> str:
        """
        MEANS:
            функция, которая 1 число в научный стиль
            (меняет на экспоненциальную запись, если число длиннее 16 символов)

        ARGS:
            match (str): изменяемое число

        RETURNS:
            str: отформатированное число
        """

        if len(match) > 16:
            # return remove_trailing_zeros("{:e}".format(float(match)))
            # return remove_trailing_zeros(match)
            return "{:e}".format(float(match))

        return match

    # я без понятия, как работают регулярные выражения, но они работают :)
    pattern = r"\b[+-]?\d+\.\d+(?:[eE][+-]?\d+)?\b|\b\d+(?:[eE][+-]?\d+)?\b"
    converted_expression = sub(pattern, lambda match: convert(match.group()), expression)

    return converted_expression


def calc_format(text: str) -> str:
    """
    MEANS:
        функция, которая приводит строку в формат для калькулятора

    ARGS:
        text (str): строка

    RETURNS:
        str: отформатированная строка
    """

    res: str = sci_format(text)
    res = res.replace('*', '×')
    res = res.replace("/", "÷")
    res = res.replace(".", ",")

    return res
