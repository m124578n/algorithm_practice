

def selection_sort(target: list) -> list:
    n = len(target)
    for i in range(n - 1):
        min_j = target.index(min(target[i:]))
        target[i], target[min_j] = target[min_j], target[i]
    return target


if __name__ == '__main__':
    target = [7, 9, 12, 2, 5, 4, 3]
    ans = selection_sort(target)
    print(ans)
