#pip install PyQt6
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class DotDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(QtGui.QColor("white"))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.setPen(QtGui.QPen(QtGui.QColor("black"), 5))
        painter.drawPoint(int(e.position().x()), int(e.position().y()))
        painter.end()
        self.label.setPixmap(canvas)

app = QtWidgets.QApplication(sys.argv)
window = DotDrawer()
window.show()
app.exec()