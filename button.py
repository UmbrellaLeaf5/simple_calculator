from PyQt6 import QtCore, QtGui, QtWidgets


class CalcButton(QtWidgets.QPushButton):
    """
    MEANS:
        класс кнопки калькулятора
    """

    def __init__(self,  name: str,  min_width=100, min_height=75, bolded=True, italic=False,
                 color: str = "rgb(226, 226, 226);", back_color: str = "rgb(59, 59, 59);",
                 hover_color: str = "rgb(50, 50, 50);", pressed_color: str = "rgb(40, 40, 40);",
                 parent=None):
        super().__init__(name, parent)

        self.setMinimumSize(QtCore.QSize(min_width, min_height))

        # определение стиля для обычного состояния кнопки
        self._usual_style = """
            QPushButton {
                color: """ + color + """;
                background-color:""" + back_color + """;
                border-radius: 5px;
                outline: none;
            }
            
            QPushButton:hover {
                color: """ + color + """;
                background-color: """ + hover_color + """;
            }
            """

        # определение стиля для нажатого состояния кнопки
        self._pressed_style = """
            QPushButton {
                color: """ + color + """;
                background-color:""" + pressed_color + """;
                border-radius: 5px;
                outline: none;
            }
            
            QPushButton:hover {
                color: """ + color + """;
                background-color: """ + pressed_color + """;
            }
            """

        self.setStyleSheet(self._usual_style)

        # установка шрифта
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(bolded)
        font.setItalic(italic)
        self.setFont(font)

        self.setObjectName(name)

        # создание тени
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(2, 2)
        self.setGraphicsEffect(shadow)

    def mousePressEvent(self, event):
        """
        DOES:
            меняет цвет кнопки при клике мышкой

        ARGS:
            event (_type_): событие
        """

        super().mousePressEvent(event)
        self.setStyleSheet(self._pressed_style)

    def mouseReleaseEvent(self, event):
        """
        DOES:
            меняет цвет кнопки после клика мышкой

        ARGS:
            event (_type_): событие
        """

        super().mouseReleaseEvent(event)
        self.setStyleSheet(self._usual_style)


# на случай, если хотим глянуть, как это выглядит, прямо отсюда
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Window = QtWidgets.QWidget()
    Window.resize(100, 100)

    button = CalcButton("1", parent=Window)

    Window.show()

    sys.exit(app.exec())
