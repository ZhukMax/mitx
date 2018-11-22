import random


def gen_even():
    return random.randint(0, 49) * 2


def dist1():
    return random.random() * 2 - 1


def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1


def dist3():
    return int(random.random() * 10)


def dist4():
    return random.randrange(0, 10)


def dist5():
    return int(random.random() * 10)


def dist6():
    return random.randint(0, 10)


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def test_roll(n=10):
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(result)
