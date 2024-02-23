

def merge(target1: list, target2: list) -> list:
    target1.sort()
    target2.sort(reverse=True)
    temp = target1 + target2
    left = 0
    right = len(temp) - 1
    ans = []
    while left != right:
        if temp[left] < temp[right]:
            ans.append(temp[left])
            left += 1
        else:
            ans.append(temp[right])
            right -= 1
    return ans



if __name__ == '__main__':
    target1 = [1, 5, 11]
    target2 = [2, 4, 9, 12]
    ans = merge(target1, target2)
    print(ans)