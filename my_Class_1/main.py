# Jesus wears balaclava, [03.02.21 21:08]
# 0. Создайте Автомобиль, который может ехать.
# Ехать он может когда у него заполнен бак(переменная)
# Пользователь может заправить автомобиль, вызвав соответствующий метод,
# Поездка в зависимости от расстояния тратит топливо.
# 1к10(км)
#
# 1. Создать рабочего. У который может ходить на работу.
# Рабочий должен иметь возраст и имя.
# Так же принимать решение идти на работу или нет, в зависимости от того,
# какой ему передали номер дня

# class Employee:
#     age = None
#     name = None
#     present_day = None
#
#     def day_is(self):
#         self.present_day = int(input("What is the day today?:"))
#
#     def age_is(self):
#         self.age = int(input("How old are you?:"))
#
#     def name_is(self):
#         self.name = input("What is you name?: ")
#
#     def go_work(self, day, how_old):
#         if how_old > 60:
#             print("Relax, you are too much old, you are pensioner!")
#             return
#         elif how_old < 16:
#             print("Relax, you are too much young, you are child!")
#
#         else:
#             if day > 5:
#                 print("Relax, you are have week end today. Stay home.")
#             else:
#                 print(f"I em so sorry, {self.name}, you must go work today")
#
#
# some_worker = Employee()
# some_worker.name_is()
# some_worker.age_is()
# some_worker.day_is()
# some_worker.go_work(some_worker.present_day, some_worker.age)


        # random.randint()
# 2. Создать класс "воин". Здоровье в 100 очков. В случайном порядке они
# бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал,
# и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о
# том, кто одержал победу.
#
# 3. Есть Алфавит, характеристиками которого являются:
# - Язык
# - Список букв
#
# Для Алфавита можно:
# - Напечатать все буквы алфавита
# - Посчитать количество букв
#
# Jesus wears balaclava, [03.02.21 21:08]
# import random

# class Warrior:
#
#     health = 100
#     name = ''
#
#     def attack(self, opponent):
#         opponent.health = opponent.health - 20
#         print(f'{self.name} opponent: {opponent.health}')
#
#
# first_warrior = Warrior()
# first_warrior.name = 'Ivan'
#
# second_warrior = Warrior()
# second_warrior.name = 'Andy'
#
# game = [
#     first_warrior,
#     second_warrior
# ]
#
# while True:
#     war_idx = random.randint(0, 1)
#     opponent_idx = war_idx - 1
#
#     opponent = game[opponent_idx]
#     aggressor = game[war_idx]
#
#     aggressor.attack(opponent)
#     if opponent.health <= 0:
#         print(f'{aggressor.name} are winner')
#         break

# import random
#
# class Fighters:
#
#     player_name = None
#     damage = None
#     health_percent = 100
#     action_score = 20
#     kick_power_score = 0
#     block_power_score = 0
#     healing = 0
#
#     def battle(self, opponent):
#         pass
#
#     def kik_block(self, opponent):
#         pass
#
#     def healing_possibility(self, owner):
#         pass
#
#     def input_player_acton_params(self):
#         self.action_score = 20
#         print(f"You have {self.action_score} action scores")
#         self.kick_power_score = input("Enter power of  your kick:")
#         self.action_score -= self.kick_power_score
#         print(f"You have {self.action_score} action scores")
#         self.block_power_score = input("Enter power of  your block:")
#         self.action_score -= self.block_power_score
#
#         if self.action_score != 0:
#             self.healing = self.action_score * 3
#             print(f'Healing possibility is {self.healing} score')
#         else:
#             pass
#         return self.kick_power_score, self.block_power_score, self.healing
#
#     def input_computer_action_params(self):
#         self.action_score = 20
#         self.kick_power_score = random.randint(0,self.action_score)
#         self.action_score -= self.kick_power_score
#         self.block_power_score = random.randint(0,self.action_score)
#         self.action_score -= self.block_power_score
#         self.healing = self.action_score
#         return  self.kick_power_score, self.block_power_score, self.healing
#
#
# player = Fighters()
# computer = Fighters()
#
# print("Battle is begin!")
#
# while True:
#
