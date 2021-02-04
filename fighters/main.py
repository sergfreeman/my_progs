# Создать класс "воин". Здоровье в 100 очков. В случайном порядке они
# бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал,
# и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о
# том, кто одержал победу.


import random


class Fighters:
    player_name = None
    damage = None
    health_percent = 100
    action_score = 20
    kick_power_score = 0
    block_power_score = 0
    healing = 0
    lucky = 0

    def get_lucky(self):
        self.lucky *= random.randint(1, 3)
        return self.lucky

    def input_player_acton_params(self):
        self.action_score = 20
        print(f"You have {self.action_score} action scores")
        self.kick_power_score = int(input("Enter power of  your kick:"))
        self.action_score -= self.kick_power_score
        print(f"You have {self.action_score} action scores")
        self.block_power_score = int(input("Enter power of  your block:"))
        self.action_score -= self.block_power_score

        if self.action_score != 0:
            self.healing = self.action_score
            print(f'Healing possibility is {self.healing} score')
        else:
            pass
        return self.kick_power_score, self.block_power_score, self.healing

    def input_computer_action_params(self):
        self.action_score = 20
        self.kick_power_score = random.randint(0, self.action_score)
        self.action_score -= self.kick_power_score
        self.block_power_score = random.randint(0, self.action_score)
        self.action_score -= self.block_power_score
        self.healing = self.action_score
        return self.kick_power_score, self.block_power_score, self.healing


player = Fighters()
computer = Fighters()

print("Battle is begin!")

while True:
    player.input_player_acton_params()
    computer.input_computer_action_params()

    player.health_percent = player.health_percent - computer.kick_power_score + player.block_power_score \
                            + player.get_lucky()

    computer.health_percent = computer.health_percent - player.kick_power_score + computer.block_power_score \
                              + computer.get_lucky()

    if player.health_percent <= 0:
        print("Computer there are winner, player - you are died!")
        break
    elif computer.health_percent <= 0:
        print("Player is winner, computer - to lose!")
        break
    else:
        pass
    print("-" * 30)
    print("  Player health:", "+" * (player.health_percent//10))
    print("Computer health:", "+" * (computer.health_percent // 10))