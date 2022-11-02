from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY
from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS
from utils.mod_operations import power


def main():
    a1, b1, p1 = 1, 6, 307 # 331 điểm
    curve1 = EllipticCurve(a1, b1, p1)
    curve1_points_count = curve1.count_points()
    p2 = 151
    """
    Tìm a2, b2, p2 sao cho 2 đường cong (a1, b1, p1) và (a2, b2, p2) có
    số điểm bằng nhau và nguyên tố
    """
    # global a2, b2
    # for a2 in range(1, 100):
    #     for b2 in range(1, 100):
    #         curve2 = EllipticCurve(a2, b2, p2)
    #         if curve2.count_points() == curve1_points_count:
    #             print(f'(a2, b2) = ({a2}, {b2})')
    #             break

    """
    Tìm các giá trị p sao cho tổng số điểm
    trên đường cong elliptic là số nguyên tó
    """
    prime_elliptic_curve = []
    prime_2_digits = list(filter(lambda x: 10 <= x <= 99, PRIME_NUMBERS_2_TO_4_DIGITS))
    prime_3_digits = list(filter(lambda x: 100 <= x <= 999, PRIME_NUMBERS_2_TO_4_DIGITS))
    start_time = time()
    # for p in PRIME_NUMBERS_2_TO_4_DIGITS:
    for p in prime_3_digits:
    # for p in prime_2_digits:
        curve = EllipticCurve(a1, b1, p)
        if curve.is_prime_points_count():
            prime_elliptic_curve.append(p)
            print(f'p = {p}, số điểm = {curve.count_points()}')
    print(f'Thời gian tính: {time() - start_time}')

    # rand_index = randrange(0, len(prime_elliptic_curve))
    # rand_p = prime_elliptic_curve[rand_index]
    # rand_curve = EllipticCurve(a, b, rand_p)
    """
    Bảng cửu chương của các điểm thuộc đường cong elliptic
    với p được chọn ngẫu nhiên trong mảng prime_elliptic_curve
    """
    # print(f'bảng cửu chương với p = {rand_p}')
    # global point
    # while True:
    #     point_index = randrange(0, rand_curve.count_points())
    #     point = rand_curve.get_points()[point_index]
    #     if not point.equals_to(POINT_AT_INFINITY):
    #         break
    # start_time = time()
    # print(rand_curve.get_times_table(point))
    # print(f'thời gian liệt kê bảng cửu chương: {time() - start_time}')


    """
    Tìm a, b với 0 <= a, b <= 100 để các đường cong elliptic y^2 = x^3 + ax + b (mod p)
    có cùng số điểm và số điểm là số nguyên tố, với p nguyên tố
    """
    # points_count = rand_curve.count_points()
    # print(f'Các cặp giá trị (a, b) sao cho đường cong y^2 = x^3 + ax + b (mod {rand_p}) có cùng số điểm:')
    # start_time_2 = time()
    # for a_i in range(1, 101):
    #     for b_i in range(1, 101):
    #         curve = EllipticCurve(a_i, b_i, rand_p)
    #         if curve.count_points() == points_count:
    #             print(f'({a_i}, {b_i})')
    # print(f'thời gian tìm các cặp (a, b): {time() - start_time_2}')


# if __name__ == '__main__':
#     main()