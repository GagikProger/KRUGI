import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)
        self.btn1.clicked.connect(self.checker)
        self.btn2.clicked.connect(self.checker)
        self.btn3.clicked.connect(self.checker)
        self.btn4.clicked.connect(self.checker)
        self.btn5.clicked.connect(self.checker)
        self.btn6.clicked.connect(self.checker)
        self.btn7.clicked.connect(self.checker)
        self.btn8.clicked.connect(self.checker)
        self.btn9.clicked.connect(self.checker)
        self.btn0.clicked.connect(self.checker)
        self.btn_clear.clicked.connect(self.clr)
        self.btn_div.clicked.connect(self.checker)
        self.btn_mult.clicked.connect(self.checker)
        self.btn_minus.clicked.connect(self.checker)
        self.btn_plus.clicked.connect(self.checker)
        self.btn_pow.clicked.connect(self.checker)
        self.btn_sqrt.clicked.connect(self.checker)
        self.btn_dot.clicked.connect(self.checker)
        self.btn_fact.clicked.connect(self.checker)
        self.btn_eq.clicked.connect(self.checker)
        self.nmb = ""
        self.itoge = ""

    def checker(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())