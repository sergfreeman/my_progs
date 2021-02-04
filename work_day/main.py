# Создать рабочего. У который может ходить на работу.
# Рабочий должен иметь возраст и имя.
# Так же принимать решение идти на работу или нет, в зависимости от того,
# какой ему передали номер дня

class Employee:
    age = None
    name = None
    present_day = None

    def day_is(self):
        self.present_day = int(input("What is the day today?:"))

    def age_is(self):
        self.age = int(input("How old are you?:"))

    def name_is(self):
        self.name = input("What is you name?: ")

    def go_work(self, day, how_old):
        if how_old > 60:
            print("Relax, you are too much old, you are pensioner!")
            return
        elif how_old < 16:
            print("Relax, you are too much young, you are child!")

        else:
            if day > 5:
                print("Relax, you are have week end today. Stay home.")
            else:
                print(f"I am so sorry, {self.name}, you must go work today")


some_worker = Employee()
some_worker.name_is()
some_worker.age_is()
some_worker.day_is()
some_worker.go_work(some_worker.present_day, some_worker.age)