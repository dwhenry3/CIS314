#pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget

class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the input window
        self.setWindowTitle("Modern Text Input Demo")
        self.setGeometry(100, 100, 400, 200)
        
        # Create a QLineEdit for text input
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter text here")
        
        # Create a QPushButton to submit text
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.open_display_window)
        
        # Layout for input window
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.submit_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Apply modern styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #282c34;
                color: #ffffff;
                font-family: "Segoe UI", sans-serif;
            }
            QLineEdit {
                background-color: #1c1f24;
                color: #ffffff;
                padding: 8px;
                border: 1px solid #61afef;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #61afef;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4b8cd4;
            }
            QLabel {
                font-size: 16px;
                margin-top: 20px;
            }
        """)

    def open_display_window(self):
        # Retrieve text from QLineEdit
        text = self.line_edit.text()
        
        # Create and open the display window
        self.display_window = DisplayWindow(text)
        self.display_window.show()
        
        # Close the input window
        self.close()

class DisplayWindow(QMainWindow):
    def __init__(self, text):
        super().__init__()
        
        # Set up the display window
        self.setWindowTitle("Submitted Text Display")
        self.setGeometry(100, 100, 400, 200)
        
        # QLabel to display the submitted text
        self.display_label = QLabel(f"Submitted Text: {text}", self)
        
        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        
        # Layout for display window
        layout = QVBoxLayout()
        layout.addWidget(self.display_label)
        layout.addWidget(self.exit_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Apply the same modern styles as the input window
        self.setStyleSheet("""
            QMainWindow {
                background-color: #282c34;
                color: #ffffff;
                font-family: "Segoe UI", sans-serif;
            }
            QLabel {
                font-size: 16px;
                color: #ffffff;
            }
            QPushButton {
                background-color: #61afef;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4b8cd4;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    input_window = InputWindow()
    input_window.show()
    sys.exit(app.exec())
