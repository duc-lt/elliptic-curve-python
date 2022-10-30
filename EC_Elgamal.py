import codecs
from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY, Point
from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS
from utils.mod_operations import is_square, square_root

def convert_message_to_number(message, cur: EllipticCurve):
    padding = 0
    number_message = 0
    while(True):
        p_message = str(padding) + message if padding else message
        encode_message = p_message.encode()
        number_message = int(encode_message.hex(), 16)
        x_part = number_message ** 3 + cur.get_a() * number_message + cur.get_b()
        if is_square(x_part, cur.get_p()):
            break
        padding += 1
    print(number_message)
    return number_message

def map_message_to_point(message, cur: EllipticCurve):
    x = convert_message_to_number(message, cur)
    x_part = x ** 3 + cur.get_a() * x + cur.get_b()
    y = square_root(x_part, cur.get_p())

    return Point(x, y)

def generate_key(message, cur: EllipticCurve):
    x = randrange(1,cur.count_points())
    p = map_message_to_point(message, cur)
    y = cur.multiply(p, x)

    return p, y, x

def generate_cyphertext(message, cur: EllipticCurve):
    k = randrange(1,cur.count_points())
    p, y, x = generate_key(message, cur)

    c1 = cur.multiply(p, k)
    c2 = cur.multiply(y, k)

    return c1, cur.add(c2,p), x

def decrypt_message(cur: EllipticCurve, cypertext):
    c1, d, x = cypertext

    c2 = cur.multiply(c1, x)

    y = 0
    if c2.get_y():
        y = - c2.get_y() % cur.get_p()

    c = Point(c2.get_x(), y)

    p = cur.add(d,c)
    encode_message = hex(p.get_x())[2:]

    return bytearray.fromhex(encode_message).decode()

cur = EllipticCurve(1,6,73)
message = "A"

result = decrypt_message(cur,generate_cyphertext(message, cur))
print(result)

