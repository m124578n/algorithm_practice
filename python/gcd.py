

def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def gcd2(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


if __name__ == '__main__':
    a = 39
    b = 52
    ans = gcd(a, b)
    print(ans)
