
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
    

class TwoDAc:
    def __init__(self, a) -> None:
        self.a = a
        self.init_tac()
        self.make_point()
        self.calculate()

    def init_tac(self):
        max_x = max([y[0] for x in self.a for y in x ])
        max_y = max([y[1] for x in self.a for y in x ])
        self.x = max_x
        self.y = max_y

        self.tac = []
        for y in range(max_y+1):
            temp = []
            for x in range(max_x+1):
                temp.append(0)
            self.tac.append(temp)

    def make_point(self):
        for x in self.a:
            # 0 是左上
            x1 = x[0][0]
            y1 = x[0][1]
            # 1 是右下
            x2 = x[1][0]
            y2 = x[1][1]
            
            self.tac[y1][x1] += 1
            self.tac[y2][x2] += 1
            self.tac[y2][x1] -= 1
            self.tac[y1][x2] -= 1

    def calculate(self):
        for y in range(1, self.y+1):
            for x in range(1, self.x+1):
                self.tac[y][x] += self.tac[y][x-1]
        
        for x in range(1, self.x+1):
            for y in range(1, self.y+1):
                self.tac[y][x] += self.tac[y-1][x]
            
    def show(self):
        show = []
        for y in self.tac:
            temp = []
            for x in y:
                if x >= 0:
                    z = " " + str(x)
                    temp.append(str(z))
                else:
                    temp.append(str(x))
            show.append(temp)
        for x in show:
            print(x)

    def __str__(self) -> str:
        return str(self.tac)


if __name__ == '__main__':
    a = [3, 5, 2, 8, 4, 1, 7]
    rs = RangeSum(a)
    rs.get_range_sum(2, 4)

    a = [[2, 6], [4, 10], [5, 9], [4, 7]]
    oac = OneDAc(a)
    print(oac)

    a = [[[1, 1], [5, 4]], [[3, 2], [7, 6]], [[3, 3], [6, 6]]]
    tac = TwoDAc(a)
    tac.show()


