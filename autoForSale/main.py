class Automobile:
    def __init__(self, n=None, b=None, f=None, c=None, lt=False):
        self.name_of_brand = n
        self.body_type = b
        self.fuel_type = f
        self.color = c
        self.load_tank = lt

    # Check is full or empty fuel tank:
    #                is True - you go away from car showroom wit new car
    #                is False - you should go to charge your tank

    def run_away(self):
        if self.load_tank is True:
            print("Congratulations, you are buy a car and went to your pretty trip!")
            return
        else:
            print("Your cars tank is empty, recharge pleas!")

    # Select fuel what you need and recharge your tank
    def recharge_tank(self, fuel):
        while True:
            print("\n\tSelect type of your fuel")
            print("1\tDiesel\n2\tGasoline\n3\tGas")
            select_fuel = input(">>")
            if select_fuel == "1":
                select_fuel = 'Diesel  '
            elif select_fuel == "2":
                select_fuel = 'Gasoline'
            elif select_fuel == "3":
                select_fuel = 'Gas     '
            if select_fuel == fuel:
                self.load_tank = True
                self.run_away()
                return
            else:
                print("Sorry, wrong type of fuel")


class CarForSale(Automobile):

    # Show all cars and select one of them to buy
    def show_all_car(self):
        print("          Model      body type   fuel type   color    full  price")
        self.write_line("-")
        for index, my_car in enumerate(self.car_list):
            print(index + 1, my_car, self.price_list[index])
        select_car = int(input(">>")) - 1

        if self.car_list[select_car][4] is True:
            print(f"Congratulations, you ar buy a car {self.car_list[select_car][0]} and went to your pretty trip!")
            self.car_list.pop(select_car)
            return
        else:
            print(f"Your cars {self.car_list[select_car][0]}tank is empty, recharge pleas!")

            self.recharge_tank(self.car_list[select_car][2])
            self.car_list.pop(select_car)

    # list of car (with all params) and price list
    price_list = [17000, 15000, 11000, 2100]
    car_list = [
        ['Peugeot Expert ', 'Van   ', 'Diesel  ', 'white ', True],
        ['Peugeot Partner', 'PickUp', 'Diesel  ', 'blue  ', False],
        ['Daewoo Lanos   ', 'Sedan ', 'Gas     ', 'gold  ', False],
        ['Vaz 2106       ', 'Sedan ', 'Gasoline', 'coffee', False]]

    # Static method drawing line from symbol
    @staticmethod
    def write_line(symbol):
        print(symbol * 40)


# Created class example car and beginning start main menu
car = CarForSale()
while len(car.car_list) != 0:
    car.write_line('*')
    print("\tWelcome to our car showroom")
    car.write_line('*')
    car.write_line('-')
    print('\t1\tShow our car for sale')
    print('\t0\tExit')
    car.write_line('-')
    select = input(">>")
    if select == "1":
        car.show_all_car()
    elif select == "0":
        exit(0)

print('Our car showroom is closed, we have not cars.')
exit('Warning: no more cars!')
