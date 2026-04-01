import datetime
import math

class Calculator:
    """A simple calculator class with advanced features."""

    @staticmethod
    def add(x, y):
        """두 수를 더합니다"""
        return x + y
    
    @staticmethod
    def subtract(x, y):
        """두 수를 뺍니다"""
        return x - y
    
    @staticmethod
    def multiply(x, y):
        """두 수를 곱합니다"""
        return x * y
    
    @staticmethod
    def divide(x, y):
        """두 수를 나눕니다"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
    
    @staticmethod
    def modulo(x, y):
        """나머지를 구합니다"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x % y
    
    @staticmethod
    def power(x, y):
        """지수 연산을 합니다"""
        return x ** y
    
    @staticmethod
    def square_root(x):
        """제곱근을 구합니다"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(x)
    
    @staticmethod
    def factorial(n):
        """팩토리얼을 계산합니다"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        return math.factorial(int(n))
    
    @staticmethod
    def sin(x):
        """사인 값을 구합니다 (라디안)"""
        return math.sin(x)
    
    @staticmethod
    def cos(x):
        """코사인 값을 구합니다 (라디안)"""
        return math.cos(x)
    
    @staticmethod
    def tan(x):
        """탄젠트 값을 구합니다 (라디안)"""
        return math.tan(x)
    
    @staticmethod
    def log(x, base=10):
        """로그 값을 구합니다"""
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers!")
        return math.log(x, base)

def interactive_calculator():
    """대화형 계산기 메인 함수"""
    calc = Calculator()
    
    print("=" * 50)
    print("         Python 공학용 계산기에 오신 것을 환영합니다")
    print("=" * 50)
    
    while True:
        print("\n선택하세요:")
        print("1. 더하기 (+)")
        print("2. 빼기 (-)")
        print("3. 곱하기 (*)")
        print("4. 나누기 (/)")
        print("5. 나머지 (%)")
        print("6. 지수 (x^y)")
        print("7. 제곱근 (√)")
        print("8. 팩토리얼 (!)")
        print("9. 삼각함수 (sin, cos, tan)")
        print("10. 로그 (log)")
        print("0. 종료")
        
        choice = input("\n연산을 선택하세요 (0-10): ")
        
        if choice == '0':
            print("\n계산기를 종료합니다. 감사합니다!")
            break
        
        try:
            if choice in ('1', '2', '3', '4', '5', '6'):
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                num2 = float(input("두 번째 숫자를 입력하세요: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"\n{num1} * {num2} = {result}")
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
                elif choice == '5':
                    result = calc.modulo(num1, num2)
                    print(f"\n{num1} % {num2} = {result}")
                elif choice == '6':
                    result = calc.power(num1, num2)
                    print(f"\n{num1} ^ {num2} = {result}")
                    
            elif choice == '7':
                num = float(input("숫자를 입력하세요: "))
                result = calc.square_root(num)
                print(f"\n√{num} = {result}")
                
            elif choice == '8':
                num = float(input("숫자를 입력하세요: "))
                result = calc.factorial(num)
                print(f"\n{num}! = {result}")
                
            elif choice == '9':
                print("삼각함수를 선택하세요:")
                print("1. sin")
                print("2. cos")
                print("3. tan")
                trig_choice = input("선택 (1-3): ")
                num = float(input("라디안 값을 입력하세요: "))
                
                if trig_choice == '1':
                    result = calc.sin(num)
                    print(f"\nsin({num}) = {result}")
                elif trig_choice == '2':
                    result = calc.cos(num)
                    print(f"\ncos({num}) = {result}")
                elif trig_choice == '3':
                    result = calc.tan(num)
                    print(f"\ntan({num}) = {result}")
                    
            elif choice == '10':
                num = float(input("숫자를 입력하세요: "))
                base = input("밑을 입력하세요 (기본값: 10): ")
                base = float(base) if base else 10
                result = calc.log(num, base)
                print(f"\nlog_{base}({num}) = {result}")
                
        except ValueError as e:
            print(f"\n오류: {e}")
        except Exception as e:
            print(f"\n예상치 못한 오류: {e}")

if __name__ == '__main__':
    print("Current Date and Time (UTC):", datetime.datetime.utcnow())
    interactive_calculator()