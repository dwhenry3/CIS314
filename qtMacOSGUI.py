#pip install PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("MacOS Style Text Input Demo")
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
        
        # Apply MacOS-like styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
                font-family: "Helvetica Neue", sans-serif;
                color: #333;
            }
            QLineEdit {
                background-color: #FFFFFF;
                color: #333;
                padding: 8px;
                border: 1px solid #C0C0C0;
                border-radius: 5px;
                font-size: 14px;
                margin: 5px;
            }
            QPushButton {
                background-color: #E0E0E0;
                color: #333;
                border: 1px solid #A0A0A0;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #D0D0D0;
            }
            QLabel {
                font-size: 15px;
                margin-top: 15px;
                color: #333;
            }
        """)

        # Add subtle shadow effect for a MacOS-like feel
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)
        shadow_effect.setOffset(0, 2)
        shadow_effect.setColor(QColor(0, 0, 0, 50))
        container.setGraphicsEffect(shadow_effect)

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
