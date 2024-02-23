

def sieve_of_eratosthenes(num: int) -> None:
    prime = [True for i in range(num + 1)]

    p = 2
    while (p * p <= num):
        if prime[p] == True:
            # 刪除2 3 4 5 6 7 ... 倍數
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            print(p)



if __name__ == '__main__':
    sieve_of_eratosthenes(30)