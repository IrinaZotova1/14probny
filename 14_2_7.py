
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests

class LandmarkApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Landmark Finder')

        self.layout = QVBoxLayout()

        self.city_input = QLineEdit()
        self.get_landmark_button = QPushButton('Get Landmark')
        self.landmark_label = QLabel('Landmark will appear here')

        self.get_landmark_button.clicked.connect(self.get_landmark)

        self.layout.addWidget(QLabel('Enter the name of a city:'))
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.get_landmark_button)
        self.layout.addWidget(self.landmark_label)

        self.setLayout(self.layout)

    def get_landmark(self):
        city = self.city_input.text()
        landmark = self.find_landmark(city)
        self.landmark_label.setText(landmark)

    def find_landmark(self, city):
        # Placeholder code to retrieve landmark - replace with real API call or database lookup
        landmarks = {
            "Paris": "Eiffel Tower",
            "Rome": "Colosseum",
            "London": "Big Ben",
            "New York": "Statue of Liberty"
            # Add more landmarks as needed
        }
        return landmarks.get(city, "Landmark not found")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    landmark_app = LandmarkApp()
    landmark_app.show()
    sys.exit(app.exec_())
