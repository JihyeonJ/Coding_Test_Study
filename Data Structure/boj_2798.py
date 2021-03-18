N, M = map(int, input().split())
arr = list(map(int, input().split()))
t = sum(arr)
m = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            s = arr[i] + arr[j] + arr[k]    # 세 숫자의 합 
            if s <= M and m <= s:
                m = s
print(m)