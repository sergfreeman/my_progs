"""
Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
метод нажатия на кнопку.
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'From class Rectangle create figure rectangle: {self.a} X {self.b}'


class Button:
    @staticmethod
    def button_click():
        print('In object of class BUTTON this button is pushed!')


a = input('a = ')
b = int(input('b = '))
figure = Rectangle(a, b)
print(figure)

button = Button()
button.button_click()
