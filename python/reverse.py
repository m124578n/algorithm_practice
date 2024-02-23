

def reverse_func(target: list) -> list:
    target.sort()
    pre = 0
    last = -1
    for _ in range(len(target)//2):
        target[pre], target[last] = target[last], target[pre]
        pre += 1
        last -= 1
    return target


if __name__ == '__main__':
    target = [0, 1, 2, 3, 4, 5, 88, -50, 9, 100, 64, 20, 37, 77, 16, 38, 54]
    ans = reverse_func(target)
    print(ans)