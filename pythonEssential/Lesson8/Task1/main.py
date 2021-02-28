from random import randint

"""
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму
"""


QUANTITY = 10000


def filer_w():
    """
        Generated 10000 random integer numbers and saved they to the mytext.txt file on HDD/SSD disc.
    """
    f = open('my_text.txt', 'w')
    for _ in range(QUANTITY):
        number = randint(-1000, 1000)
        if _ == 0:
            f.write(f'{number}')
        else:
            f.write(f'*{number}')
    f.close()


def filer_r():
    """
        Read from a file, create a list of lines, convert to an integer list. Gets the sum from the integer list.
    """
    f = open('my_text.txt', 'r')
    read_list_str = f.read()
    read_list = read_list_str.split('*')
    f.close()

    int_list = list()
    for element in range(QUANTITY):
        int_list.append(int(read_list[element]))
    print(f'The sum is: {sum(int_list)}')


filer_w()
filer_r()
