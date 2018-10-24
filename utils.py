import math

def intersecting_area(circle1, circle2):
    """
    Return the area that two circles intersect
    :param circle1: circle represented by (r, x, y)
    :param circle2: circle represented by (r, x, y)
    :return: area of intersection
    """
    R, r = circle1[0], circle2[0]
    dist = distance(circle1[1], circle1[2], circle2[1], circle2[2])
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
