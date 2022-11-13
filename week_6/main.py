from core.elliptic_curve import EllipticCurve
from utils.constants import PRIME_NUMBER_3_DIGITS


def main():
    """
    Liệt kê 20 cặp (a, b) với 0 < a <= 26 và 0 < b <= 26 sao cho đường cong
    elliptic có số điểm nguyên tố, với p nguyên tố có 3 chữ số
    """
    with open('prime_order.txt', 'w') as prime_order:
        for p in PRIME_NUMBER_3_DIGITS:
            prime_order.write(f'p = {p}\n')
            curves = []
            count = 0
            for a in range(1, 27):
                for b in range(1, 27):
                    curve = EllipticCurve(a, b, p)
                    points_count = curve.count_points()
                    if curve.is_prime_points_count():
                        count += 1
                        curves.append((p, (a, b), points_count))
                        # print(f'{count}. (a, b) = ({a}, {b}), số điểm: {points_count}')
                        prime_order.write(f'{count}. (a, b) = ({a}, {b}), số điểm: {points_count}\n')
                        if count == 20:
                            prime_order.write('\n')
                            break
                else:
                    continue
                break
    
    prime_order.close()


if __name__ == '__main__':
    main()