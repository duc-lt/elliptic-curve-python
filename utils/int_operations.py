from math import gcd


def is_prime(a):
    if a < 2 or any(a % i == 0 for i in range(2, a)):
        return False
    return True


def is_odd_prime(a):
    return is_prime(a) and a % 2 == 1


def is_coprime(a, b):
    return gcd(a, b) == 1


def to_base_2(a):
    # phân tích a về dạng a = q.2^s, với q lẻ
    q, s = a, 0
    while q % 2 == 0:
        q /= 2
        s += 1
    return q, s