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
                return value

    def level(self):
        if self.exp > 1000:
            print('Your lvl:', 100)
        else:
            my_lvl = math.floor(self.exp / 100)
        return 'Your lvl:', my_lvl

    def experience(self):
        return 'Your experience:', self.exp

    def training(self, training, exp, lvl):
        if lvl - math.floor(self.exp / 100) > 3:
            return "Not strong enough"
        else:
            self.exp += exp
            achiv.append(training)
            return training

    def achivment(self):
        return achiv

    def battle(self, enemy_lvl):
        if enemy_lvl > 100 or enemy_lvl < 1:
            return 'Invalid lvl'
        else:
            if enemy_lvl == math.floor(self.exp / 100) or \
                    math.floor(self.exp / 100) - enemy_lvl == 1:
                self.exp += int(20 * pow(1 / 2, math.floor(self.exp / 100) - enemy_lvl + 1))
                return "A good fight"
            if math.floor(self.exp / 100) - enemy_lvl > 1:
                return 'Easy fight'
            if 5 > enemy_lvl - math.floor(self.exp / 100) > 1:
                return "An intense fight"
                self.exp += int(20 * math.pow((enemy_lvl - math.floor(self.exp / 100)), 2))
            else:
                return 'You have been defeated'
