from core.elliptic_curve import EllipticCurve
from utils.aks import is_prime
from utils.int_operations import miller_rabin_algorithm

def main():
    a = 1
    b = 6
    p = 9929
    for p in range(9999, 3, -1):
        if miller_rabin_algorithm(p):
            print(p)
            if is_prime(p):
                EC = EllipticCurve(a,b,p)
                if EC.is_prime_points_count():
                    print(EC.to_string())
                    break

if __name__ == "__main__":
    main()
        
def encoding():
    text = "text"

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


    k = randrange(1,EC.count_points())

    nB = 2048

    G = Point(0,1)

    kG = EC.multiply(G, k)

    Pb = EC.multiply(G, nB)

    kPb = EC.multiply(Pb, nB)

    cypherText = []
    
    for Pm in group_list:
        cypherText.append(EC.add_with_Pm(Pm, kPb))

    Pc = [kG, cypherText]

    return Pc


def decoding(Pc):

    kG = Pc[0]

    cypherText = cypherText[1]

    nB = 2048

    nBkG = EC.multiply(kG, nB)

    y = 0
    if nBkG.get_y():
        y = - nBkG.get_y() % EC.get_p()

    minus_nBkG = Point(c.get_x(), y)

    group_list = []
    for cypher in cypherText:
        Pm = EC.add(cypher, minus_nBkG)
        group_list.append(Pm)
    
    for Pm in group_list:







