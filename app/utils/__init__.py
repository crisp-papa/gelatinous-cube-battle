import random
def die_roll(minimum = 1, maximum = 2):
    random.seed()
    return random.randint(minimum, maximum)