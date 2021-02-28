"""
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
отрицательную степень.
"""


class Calc:

    def input_val(self):
        while True:
            try:
                val = float(input(f'Value = '))
                return val
            except (TypeError, ValueError):
                print('Illegal value, try again!')

    def __add__(self, a, b):
        return a + b

    def __sub__(self, a, b):
        return a - b

    def __mul__(self, a, b):
        return a * b

    def __truediv__(self, a, b):
        return a / b

    def __pow__(self, a, b):
        if b < 0:
            print('Second value < 0')
        else:
            return pow(a, b)

    def operation(self):
        while True:
            val1 = self.input_val()
            val2 = self.input_val()
            operation = input('Select come operation(+ - * / ^) or "exit" to close program:')

            if operation == '+':
                print(self.__add__(val1, val2))
            if operation == '-':
                print(self.__sub__(val1, val2))
            elif operation == '/':
                if val2 == 0:
                    print('Division by zero')
                else:
                    print(self.__truediv__(val1, val2))
            elif operation == '*':
                print(self.__mul__(val1, val2))
            elif operation == '^':
                if val2 < 0:
                    print('Value is less then zero')
                else:
                    print(self.__pow__(val1, val2))
            elif operation == 'exit':
                exit(0)
            else:
                print('Unsupported operation')

            print()


c = Calc()
c.operation()

