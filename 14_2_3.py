
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton

class MathTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Math Test')
        self.layout = QVBoxLayout()

        self.question_label = QLabel('What is 2 + 2?')
        self.option1 = QRadioButton('3')
        self.option2 = QRadioButton('4')
        self.option3 = QRadioButton('5')

        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.option1)
        self.layout.addWidget(self.option2)
        self.layout.addWidget(self.option3)

        buttons_layout = QHBoxLayout()
        self.submit_button = QPushButton('Submit')
        self.result_label = QLabel('')
        self.submit_button.clicked.connect(self.show_result)
        buttons_layout.addWidget(self.submit_button)
        buttons_layout.addWidget(self.result_label)

        self.layout.addLayout(buttons_layout)
        self.setLayout(self.layout)

    def show_result(self):
        if self.option2.isChecked():
            self.result_label.setText('Correct!')
        else:
            self.result_label.setText('Incorrect')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    math_test_app = MathTestApp()
    math_test_app.show()
    sys.exit(app.exec_())


