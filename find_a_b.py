from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY

from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS

prime_elliptic_curve = {}
p = 11
number_of_point = 13

for a in range(0,100):
    for b in range(0,100):
        curve = EllipticCurve(a,b,p)
        if curve.count_points() != number_of_point:
            continue
        if curve.is_prime_points_count():
            if str(curve.count_points()) not in prime_elliptic_curve:
                prime_elliptic_curve[str(curve.count_points())] = [(a,b)]
            else:
                prime_elliptic_curve[str(curve.count_points())].append((a,b))

print(prime_elliptic_curve)


