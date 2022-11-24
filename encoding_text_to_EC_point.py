import codecs
from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY, Point
from utils.aks import is_prime
from utils.int_operations import miller_rabin_algorithm
from utils.mod_operations import is_square, square_root

def main():
    a = 1
    b = 6
    for p in range(99999, 3, -1):
        if miller_rabin_algorithm(p):
            if is_prime(p):
                EC = EllipticCurve(a,b,p)
                if EC.is_prime_points_count():
                    print(EC.to_string())

if __name__ == "__main__":
    main()
        

# text = "תזדיין עם אמא שלך"

# list_text = list(text)
# print(list_text)

# encode_list = [ord(i) for i in list_text]
# print(encode_list)

# n = p
# group_size = -1
# while(n != 0):
#     n = n // 65536
#     group_size += 1

# print(group_size)

# group_list = [encode_list[x:x + group_size] for x in range(0, len(encode_list), group_size)]
# print(group_list)


# k = randrange(1,EC.count_points())