"""
Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве.

"""
class Car:

    def haves_four_wheels(self):
        print(f'This car has four wheels')


class CrewCar(Car):
    def haves_passanger_box(self):
        print('This car has a crew')


class SportCar(CrewCar):
    def has_sports_pilot(self):
        print('This car has a sports pilot')


class CargoCar(Car):
    def has_cargo(self):
        print('This car has a cargo')


car = Car()
car.haves_four_wheels()
print('*' *50)

car = CargoCar()
car.has_cargo()
car.haves_four_wheels()
print('*' *50)

car = CrewCar()
car.haves_passanger_box()
car.haves_four_wheels()
print('*' *50)

car = SportCar()
car.haves_passanger_box()
car.has_sports_pilot()
car.haves_four_wheels()

