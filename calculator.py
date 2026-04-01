import datetime

class Calculator:
    """A simple calculator class."""

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

if __name__ == '__main__':
    print("Current Date and Time (UTC):", datetime.datetime.utcnow())
    calc = Calculator()
    print(f'Adding 5 and 3 gives: {calc.add(5, 3)}')
    print(f'Subtracting 5 from 3 gives: {calc.subtract(3, 5)}')
    print(f'Multiplying 5 and 3 gives: {calc.multiply(5, 3)}')
    print(f'Dividing 5 by 2 gives: {calc.divide(5, 2)}')