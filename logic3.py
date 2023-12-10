import random
from gui3 import *
from PyQt6.QtWidgets import *


class Logic(QMainWindow, Ui_NewMorganMoore3):
    def __init__(self) -> None:
        '''
        Method that sets class variables
        '''
        super().__init__()
        # class variables
        self.input = ""
        self.answer = ""
        self.setupUi(self)
        # calling submit button
        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        '''
        Method that converts input to list of integers, and then does the selected mathematical method (eg. add, subtract, multiply, divide, choose)
        '''
        # try block then finally
        try:
            # getting values into int list
            self.input = self.input_values.text().split()
            self.num_values = len(self.input)
            for x in range(len(self.input)):
                self.input[x] = int(self.input[x])
                self.clear()
            # catches if length is less than 2 integers
            if self.num_values < 2:
                self.answer = 'Need to provide at least 2 numbers'
                self.label_answer.setText(self.answer)
                self.clear()
            # if not, then run the math based on dropdown options index
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
            # prints out answer in answer label
            self.label_answer.setText(self.answer)
            self.clear()


    def clear(self) -> None:
        '''
        Method that clears the input values and sets dropdown back to add
        '''
        # clears input values and sets dropdown back to add
        self.input_values.clear()
        self.dropdown_op.setCurrentIndex(0)

    def add(self, values) -> str:
        '''
        Method that adds positive values together
        :param values: self, list of values
        :return: str
        '''
        # adds positive values together
        total = 0.0
        for x in values:
            if x >= 0:
                total += x
        return str(round(total, 2))


    def subtract(self, values) -> str:
        '''
        Method that gets difference of negative values
        :param values: self, list of values
        :return: str
        '''
        # gets difference of negative values
        total = 0.0
        for x in values:
            if x <= 0:
                total += x
        return str(total)


    def multiply(self, values) -> str:
        '''
        Method that multiplies values and makes sure to apply multiplication rules to negative values used
        :param values: self, list of values
        :return: str
        '''
        # multiplies values, if negative makes sure total is negative if odd amount of negative values
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


    def divide(self, values) -> str:
        '''
        Method that divides values and makes sure to apply division rules to negative values used
        :param values: self, list of values
        :return: str
        '''
        # divides values, if negative makes sure total is negative if odd amount of negative values
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


    def choose(self, values) -> str:
        '''
        Method that chooses a random values from the given list
        :param values: self, list of values
        :return: str
        '''
        # chooses random values in list
        n = 0
        for x in values:
            values[n] = x
            n += 1
        choice = random.choice(values)
        return str(round(choice, 2))
