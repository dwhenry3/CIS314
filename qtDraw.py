# pip install PyQT6
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 460, 300)
        self.setWindowTitle('Rectangle')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawRect(qp)
        qp.end()

    def drawRect(self, qp):
        qp.setBrush(QBrush(QColor(255, 0, 0)))  # Set brush color to red
        qp.drawRect(30, 10, 120, 80)  # Draw rectangle

        qp.setBrush(QBrush(QColor(0, 255, 0)))  # Set brush color to green
        qp.drawRect(150, 10, 120, 80)  # Draw rectangle

        qp.setBrush(QBrush(QColor(0, 0, 255)))  # Set brush color to red
        qp.drawRect(270, 10, 120, 80)  # Draw rectangle

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())