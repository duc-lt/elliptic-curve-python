from core.elliptic_curve import EllipticCurve


def week_2():
    a, b, p = 2, 21, 101
    curve = EllipticCurve(a, b, p)
    with open('times_tables.txt', 'w') as f:
        print(curve.count_points())
        f.write(curve.get_times_tables())
    f.close()


week_2()
        
    

