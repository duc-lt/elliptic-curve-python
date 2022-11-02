from random import choice
from core.elliptic_curve import EllipticCurve
from utils.constants import PRIME_NUMBER_4_DIGITS


def main():
    """
    Liệt kê 20 cặp (a, b) với 0 < a <= 100 và 0 < b <= 100 sao cho đường cong
    elliptic có số điểm nguyên tố, với p nguyên tố có 4 chữ số bất kỳ
    """
    p = choice(PRIME_NUMBER_4_DIGITS)
    print(f'p = {p}')
    curves = []
    count = 0
    for a in range(1, 101):
        for b in range(1, 101):
            curve = EllipticCurve(a, b, p)
            points_count = curve.count_points()
            if curve.is_prime_points_count():
                count += 1
                curves.append((p, (a, b), points_count))
                print(f'{count}. (a, b) = ({a}, {b}), số điểm: {points_count}')
                if count == 20:
                    print(f'count: {count}')
                    break
        else:
            continue
        break


    print(curve[0])


if __name__ == '__main__':
    main()