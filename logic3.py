import random
from gui3 import *
from PyQt6.QtWidgets import *


class Logic(QMainWindow, Ui_NewMorganMoore3):
    def __init__(self):
        super().__init__()
        self.input = ""
        self.answer = ""
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self):
        try:
            self.input = self.input_values.text().split()
            self.num_values = len(self.input)
            for x in range(len(self.input)):
                self.input[x] = int(self.input[x])
            if self.num_values < 2:
                self.label_answer.setText('Need to provide at least 2 integers')
                self.clear()
            else:
                if self.dropdown_op.currentIndex() == 0:
                    self.answer = 'Answer = ' + self.add(self.input)
                    self.clear()
                    pass
                elif self.dropdown_op.currentIndex() == 1:
                    self.answer = 'Answer = ' + self.subtract(self.input)
                    self.clear()
                    pass
                elif self.dropdown_op.currentIndex() == 2:
                    self.answer = 'Answer = ' + self.multiply(self.input)
                    self.clear()
                    pass
                elif self.dropdown_op.currentIndex() == 3:
                    self.answer = 'Answer = ' + self.divide(self.input)
                    self.clear()
                    pass
                elif self.dropdown_op.currentIndex() == 4:
                    self.answer = 'Answer = ' + self.choose(self.input)
                    self.clear()
        finally:
            self.label_answer.setText(self.answer)
            self.clear()


    def clear(self):
        self.input_values.clear()
        self.dropdown_op.setCurrentIndex(0)

    def add(self, values):
        total = 0.0
        for x in values:
            if x >= 0:
                total += x
        return str(round(total, 2))


    def subtract(self, values):
        total = 0.0
        for x in values:
            if x <= 0:
                total += x
        return str(total)


    def multiply(self, values):
        total = 1.0
        count = 0
        for x in values:
            if x > 0:
                total *= x
            if x == 0:
                total = 0.0
            if x < 0:
                count += 1
                total *= abs(x)
            if count % 2 == 0:
                total = total
            if count % 2 == 1:
                total = -total
        return str(round(total, 2))


    def divide(self, values):
        total = 1.0
        count = 0
        if values[0] == 0:
            self.label_answer.setText("Answer = 0.0")
        for x in values[1:]:
            if x == 0:
                self.label_answer.setText("Cannot divide by zero")
            if x > 0:
                total /= abs(x)
            if x < 0:
                total /= abs(x)
                count += 1
            if count % 2 == 0:
                total = total
            if count % 2 == 1:
                total = -total
        return str(round(total, 2))


    def choose(self, values):
        n = 0
        for x in values:
            values[n] = x
            n += 1
        choice = random.choice(values)
        return str(round(choice, 2))
