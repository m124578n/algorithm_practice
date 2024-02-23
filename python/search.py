
def linear_search(target: list, key: int) -> int:
    for i, v in enumerate(target):
        if v == key:
            return i
    return -1


def binary_search(target: list, key: int) -> int:
    target.sort()
    n = len(target)
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if target[mid] == key:
            return mid
        elif target[mid] < key:
            left = mid + 1
        else:
            right = mid
    return -1


if __name__ == '__main__':
    target = [0, 1, 2, 3, 4, 5, 88, -50, 9]
    key = 5
    ans = linear_search(target, key)
    print(ans)

    target = [0, 1, 2, 3, 4, 5, 88, -50, 9, 100, 64, 20, 37, 77, 16, 38, 54]
    key = 5
    ans = binary_search(target, key)
    print(ans)