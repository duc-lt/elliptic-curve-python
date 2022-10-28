from email import message
from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY, Point
from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS
from utils.mod_operations import is_square, square_root

def convert_message_to_number(message, cur: EllipticCurve):
    k = 0
    encode_message = message.encode()
    number_message = int(encode_message.hex(), 16)
    x_part = number_message ** 3 + cur.__a * number_message + cur.__b
    while(not is_square(x_part, cur.__p)):
        k += 1
        number_message += k
        x_part = number_message ** 3 + cur.__a * number_message + cur.__b
    
    return number_message, k

def map_message_to_point(message, cur: EllipticCurve):
    x, k = convert_message_to_number(message)
    x_part = x ** 3 + cur.__a * x + cur.__b
    y = square_root(x_part, cur.__p)

    return Point(x, y)

def generate_key(message, cur: EllipticCurve):
    k = randrange(1,cur.count_points())
    p = map_message_to_point(message, cur)
    c = cur.multiply(p)

    return k, p, c

def generate_cyphertext(message, cur: EllipticCurve):
    c1, p, c2 = generate_key(message, cur)
    
    return (c1, cur.add(c1,p))

