"""
Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.
"""


class RedError:
    def __init__(self):
        print("Don't say red")

    def say(self):
        color = input('Say you color: ')
        assert color != 'red', 'ColorError, You are loser, never say "red"!'
        return color

    @staticmethod
    def print_color(word):
        print(f'Good, your color is {word}')


r = RedError()

while True:
    r.print_color(r.say())
