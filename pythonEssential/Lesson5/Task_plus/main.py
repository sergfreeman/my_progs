"""
Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
отсортированной в порядке возрастания.
"""


def set_text():
    str_txt = input("Enter some numbers separate space:")

    return str_txt


def list_creator(my_str):
    my_list = my_str.split(sep=' ')
    return my_list


the_list_txt = list_creator(set_text())

the_list = list()
for i in range(len(the_list_txt)):
    the_list.append(int(the_list_txt[i]))
print(f'Entered list: {the_list}')

for _ in range(len(the_list)):
    for val in range(len(the_list)):
        if val == 0:
            pass
        elif the_list[val] < the_list[val - 1]:
            the_list[val], the_list[val - 1] = the_list[val - 1], the_list[val]


print(f'Sorted list:{the_list}')

