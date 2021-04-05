N, x = map(int, input().split())
arr = list(map(int, input().split()))


def first(array, target, start, end):
    if (start > end):
        return None
    mid = (start + end) // 2
    if mid == 0 or array[mid] == target and target > array[mid - 1]:
        return mid
    elif array[mid] >= target:
        first(array, target, start, mid - 1)
    else:
        first(array, target, mid + 1, end)


def last(array, target, start, end):
    if (start > end):
        return None
    mid = (start + end) // 2
    if mid == N - 1 or array[mid] == target and target < array[mid - 1]:
        return mid
    elif array[mid] >= target:
        last(array, target, start, mid - 1)
    else:
        last(array, target, mid + 1, end)


a = first(arr, x, 0, N - 1)
b = last(arr, x, 0, N-1)
print(a, b)
