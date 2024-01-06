import random

# six_to_eighteen = random.randint(6,18)
# print(six_to_eighteen)

# members = ['Prince', 'King', 'Princess']
# leader = random.choice(members)
# print(leader)

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)

# print(f'({dice1}, {dice2})')

class Dice:
    def roll():
        dicerange = (1, 2, 3, 4, 5, 6)
        dice1 = random.choice(dicerange)
        dice2 = random.choice(dicerange)
        print(f'({dice1}, {dice2})')


solaDice = Dice
solaDice.roll()


