import random
import pylab


def get_mean_and_std(x):
    mean = sum(x) / float(len(x))
    tot = 0.0
    for i in x:
        tot += (i - mean) ** 2

    std = (tot / len(x)) ** 0.5
    return mean, std


def plot_means(num_dice, num_rolls, num_bins, legend, color, style):
    means = []
    for i in range(num_rolls // num_dice):
        vals = 0
        for j in range(num_dice):
            vals += 5 * random.random()
        means.append(vals / float(num_dice))

    pylab.hist(means, num_bins, color=color, label=legend, weights=pylab.array(len(means)*[1])/len(means), hatch=style)
    return get_mean_and_std(means)


mean, std = plot_means(1, 1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean), ',', 'Std =', std)
mean, std = plot_means(50, 1000000, 19, 'Mean of 50 die', 'r', '//')
print('Mean of rolling 50 die =', str(mean), ',', 'Std =', std)
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
