
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')

        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.layout.addWidget(self.display)

        buttons_layout = QVBoxLayout()

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '=', '+']
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            buttons_layout.addLayout(row_layout)

        self.layout.addLayout(buttons_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.insert(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

