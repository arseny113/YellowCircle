import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class DrawCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.color = QColor(255, 255, 0)
        self.flag = False
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.painter = QPainter()
            self.painter.begin(self)
            self.painter.setBrush(self.color)
            r = randint(1, 200)
            self.painter.drawEllipse(200, 200, r, r)
            self.painter.end()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DrawCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


