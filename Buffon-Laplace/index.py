import random
import numpy


def throw_needels(num_needles):
    in_circle = 0
    for needles in range(1, num_needles + 1, 1):
        x = random.random()
        y = random.random()

        if (x * x + y * y) ** 0.5 <= 1.0:
            in_circle += 1

    return 4 * (in_circle / float(num_needles))


def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needels(num_needles)
        estimates.append(pi_guess)

    sdev = numpy.std(estimates)
    cur_est = sum(estimates) / len(estimates)
    print('Est. =', str(cur_est), ', Std. dev. =', str(round(sdev, 6)), 'Needles =', num_needles)

    return cur_est, sdev


def est_pi(precision, num_trials):
    cur_est = 0.0
    num_needles = 1000
    sdev = precision
    while sdev >= precision / 1.96:
        cur_est, sdev = get_est(num_needles, num_trials)
        num_needles *= 2
    return cur_est


def drawing_balls():
    bucket = ['r', 'r', 'r', 'g', 'g', 'g']
    for i in range(3):
        bucket.pop(random.randint(0, len(bucket) - 1))

    if bucket[0] == bucket[1] == bucket[2]:
        return 1
    else:
        return 0


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """
    estimates = []
    for i in range(numTrials):
        estimates.append(drawing_balls())

    return sum(estimates) / len(estimates)


# random.seed(0)
# est_pi(0.005, 100)
# print(noReplacementSimulation(100000))


import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    power_set = []
    for i in itertools.product([1, 0], repeat=len(choices)):
        power_set.append(np.array(i))

    filter_set_eq = []
    filter_set_less = []
    for j in power_set:
        # print(sum(j * choices))
        if sum(j * choices) == total:
            filter_set_eq.append(j)
        elif sum(j * choices) < total:
            filter_set_less.append(j)

    if len(filter_set_eq) > 0:
        minidx = min(enumerate(filter_set_eq), key=lambda x: sum(x[1]))[1]
        return minidx
    else:
        minidx = max(enumerate(filter_set_less), key=lambda x: sum(x[1]))[1]

    return minidx


def find_combination2(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    r, result = [], []
    for i in range(len(choices)):
        r.append(0)

    r = np.array(r)
    for i in range(len(choices)):
        temp = r.copy()
        temp[i] = 1

        for i2 in range(len(choices) - i):
            if sum(temp * choices) != total:
                temp[i2+i] = 1
            else:
                if sum(temp) < sum(result) or sum(result) == 0:
                    result = temp

    return result


# print(find_combination([1, 2, 2, 3], 4))
print(find_combination2([1, 2, 2, 3], 4))
