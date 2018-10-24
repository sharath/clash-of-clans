import math

def eucl_dist(clan1, clan2):
    return distance(clan1.x, clan1.y, clan2.x, clan2.y)


def intersecting_area(clan1, clan2):
    R, r = clan1.circle()[0], circle2.circle()[0]
    dist = eucl_dist(clan1, clan2)
    if dist >= R + r: # no overlap
        return 0
    if dist < abs(R - r): # one circle inside the other
        return math.pi * min(R, r)**2
    r2, R2, d2 = r ** 2, R ** 2, dist ** 2
    alpha = math.acos((d2 + r2 - R2) / (2 * dist * r))
    beta = math.acos((d2 + R2 - r2) / (2 * dist * R))
    return (r2 * alpha + R2 * beta -
            0.5 * (r2 * math.sin(2 * alpha) + R2 * math.sin(2 * beta))
            )


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** .5
