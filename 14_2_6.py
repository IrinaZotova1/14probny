
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class MathProblemApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Math Problem Solver')

        self.layout = QVBoxLayout()

        self.problem_label = QLabel('')
        self.user_input = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.result_label = QLabel('')

        self.submit_button.clicked.connect(self.check_answer)

        self.generate_problem()

        self.layout.addWidget(self.problem_label)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def generate_problem(self):
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        problem = f'{num1} {operation} {num2}'

        self.problem_label.setText(problem)

    def check_answer(self):
        problem = self.problem_label.text()
        user_answer = self.user_input.text()
        num1, operation, num2 = problem.split(' ')
        num1, num2 = int(num1), int(num2)

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        elif operation == '/':
            correct_answer = num1 / num2

        if user_answer == str(correct_answer):
            self.result_label.setText('Correct!')
        else:
            self.result_label.setText('Incorrect. Try again.')
        self.user_input.clear()
        self.generate_problem()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    math_app = MathProblemApp()
    math_app.show()
    sys.exit(app.exec_())


