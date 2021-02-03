# 1. Вы принимаете от пользователя последовательность чисел,
# разделённых запятой. Составьте список

# digit_string = "1,4,9,25.55,89,-3,245.01,0,-327,99,5,99,75"
#
#
# def transform(string):
#     my_digit_list = string.split(',')
#     return my_digit_list
#
#
# print(transform(digit_string))

# 2. Выведите первый и последний элемент списка.

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '5', '99', '237', '75', '22']
#
#
# def first_and_last(my_list):
#     first_element = my_list[0]
#     last_element = my_list[-1]
#     print(f"The first element is:{first_element}, the last element is:{last_element}")
#
#
# first_and_last(the_list)


# 3. При заданном целом числе n посчитайте n + nn + nnn.

# number = int(input("function is: n + nn + nnn,  write your N: "))
#
#
# def multi(result):
#     result = result + pow(result, 2) + pow(result, 3)
#     return result
#
#
# print(multi(number))
# 4. Напишите программу, которая выводит чётные числа из
# заданного списка и останавливается, если встречает число 237.

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '5', '99', '237', '75', '22']
#
#
# def even_numbers(my_list):
#     for number in my_list:
#         if float(number) % 2 == 0:
#             print(number)
#         elif float(number) == 237:
#             return
#
#
# even_numbers(the_list)

# 5. Напишите программу, которая принимает два списка и
# выводит все элементы первого, которых нет во втором.

# list1 = ['1', '22', '9', '25.55', '99', '-3', '66', '245.01', '0']
# list2 = ['-327', '9', '5', '99', '237', '75', '22']
# is_chek = True
#
# for value1 in list1:
#     for index, value2 in enumerate(list2):
#         if value1 == value2:
#             is_chek = True
#             break
#         else:
#             is_chek = False
#     if is_chek is False:
#         print(value1, end=" ")


# 6. Сложите цифры целого числа.

#
# my_str = input("Enter some number: ")
#
#
# def sum_of_digits(number):
#     sum_is = 0
#     for digit in my_str:
#         sum_is += int(digit)
#     print(f"Sum of digits is: {sum_is}")
#
#
# sum_of_digits(my_str)


# 7. Посчитайте, сколько раз символ встречается в строке.

# digit_string = "1,4,9,25.55,89,-3,245.01,0,-327,99,5,99,75"
# my_str = input("Enter some one digit: ")
#
#
# def digit_symbol_count(symbol):
#     return digit_string.count(symbol, 0, len(digit_string))
#
#
# print(digit_symbol_count(my_str))


# 8. Реверс списка

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '5', '99', '237', '75', '22']
# the_list.reverse()
# print(the_list)

# 9. Функция очереди(написать функцию которая принимает список и
#  добавляет в него элементы как в очередь)

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '5', '99', '237', '75', '22']
# el = input("Enter some element: ")
#
#
# def add_element(add_el):
#     right_part = the_list[0:-1]
#     the_list.clear()
#     the_list.append(el)
#     the_list.extend(right_part)
#     return the_list
#
#
# print(add_element(el))


# 10. Наибольший общий делитель

# val1 = int(input("val1: "))
# val2 = int(input("val2: "))
#
#
# def nod_is(x, y):
#     for val in range(y):
#         if val != 0 and y % val == 0 and x % val == 0:
#             nod_max = val
#     print(f'NOD is {nod_max}')
#
#
# nod_is(val1, val2)


# 11. Циклический сдвиг

# the_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# modify_list = []
# step = int(input("Enter step of the cycle (int value from - 9 to 9): ")) * (-1)
#
#
# def cycle_step_modify(my_step):
#     print(the_list)
#     if my_step > 0:
#
#         part1 = the_list[step:]
#         part2 = the_list[:step]
#         modify_list.extend(part1)
#         modify_list.extend(part2)
#         return modify_list
#
#     elif my_step < 0:
#
#         part1 = the_list[step:]
#         part2 = the_list[:step]
#         modify_list.extend(part1)
#         modify_list.extend(part2)
#         return modify_list
#
#
# cycle_step_modify(step)
# print(modify_list)

# # 12. Проверить, есть ли в поседовательности дубликаты

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '5', '99', '237', '75', '22']
# duplicate = 0
# for val1 in the_list:
#     for val2 in the_list:
#         if val1 == val2:
#             duplicate += 1
#     if duplicate > 1:
#         print(f"Duplicate:{val1}")
#     duplicate = 0


# 13. Дан список некоторых целых чисел, найдите значение 20 в нем и,
#  если оно присутствует, замените его на 200. Обновите список только
#  при первом вхождении числа 20.

# the_list = ['1', '4', '9', '25.55', '89', '-3', '66', '245.01', '0', '-327', '99', '20', '99', '237', '75', '22']
# print(f"Start list {the_list}")
# for index, value in enumerate(the_list):
#     if value == "20":
#         the_list[index] = "200"
#
# print(f'New list {the_list}')


# 14.  Необходимо удалить пустые строки из списка строк.
# the_list = ['1', ' ', '4', '9', '25.55', '89', '-3', ' ', '66', '245.01', '0', '-327', '99', ' ', '5', '99', '237', '75', '22']
# print(f"Start list {the_list}")
# for index, value in enumerate(the_list):
#     if value == " ":
#         the_list.pop(index)
#
# print(f'New list {the_list}')