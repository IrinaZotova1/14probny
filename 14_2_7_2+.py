
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton


class LandmarkApp(QMainWindow):
    def __init__(self):
        super(LandmarkApp, self).__init__()
        uic.loadUi('primer.ui', self)
        self.setWindowTitle('Landmark Finder')

        self.line = self.findChild(QLineEdit, 'line')
        self.Button = self.findChild(QPushButton, 'Button')
        self.label = self.findChild(QLabel, 'label')
        self.line.setPlaceholderText(f"data")

        self.Button.clicked.connect(self.get_landmark)

    def get_landmark(self):
        city = self.line.text()
        landmark = self.find_landmark(city)
        self.label.setText(landmark)

    def find_landmark(self, city):
        landmarks = {
            "Paris": "Eiffel Tower",
            "Rome": "Colosseum",
            "London": "Big Ben",
            "New York": "Statue of Liberty"
        }
        return landmarks.get(city, "Landmark not found")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    landmark_app = LandmarkApp()
    landmark_app.show()
    sys.exit(app.exec_())
