import math


RANK = {
    '1': 'Pushover', '2': 'Novice', '3': 'Fighter', '4': 'Warrior',
    '5': 'Veteran', '6': 'Sage', '7': 'Elite', '8':
    'Conqueror', '9': 'Champion', '10': 'Greatest'
}
achiv = []


class Character:

    def __init__(self, lvl=1, exp=100):
        self.exp = exp

    def rank(self):
        for key, value in RANK.items():
            if int(key) == math.floor(self.exp / 100):
                print(value)

    def level(self):
        if self.exp > 1000:
            print('Your lvl:', 100)
        else:
            my_lvl = math.floor(self.exp / 100)
        print('Your lvl:', my_lvl)

    def experience(self):
        print('Your experience:', self.exp)

    def training(self, training, exp, lvl):
        if lvl - math.floor(self.exp / 100) > 3:
            print("Not strong enough")
        else:
            self.exp += exp
            achiv.append(training)
            print(training)

    def achivment(self):
        print(achiv)

    def battle(self, enemy_lvl):
        if enemy_lvl > 100 or enemy_lvl < 1:
            print('Invalid lvl')
        else:
            if enemy_lvl == math.floor(self.exp / 100) or \
                    math.floor(self.exp / 100) - enemy_lvl == 1:
                self.exp += int(20 * pow(1 / 2, math.floor(self.exp / 100) - enemy_lvl + 1))
                print("A good fight")
            if math.floor(self.exp / 100) - enemy_lvl > 1:
                print('Easy fight')
            if 5 > enemy_lvl - math.floor(self.exp / 100) > 1:
                print("An intense fight")
                self.exp += int(20 * math.pow((enemy_lvl - math.floor(self.exp / 100)), 2))
            else:
                print('You have been defeated')
