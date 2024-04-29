
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class CompatibilityCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Compatibility Calculator')

        self.layout = QVBoxLayout()

        self.date1_input = QLineEdit()
        self.date2_input = QLineEdit()
        self.calculate_button = QPushButton('Calculate')
        self.result_label = QLabel('')

        self.calculate_button.clicked.connect(self.calculate_compatibility)

        self.layout.addWidget(QLabel('Enter first date (YYYY-MM-DD):'))
        self.layout.addWidget(self.date1_input)
        self.layout.addWidget(QLabel('Enter second date (YYYY-MM-DD):'))
        self.layout.addWidget(self.date2_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate_compatibility(self):
        date1 = self.date1_input.text()
        date2 = self.date2_input.text()

        # Add compatibility calculation logic here
        compatibility = "80%"  # Placeholder value

        self.result_label.setText(f'Compatibility of {date1} and {date2}: {compatibility}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CompatibilityCalculator()
    calculator.show()
    sys.exit(app.exec_())

