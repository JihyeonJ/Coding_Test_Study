N = int(input())
arr = []
cnt = 0

for i in range(N):
    arr.append(int(input()))

for i in range(N-1, 0, -1):
    if arr[i] <= arr[i-1]:
        cnt += arr[i-1] - arr[i] + 1 
        arr[i - 1] = arr[i] - 1

print(cnt)