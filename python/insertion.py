
def insertion(target: list, key: int) -> list:
    for i, v in enumerate(target):
        if v >= key > target[i-1]:
            target = target[:i] + [key] + target[i:]
            return target


if __name__ == '__main__':
    target = [0, 1, 2, 3, 4, 5, 88, -50, 9, 100, 64, 20, 37, 77, 16, 38, 54]
    target.sort()
    print(target)
    key = 25
    ans = insertion(target, key)
    print(ans)