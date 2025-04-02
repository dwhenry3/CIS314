#pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello, CIS 314!")
window.setGeometry(100, 100, 400, 200)

label = QLabel("Hello, CIS 314!", window)
label.move(150, 80)

button = QPushButton("Click me!", window)
button.move(150, 120)

exit_button = QPushButton("Exit", window)
exit_button.clicked.connect(app.quit)
exit_button.move(150, 150)

window.show()

sys.exit(app.exec())