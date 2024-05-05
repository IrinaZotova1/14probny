import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt5 import uic


class AnimalCompatibilityApp(QMainWindow):
    def __init__(self):
        super(AnimalCompatibilityApp, self).__init__()
        uic.loadUi('primer.ui', self)
        self.setWindowTitle('Animal Compatibility Calculator')

        self.layout = QVBoxLayout()

        self.date_input = self.findChild(QLineEdit, 'line')
        self.calculate_button = self.findChild(QPushButton, 'Button')
        self.result_label = self.findChild(QLabel, 'label')
        self.date_input.setPlaceholderText(f"data")

        self.calculate_button.clicked.connect(self.calculate_animal_compatibility)
    def calculate_animal_compatibility(self):
        date = self.date_input.text()
        animal = determine_animal_compatibility(date)
        self.result_label.setText(f'The animal that suits you based on {date} is {animal}')


def determine_animal_compatibility(date):
    animals = ['Dog', 'Cat', 'Horse', 'Rabbit', 'Tiger', 'Snake', 'Monkey', 'Pig', 'Dragon', 'Sheep', 'Rooster', 'Ox']
    day = int(date.split('-')[-1])
    return animals[day % len(animals)]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    animal_app = AnimalCompatibilityApp()
    animal_app.show()
    sys.exit(app.exec_())
