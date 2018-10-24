from utils import intersecting_area

class Clan:
    def __init__(self, x, y, p0):
        self.x = x
        self.y = y
        self.pop = p0


def discontent(clan):
    return clan.carrying() - clan.pop()


def conflict(clan1, clan2):
    return lambda_(clan1, clan2) * 1.0 / (discontent(clan1) * discontent(clan2))


def lambda_(clan1, clan2):
    return intersecting_area(clan1.circle(), clan2.circle())

