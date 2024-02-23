

def minimum(target: list) -> int | float:
    ans = target[0]
    for x in target:
        if x < ans:
            ans = x            
    return ans

def find_minimum_index(target: list) -> int | float:
    ans, idx = target[0], 0
    for i, v in enumerate(target):
        if v < ans:
            ans, idx = v, i
    return idx


if __name__ == '__main__':
    target = [1, 2, 3, 4, 5, 0, 99, 87, 55, -50, -35]
    ans = minimum(target)
    print(ans)
    ans = find_minimum_index(target)
    print(ans)
