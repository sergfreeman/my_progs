"""
Создайте иерархию классов с использованием множественного наследования. Выведите на экран
порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
классов выглядят именно так.
"""
import random

class Father:
    gender = 'Male'
    eye_color = 'blue'
    love_to_beer = True


class Mother:
    gender = 'Female'
    eye_color = 'brown'
    love_to_theatre = True

class Child(Father, Mother):
    def __init__(self):

        print('If value is not define in current class, value will find in first lefts parent class')

    def play_games(self):
        print('Love play games')

child = Child()
child.play_games()
print(f'Gender is:{child.gender}')
print(f'Color eyes is:{child.eye_color}')
print(f'Love to beer:{child.love_to_beer}')
print(f'Love to theatre:{child.love_to_theatre}')