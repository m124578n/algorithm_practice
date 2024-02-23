

def partition(target: list) -> list:
    left = -1
    n = len(target) - 1
    for x in range(n):
        if target[x] < target[n]:
            left += 1
            target[left], target[x] = target[x], target[left]
    left += 1
    target[left], target[n] = target[n], target[left]
    return target


def quick_sort(target, left, right):
    if left >= right:
        return
    
    i = left
    j = right
    key = target[left]

    while i != j:
        while target[j] > key and i < j:
            j -= 1
        while target[i] <= key and i < j:
            i += 1
        if i < j:
            target[i], target[j] = target[j], target[i]
    
    target[left] = target[i]
    target[i] = key

    quick_sort(target, left, i - 1)
    quick_sort(target, i + 1, right)



if __name__ == '__main__':
    target = [1, 9, 12, 5, 4, 10, 6, 8]
    ans = partition(target)
    print(ans)

    target = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    quick_sort(target, 0, len(target) - 1)
    print(target)