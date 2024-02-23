

def minimum(target: list) -> int | float:
    ans = target[0]
    for x in target:
        if x < ans:
            ans = x            
    return ans


if __name__ == '__main__':
    target = [1, 2, 3, 4, 5, 0, 99, 87, 55, -50, -35]
    ans = minimum(target)
    print(ans)
