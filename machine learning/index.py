import pylab


class Animal():
    def __init__(self, name, egg_laying, scales, poisonous, cold_blood, legs, reptile):
        self.name = name
        self.egg_laying = egg_laying
        self.scales = scales
        self.poisonous = poisonous
        self.legs = legs
        self.cold_blood = cold_blood
        self.reptile = reptile

    def get_name(self):
        return self.name

    def distance(self, another_animal):
        return 1

    def __str__(self):
        return self.name


animals = [Animal('cobra', 1, 1, 1, 1, 0, 1),
           Animal('rattlesnake', 1, 1, 1, 1, 0, 1),
           Animal('boa constrictor', 0, 1, 0, 1, 0, 1),
           Animal('chicken', 1, 1, 0, 1, 2, 0),
           Animal('guppy', 0, 1, 0, 0, 0, 0),
           Animal('dart frog', 1, 0, 1, 0, 4, 0),
           Animal('zebra', 0, 0, 0, 0, 4, 0),
           Animal('python', 1, 1, 0, 1, 0, 1),
           Animal('alligator', 1, 1, 0, 1, 4, 1)]


def distance_matrix(animals, precision):
    column_label = []
    for a in animals:
        column_label.append(a.get_name())
    row_label = column_label[:]
    table_vals = []

    # Get distance between pairs of animals
    for a1 in animals:
        row = []
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        table_vals.append(row)

    table = pylab.table(rowLabels=row_label,
                        colLabels=column_label,
                        cellText=table_vals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.138] * len(animals))
    # table.auto_set_front_size(False)
    # table.set_frontsize(10)
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distance')


distance_matrix(animals, 3)
