class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calories

    def density(self):
        return self.get_value()/self.get_cost()

    def __str__(self):
        return self.name + ': <' + str(self.value)\
               + ', ' + str(self.calories) + '>'
