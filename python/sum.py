
def sum_func(target: list) -> int | float:
    ans = 0
    for x in target:
        ans += x
    return ans


if __name__ == '__main__':
    target = [0, 1, 2, 3, 4, 5, 88, -50, 9]
    ans = sum_func(target)
    print(ans)
    