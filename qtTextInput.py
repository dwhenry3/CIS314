#pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 QLineEdit Example")
        self.resize(250, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your text...")
        layout.addWidget(self.input)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_text)
        layout.addWidget(submit_button)

    def submit_text(self):
        text = self.input.text()
        print(f"Submitted text: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())