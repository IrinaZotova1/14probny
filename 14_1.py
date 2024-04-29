
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QPushButton, QComboBox, QLineEdit, QLabel
import requests


class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Currency Converter')
        layout = QVBoxLayout()

        self.amount_input = QLineEdit(self)
        self.from_currency = QComboBox()
        self.to_currency = QComboBox()
        self.to_amount_label = QLabel()

        form_layout = QFormLayout()
        form_layout.addRow('Amount:', self.amount_input)
        form_layout.addRow('From Currency:', self.from_currency)
        form_layout.addRow('To Currency:', self.to_currency)
        form_layout.addRow('Converted Amount:', self.to_amount_label)

        convert_button = QPushButton('Convert')
        convert_button.clicked.connect(self.convert_currency)

        layout.addLayout(form_layout)
        layout.addWidget(convert_button)
        self.setLayout(layout)

        self.populate_currencies()

    def populate_currencies(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        currencies = ["USD"] + list(data['rates'].keys())
        self.from_currency.addItems(currencies)
        self.to_currency.addItems(currencies)

    def convert_currency(self):
        amount = float(self.amount_input.text())
        from_currency = self.from_currency.currentText()
        to_currency = self.to_currency.currentText()

        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        data = response.json()
        exchange_rate = data['rates'][to_currency]
        converted_amount = amount * exchange_rate

        self.to_amount_label.setText(str(round(converted_amount, 2)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec_())
