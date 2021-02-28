"""
Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
данного текста.
"""


def set_text():
    str_txt = input("Enter some text:")
    return str_txt


def list_creator(my_str):
    my_list = my_str.split(sep=' ')
    return my_list


the_list = list_creator(set_text())
the_list.sort()
print(the_list)

