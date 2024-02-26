
class RangeSum:
    def __init__(self, a) -> None:
        self.a = a
        self.init_ac()

    def init_ac(self):
        self.ac = [0]
        for x in self.a:
            self.ac.append(self.ac[-1]+x)
    
    def get_range_sum(self, l, r):
        print(self.ac[r] - self.ac[l-1])


class OneDAc:
    def __init__(self, a) -> None:
        self.a = a
        self.init_oac()
    
    def init_oac(self):
        max_n = max([x[1] for x in self.a])
        self.oac = [0] * (max_n + 1)
        for x in self.a:
            self.oac[x[0]] += 1
            self.oac[x[1]] -= 1
        
        for i, v in enumerate(self.oac):
            if i != 0:
                self.oac[i] = self.oac[i-1] + v

    def __str__(self) -> str:
        return str(self.oac)

if __name__ == '__main__':
    a = [3, 5, 2, 8, 4, 1, 7]
    rs = RangeSum(a)
    rs.get_range_sum(2, 4)

    a = [[2, 6], [4, 10], [5, 9], [4, 7]]
    oac = OneDAc(a)
    print(oac)


