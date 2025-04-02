#pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("Modern Text Input Demo")
        self.setGeometry(100, 100, 400, 200)
        
        # Create a QLineEdit for text input
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter text here")
        
        # Create a QPushButton to submit text
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.display_text)
        
        # QLabel to display the submitted text (initially hidden)
        self.display_label = QLabel("", self)
        self.display_label.setVisible(False)
        
        # Exit button (initially hidden)
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.exit_button.setVisible(False)
        
        # Layout for main window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.display_label)
        self.layout.addWidget(self.exit_button)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
        # Apply styles
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
        '''self.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e2e;
            color: #cdd6f4;
            font-family: "Segoe UI", sans-serif;
        }

        QLineEdit {
            background-color: #313244;
            color: #cdd6f4;
            padding: 8px;
            border: 1px solid #a6e3a1;
            border-radius: 6px;
            font-size: 14px;
        }

        QLineEdit:focus {
            border: 1px solid #94e2d5;
            background-color: #45475a;
        }

        QPushButton {
            background-color: #94e2d5;
            color: #1e1e2e;
            border: none;
            padding: 10px 15px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #74c7ec;
        }

        QPushButton:pressed {
            background-color: #40a8a3;
        }

        QLabel {
            font-size: 16px;
            margin-top: 10px;
            color: #cdd6f4;
        }
        """)'''

    def display_text(self):
        # Retrieve text from QLineEdit
        text = self.line_edit.text()
        
        # Set text to the display_label and show it
        self.display_label.setText(f"Submitted Text: {text}")
        self.display_label.setVisible(True)
        
        # Remove the input widgets from the layout
        self.layout.removeWidget(self.line_edit)
        self.layout.removeWidget(self.submit_button)
        
        # Hide the input widgets
        self.line_edit.deleteLater()
        self.submit_button.deleteLater()
        
        # Show the exit button
        self.exit_button.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
