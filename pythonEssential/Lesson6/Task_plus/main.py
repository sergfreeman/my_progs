"""
Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
указывая параметры.
"""

my_dict = dict(one=1, two=2, three=3, four=4, five=5)


def dict_actions(some_dict):
    if some_dict == my_dict:
        print(my_dict.values())
    else:
        print(my_dict.get(some_dict))


dict_actions('five')
dict_actions(my_dict)
dict_actions('one')
