from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY, Point
from utils.constants import PRIME_NUMBER_3_DIGITS


def main():
    """
    Lập bảng cửu chương của đường cong elliptic với cặp (a, b) bất kỳ sao cho
    đường cong có cấp nguyên tố, với p nguyên tố có 3 chữ số
    """
    with open('times_table.txt', 'w') as times_table:
        for p in PRIME_NUMBER_3_DIGITS:
            times_table.write(f'p = {p}\n')
            for a in range(0, 26):
                for b in range(0, 26):
                    curve = EllipticCurve(a, b, p)
                    points_count = curve.count_points()
                    if curve.is_prime_points_count():
                        times_table.write(
                            f'(a, b) = ({a}, {b}), số điểm: {points_count}\n')
                        """
                        Nhóm đường cong elliptic có cấp nguyên tố thì mọi điểm
                        thuộc nó đều là điểm sinh
                        """
                        generator_point = curve.get_points()[points_count // 2]
                            
                        times_table.write(
                            curve.get_times_table(generator_point) + '\n')
                        break
                else:
                    continue
                break

    times_table.close()


if __name__ == '__main__':
    main()
