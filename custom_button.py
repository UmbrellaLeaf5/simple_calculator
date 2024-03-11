from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QPushButton, QApplication, QWidget
from PyQt6.QtGui import QColor
import sys


class CalcButton(QPushButton):

    _usual_style: str
    _pressed_style: str

    def __init__(self,  name: str,  min_width=100, min_height=75, bolded=True, italic=False,
                 color: str = "rgb(59, 59, 59);", hover_color: str = "rgb(50, 50, 50);", pressed_color: str = "rgb(40, 40, 40);",
                 parent=None):
        super().__init__(name, parent)
        self.setMinimumSize(QtCore.QSize(min_width, min_height))

        self._usual_style = """
            QPushButton {
                background-color:""" + color + """;
                border-radius: 5px;
                outline: none;
            }
            
            QPushButton:hover {
                background-color: """ + hover_color + """;
            }
            """

        self._pressed_style = """
            QPushButton {
                background-color:""" + pressed_color + """;
                border-radius: 5px;
                outline: none;
            }
            
            QPushButton:hover {
                background-color: """ + pressed_color + """;
            }
            """
        self.setStyleSheet(self._usual_style)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(bolded)
        font.setItalic(italic)
        self.setFont(font)

        self.setObjectName(name)

        # Создание тени
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(2, 2)

        # Применение тени к кнопке
        self.setGraphicsEffect(shadow)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.setStyleSheet(self._pressed_style)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.setStyleSheet(self._usual_style)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(461, 556)

    button = CalcButton("1", parent=window)

    window.show()

    sys.exit(app.exec())
