import codecs
from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY, Point
from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS
from utils.mod_operations import is_square, square_root

a = 0
b = 0
p = 5915587277

text = "תזדיין עם אמא שלך"

list_text = list(text)
print(list_text)

encode_list = [ord(i) for i in list_text]
print(encode_list)

n = p
group_size = -1
while(n != 0):
    n = n // 65536
    group_size += 1

print(group_size)

group_list = [encode_list[x:x + group_size] for x in range(0, len(encode_list), group_size)]
print(group_list)



