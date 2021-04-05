import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))


def binarysearch(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    temp = 0
    for i in arr:
        if i - target > 0:
            temp += (i - target)

    if temp < target:
        return binarysearch(arr, target, start, mid - 1)
    elif temp == target:
        return mid
    else:
        return binarysearch(arr, target, mid + 1, end)


result = binarysearch(arr, M, 0, N-1)
print(result + 1)
