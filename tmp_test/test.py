import datetime
"""
    To show getter and setter,
    use some 'magic' methods
"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        result = self.present_year() - self.__age
        print(result)
        return 'You are was born in: ' + str(result)

    @staticmethod
    def present_year():
        p_year = int(datetime.date.today().year)
        return p_year

    @property
    def my_name(self):
        return self.__name

    @my_name.setter
    def my_name(self, val):
        if (val is None) or (str(val).strip() == ""):
            print('Error, value "name" is empty')
        else:
            self.__name = val
            print(f"Okay, {self.__name}, lets set your age:")

    @property
    def my_age(self):
        return self.__age

    @my_age.setter
    def my_age(self, val):

        try:
            if int(val) in range(0, 121):
                self.__age = int(val)

            else:
                print("Error, non correct value, age must be from 0 to 120")
        except ValueError:
            print("Error, non correct value, age value must be integer")


pers = Person(False, False)

while True:

    pers.my_name = input("Name is >> ")
    if (pers.my_name is False) or (str(pers.my_name).strip() == ""):
        print("Try not empty value")
    else:
        break


while True:

    pers.my_age = input("Age is >> ")
    try:
        if 0 < int(pers.my_age) < 121:
            break
        else:
            print('Try correct value in diapason 0 - 120.')
    except ValueError:
        print('Try again.')

print(str(pers))






