import random
import pylab


class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0

    def spin(self):
        self.ball = random.choice(self.pockets)

    def is_black(self):
        if type(self.ball) != int:
            return False

        if (0 < self.ball <= 10) or (18 < self.ball <= 28):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def is_red(self):
        return type(self.ball) == int and not self.is_black()

    def bet_black(self, amt):
        if self.is_black():
            return amt * self.blackOdds
        else:
            return -amt

    def bet_red(self, amt):
        if self.is_red():
            return amt * self.redOdds
        else:
            return -amt * self.redOdds

    def bet_pocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append(0)

    def __str__(self):
        return 'Europe Roulette'


class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def play_roulette(game, num_spins, to_print=True):
    lucky_number = '12'
    bet = 1
    tot_black, tot_red, tot_pocket = 0.0, 0.0, 0.0

    for i in range(num_spins):
        game.spin()
        tot_red += game.bet_red(bet)
        tot_black += game.bet_black(bet)
        tot_pocket += game.bet_pocket(lucky_number, bet)

    if to_print:
        print(num_spins, 'spins of', game)
        print('Expected return betting red =', str(100 * tot_red / num_spins) + '%')
        print('Expected return betting black =', str(100 * tot_black / num_spins) + '%')
        print('Expected return betting ', lucky_number, ' =', str(100 * tot_pocket / num_spins) + '%\n')

    return tot_red / num_spins, tot_black / num_spins, tot_pocket / num_spins


def find_pocket_return(game, num_trials, trial_size, to_print=True):
    pocket_returns = []
    for t in range(num_trials):
        trial_vals = play_roulette(game, trial_size, to_print)
        pocket_returns.append(trial_vals[2])

    return pocket_returns


# Standard Deviation & Mean of array of numbers
def get_mean_and_std(x):
    mean = sum(x) / float(len(x))
    tot = 0.0
    for i in x:
        tot += (i - mean) ** 2

    std = (tot / len(x)) ** 0.5
    return mean, std


def empirical_rule(games, num_trials):
    result_dict = None
    for g in games:
        result_dict[g.__str__] = []
    for num_spins in (100, 1000, 10000):
        print('\nSimulate betting a pocket for', num_trials, 'trials of', num_spins, 'spins each')

        for g in games:
            pocket_returns = find_pocket_return(g(), num_trials, num_spins, False)
            mean, std = get_mean_and_std(pocket_returns)
            result_dict[g.__str__].append((num_spins, 100 * mean, 100 * std))
            print('Exp. return for', g(), '=', str(round(100 * mean, 3)), '% +/- ', str(round(100 * 1.96 * std, 3)),
                  '% with 95% confidence')


def coefficient_of_variation(x):
    mean, std = get_mean_and_std(x)
    return std / mean


# Стандартное отклонение массива строк / standard deviation
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    summ = 0
    for i in L:
        summ += len(i)

    mean = summ / float(len(L))
    tot = 0.0
    for i in L:
        tot += (len(i) - mean) ** 2

    std = (tot / len(L)) ** 0.5
    return std


random.seed(0)
# num_trials = 20
# result_dict = {}
# games = (FairRoulette, EuRoulette, AmRoulette)
# for g in games:
#     result_dict[g.__str__] = []
# for num_spins in (100, 1000, 10000, 100000):
#     print('\nSimulate betting a pocket for', num_trials, 'trials of', num_spins, 'spins each')
#     for g in games:
#         pocket_returns = find_pocket_return(g(), num_trials, num_spins, False)
#         print('Exp. return for', g(), '=', str(100 * sum(pocket_returns) / float(len(pocket_returns))), '%')


# empirical_rule(games, num_trials)
# print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
# print(coefficient_of_variation([10, 4, 12, 15, 20, 5]))


num_trials = 50000
num_spins = 200
game = FairRoulette()

means = []
for i in range(num_trials):
    means.append(find_pocket_return(game, 1, num_spins, False)[0] / num_spins)

pylab.hist(means, bins=19, weights=pylab.array(len(means)*[1])/len(means))
pylab.xlabel('Mean return')
pylab.ylabel('Probability')
pylab.title('Expected return betting a pocket')
