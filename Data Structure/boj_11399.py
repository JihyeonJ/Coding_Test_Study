N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 12334
sum = 0
for i in range(0, N):
    for j in range(i+1):
        sum += arr[j]
print(sum)