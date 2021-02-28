"""
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
после заданного года.
"""


class Employee:

    def set_val_str(self):
        val = input()
        return val

    def set_years(self):
        while True:

            try:
                year = int(input())
                if 2021 >= year >= 1900:
                    return year
                else:
                    print('Illegal value, must be from 1900 till 2021')
            except ValueError:
                print('Illegal value, must be type int')

    def __init__(self):
        print('Enter persons name:', end='')
        self.__name = self.set_val_str()
        print('Enter persons last name:', end='')
        self.__last_name = self.set_val_str()
        print('Enter persons work department:', end='')
        self.__department = self.set_val_str()
        print('Enter the start year:', end='')
        self.__year = self.set_years()

    def get_year(self):
        return self.__year

    def __repr__(self):
        return f"       Person info\n  " \
               f"        name:{self.__name}\n" \
               f"   last name:{self.__last_name}\n" \
               f"  department:{self.__department}\n" \
               f"  start year:{self.__year}\n"


employers_base_list = list()

print("Let's set 5 employee\n")
for index in range(5):
    print(f'Employee{index+1}')
    obj_name = 'employee' + str(index)
    obj_name = Employee()
    employers_base_list.append(obj_name)

print('Set year limit:', end='')
years_limit = Employee.set_years(0)

for _ in employers_base_list:
    if _.get_year() > years_limit:
        print(_)

