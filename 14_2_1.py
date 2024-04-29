
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Timer')
        layout = QVBoxLayout()

        self.timer_label = QLabel('Set timer (seconds):', self)
        self.time_input = QLineEdit(self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.stop_button.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)

        layout.addWidget(self.timer_label)
        layout.addWidget(self.time_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

    def start_timer(self):
        time_in_seconds = int(self.time_input.text())
        self.timer.start(time_in_seconds * 1000)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())

