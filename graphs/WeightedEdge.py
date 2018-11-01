from graphs.Edge import Edge


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        super().__init__(src, dest)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name() + '(' + str(self.get_weight()) + ')'
