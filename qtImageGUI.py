#pip install PyQt6
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class ImageTextWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Image with Text Example")
        self.setGeometry(100, 100, 800, 800)

        # Set up the layout
        layout = QVBoxLayout()

        # Create QLabel to display image
        image_label = QLabel(self)
        pixmap = QPixmap("dog_of_the_day.jpg")  # Replace with the path to your image
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image

        # Create QLabel to display text
        text_label = QLabel("Dog of the Day - Juliet.", self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text

        # Add the image label and text label to the layout
        layout.addWidget(image_label)
        layout.addWidget(text_label)

        # Set the layout for the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the window
    window = ImageTextWindow()
    window.show()

    sys.exit(app.exec())
