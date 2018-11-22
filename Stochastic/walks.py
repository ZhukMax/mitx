import pylab
import random


class StyleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        ox = other.x
        oy = other.y
        x_dist = self.x - ox
        y_dist = self.y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        self.drunks[drunk] = current_location.move(x_dist, y_dist)


class OddField(Field):
    def __init__(self, num_holes=1000, x_range=100, y_range=100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(num_holes):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            new_x = random.randint(-x_range, x_range)
            new_y = random.randint(-y_range, y_range)
            new_loc = Location(new_x, new_y)
            self.wormholes[(x, y)] = new_loc

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self.drunks[drunk].get_x()
        y = self.drunks[drunk].get_y()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):
    @staticmethod
    def take_step():
        step_choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):
    @staticmethod
    def take_step():
        step_choices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


def walk(f, d, num_steps):
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps, num_trials, d_class):
    homer = d_class('Homer')
    origin = Location(0, 0)
    distance = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distance.append(round(walk(f, homer, num_steps), 1))

    return distance


def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)


def trace_walk(field_kinds, num_steps):
    style_choice = StyleIterator(('b+', 'r^', 'ko'))
    for f_class in field_kinds:
        d = UsualDrunk('')
        f = f_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))

        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())

        cur_style = style_choice.next_style()
        pylab.plot(x_vals, y_vals, cur_style, label=f_class.__name__)
        pylab.title('Spots Visited on Walk (' + str(num_steps) + ' steps)')
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc='best')


def drunk_test(walk_lengths, num_trials, d_class):
    for num_steps in walk_lengths:
        distance = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'random walk of', num_steps, 'steps')
        print(' Mean =', round(sum(distance)/len(distance), 4))
        print(' Max =', max(distance), 'Min =', min(distance))


random.seed(0)
drunk_test((10, 100, 1000), 100, UsualDrunk)
sim_all((UsualDrunk, ColdDrunk), (10, 100, 1000), 100)
trace_walk((Field, OddField), 500)
