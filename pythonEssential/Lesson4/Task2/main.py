"""
Перепишите решение первого задания с помощью генератора.
"""

my_numbers = [23, 2, 112, 8, 548, 237]


def reverse_enum(my_numbers):
    for index in reversed(range(len(my_numbers))):
        yield my_numbers[index]


for item in reverse_enum(my_numbers):
    print(item)