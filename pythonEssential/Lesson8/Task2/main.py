from random import randint
import pickle

"""
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму

Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными 
файлами. 
"""


QUANTITY = 10000


def filer_w():
    """
        Generated 10000 random integer numbers and saved they to the my_binary.dat file on HDD/SSD disc.
    """
    f = open('my_binary.dat', 'wb')
    for _ in range(QUANTITY):
        number = randint(-1000, 1000)
        pickle.dump(number, f)
    f.close()


def filer_r():
    """
        Read from a binary file, create a integer list. Gets the sum from the integer list.
    """
    read_list = list()
    f = open('my_binary.dat', 'rb')
    for _ in range(QUANTITY):
        read_list.append(pickle.load(f))


filer_w()
filer_r()
