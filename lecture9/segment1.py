import random

import numpy
import pylab


def make_hist(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)


def get_highs():
    in_file = open('lecture9/temperature.cvs')
    population = []
    for l in in_file:
        try:
            temp_c = float(l.split(',')[1])
            population.append(temp_c)
        except:
            continue
    return population


def loadFile():
    inFile = open('./julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return low, high


def get_means_and_stds(population, sample, verbose=False):
    pop_mean = sum(population) / len(population)
    sample_mean = sum(sample) / len(sample)
    if verbose:
        make_hist(population, 'Daily High 1961-2015, Population\n(mean =' + str(round(pop_mean, 2)) + ')',
                  'Degrees C', 'Number days')
        pylab.figure()
        make_hist(sample, 'Daily High 1961-2015, Sample\n(mean =' + str(round(sample_mean, 2)) + ')',
                  'Degrees C', 'Number days')
        print('Population mean =', pop_mean)
        print('Standard deviation of population =', numpy.std(population))
        print('Sample mean =', sample_mean)
        print('Standard deviation of sample =', numpy.std(sample))

    return pop_mean, sample_mean, numpy.std(population), numpy.std(sample)


def plot_dist():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    make_hist(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.figure()
    make_hist(normal, 'Gaussian', 'Value', 'Frequency')
    pylab.figure()
    make_hist(exp, 'Exponential', 'Value', 'Frequency')


# random.seed(0)
# population = get_highs()
# sample = random.sample(population, 100)
# get_means_and_stds(population, sample, True)
plot_dist()
