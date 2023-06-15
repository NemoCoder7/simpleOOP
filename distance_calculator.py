import math as m


class DistanceCalcualtor:

    def __init__(self, t1, g1, t2, g2):
        self.t1 = t1
        self.g1 = g1
        self.t2 = t2
        self.g2 = g2


    def calculate_distance(self):
        return 6371.01 * m.acos(m.sin(self.t1) * m.sin(self.t2) + m.cos(self.t1) * m.cos(self.t2)) * m.cos(self.g1 - self.g2)

distance = DistanceCalcualtor(10, 12, 20, 12)
print(distance.calculate_distance())

