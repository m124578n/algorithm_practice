

def swap(a, b):
    '''in python we can just a, b = b, a'''
    return b, a


def sorting_by_swap(target: list) -> list:
    n = len(target)
    is_sorting = False
    while not is_sorting:
        for x in range(0, n-1):
            if target[x] > target[x+1]:
                target[x], target[x+1] = target[x+1], target[x]
        is_sorting = check_is_sorting(target)
    return target


def check_is_sorting(target: list) -> bool:
    n = len(target)
    for x in range(0, n-1):
        if target[x] > target[x+1]:
            return False
    return True


def bubble_sort(target: list) -> list:
    n = len(target)
    while n > 1:
        for x in range(0, n-1):
            if target[x] > target[x+1]:
                target[x], target[x+1] = target[x+1], target[x]
        n -= 1
    return target


if __name__ == '__main__':
    target = [5, 2, 0, 4, 9, 8, 7, 100, -5]
    ans = bubble_sort(target)
    print(ans)