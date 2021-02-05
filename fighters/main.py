# Создать класс "воин". Здоровье в 100 очков. В случайном порядке они
# бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал,
# и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о
# том, кто одержал победу.


import random


class Fighters:

    health_percent = 100
    action_score = 30
    kick_power_score = 0
    block_power_score = 0
    lucky = 0

    def get_lucky(self):
        self.lucky = random.randint(1, 5)
        return self.lucky

    def input_player_acton_params(self):
        self.action_score = 20
        print(f"You have {self.action_score} action scores")
        self.kick_power_score = int(input("Enter power of your kick:"))
        self.block_power_score = self.action_score - self.kick_power_score
        print(f"You have {self.block_power_score} block scores")

        return self.kick_power_score, self.block_power_score

    def input_computer_action_params(self):
        self.action_score = 20
        self.kick_power_score = random.randint(0, self.action_score)
        self.block_power_score = self.action_score - self.kick_power_score
        return self.kick_power_score, self.block_power_score


player = Fighters()
computer = Fighters()

print('Remember, you may not only attacked, block opponents kicks too!')
print("\t\tBattle is begin!")

while True:
    # generate fighters params
    player.input_player_acton_params()
    computer.input_computer_action_params()

    computer.kick_power_score *= computer.get_lucky()
    player.block_power_score *= player.get_lucky()

    player.block_power_score *= player.get_lucky()
    computer.block_power_score *= computer.get_lucky() - 1

    # Calculate battle params for 'Player'
    if player.block_power_score < computer.kick_power_score:
        player.health_percent = player.health_percent - computer.kick_power_score + player.block_power_score
    else:
        pass

    # Calculate battle params for 'Computer'
    if computer.block_power_score < player.kick_power_score:
        computer.health_percent = computer.health_percent - player.kick_power_score + computer.block_power_score
    else:
        pass

# end of game or visualisation current values of health
    if player.health_percent <= 0:
        print("Computer there are winner, player - you are died!")
        break
    elif computer.health_percent <= 0:
        print("Player is winner, computer - to lose!")
        break
    else:
        pass
    print("-" * 30)
    print("  Player health:", "+" * (player.health_percent // 2), player.health_percent)
    print("Computer health:", "+" * (computer.health_percent // 2), computer.health_percent)
