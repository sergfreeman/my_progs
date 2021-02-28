"""
Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
чисел и среднее арифметическое чисел из заданного диапазона.
"""
my_list = [3, 34, 27, 91, 18, 237, -2, 223, 14]

def slice_diapason(values_list):
    for action in ('two index', 'interval'):
        first_index = int(input('Enter first index: '))
        second_index = int(input('Enter second index: '))
        if action == 'two index':
            print(f'Arithmetic mean of two index {first_index} and {second_index} = '
                  f'{(my_list[first_index]+my_list[second_index])/2}')
        else:
            res = sum(my_list[first_index:second_index]) / len(my_list[first_index:second_index])
            print(f'Arithmetic mean of slice from {first_index} to {second_index}: {res}')

print(my_list)
slice_diapason(my_list)

