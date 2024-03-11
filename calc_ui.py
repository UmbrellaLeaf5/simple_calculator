from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtCore import QSize
from custom_button import CalcButton


class Ui_Form(object):
    def setupUi(self, Window):
        Window.setObjectName("Calculator")
        Window.setFixedSize(QSize(465, 550))
        Window.setStyleSheet("color: rgb(226, 226, 226); background-color: rgb(32, 32, 32);")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 555))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_percent = CalcButton(
            "pushButton_percent", min_height=50, parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_percent, 0, 0, 1, 1)

        self.pushButton_CE = CalcButton(
            "pushButton_CE", min_height=50, italic=True, parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_CE, 0, 1, 1, 1)

        self.pushButton_C = CalcButton(
            "pushButton_C", min_height=50, italic=True, parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_C, 0, 2, 1, 1)

        self.pushButton_del = CalcButton(
            "pushButton_del", min_height=50, italic=True, parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_C, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.pushButton_del, 0, 3, 1, 1)

        self.pushButton_rev = CalcButton("pushButton_rev", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_rev, 1, 0, 1, 1)

        self.pushButton_sqr = CalcButton("pushButton_sqr", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_sqr, 1, 1, 1, 1)

        self.pushButton_sqrt = CalcButton("pushButton_sqrt", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_sqrt, 1, 2, 1, 1)

        self.pushButton_div = CalcButton("pushButton_div", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)

        self.pushButton_1 = CalcButton("pushButton_1", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)

        self.pushButton_2 = CalcButton("pushButton_2", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_3 = CalcButton("pushButton_3", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_mul = CalcButton("pushButton_mul", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)

        self.pushButton_4 = CalcButton("pushButton_4", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_5 = CalcButton("pushButton_5", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_6 = CalcButton("pushButton_6", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_minus = CalcButton("pushButton_minus", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)

        self.pushButton_7 = CalcButton("pushButton_7", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.pushButton_8 = CalcButton("pushButton_8", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)

        self.pushButton_9 = CalcButton("pushButton_9", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)

        self.pushButton_plus = CalcButton("pushButton_plus", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)

        self.pushButton_neg = CalcButton("pushButton_neg", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_neg, 5, 0, 1, 1)

        self.pushButton_0 = CalcButton("pushButton_0", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)

        self.pushButton_dot = CalcButton("pushButton_dot", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_dot, 5, 2, 1, 1)

        self.pushButton_eq = CalcButton("pushButton_eq", parent=self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.pushButton_eq, 5, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Calculator"))

        self.pushButton_percent.setText(_translate("Window", "%"))
        self.pushButton_CE.setText(_translate("Window", "CE"))
        self.pushButton_C.setText(_translate("Window", "C"))
        self.pushButton_del.setText(_translate("Window", "DEL"))

        self.pushButton_rev.setText(_translate("Window", "⅟"))
        self.pushButton_sqr.setText(_translate("Window", "x²"))
        self.pushButton_sqrt.setText(_translate("Window", "√x"))
        self.pushButton_div.setText(_translate("Window", "÷"))

        self.pushButton_1.setText(_translate("Window", "1"))
        self.pushButton_2.setText(_translate("Window", "2"))
        self.pushButton_3.setText(_translate("Window", "3"))
        self.pushButton_mul.setText(_translate("Window", "×"))

        self.pushButton_4.setText(_translate("Window", "4"))
        self.pushButton_5.setText(_translate("Window", "5"))
        self.pushButton_6.setText(_translate("Window", "6"))
        self.pushButton_minus.setText(_translate("Window", "-"))

        self.pushButton_7.setText(_translate("Window", "7"))
        self.pushButton_8.setText(_translate("Window", "8"))
        self.pushButton_9.setText(_translate("Window", "9"))
        self.pushButton_plus.setText(_translate("Window", "+"))

        self.pushButton_neg.setText(_translate("Window", "∓"))
        self.pushButton_0.setText(_translate("Window", "0"))
        self.pushButton_dot.setText(_translate("Window", ","))
        self.pushButton_eq.setText(_translate("Window", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
