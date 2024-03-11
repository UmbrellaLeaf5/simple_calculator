from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QPushButton, QApplication, QWidget
from PyQt6.QtGui import QColor
import sys


class CalcButton(QPushButton):
    def __init__(self,  name: str, min_height=100, min_width=75, parent=None):
        super().__init__(name, parent)
        self.setMinimumSize(QtCore.QSize(min_height, min_width))
        self.setCheckable(True)

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.setFont(font)

        self.setObjectName(name)

        self.setStyleSheet(
            "background-color: rgb(59, 59, 59); border-radius: 5px; outline: none")

        # Создание тени
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(4)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(2, 2)

        # Применение тени к кнопке
        self.setGraphicsEffect(shadow)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.setStyleSheet(
            "background-color: rgb(50, 50, 50); border-radius: 5px; outline: none")

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.setStyleSheet(
            "background-color: rgb(59, 59, 59); border-radius: 5px; outline: none")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(461, 556)

    button = NumButton("1", window)
    button = OperButton("+", window)

    window.show()

    sys.exit(app.exec())
