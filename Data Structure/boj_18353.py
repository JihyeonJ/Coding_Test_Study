N = int(input())
arr = list(map(int, input().split()))
idx, cnt = 0, 0

while True:
    if idx == N - 1:
        break;
    
    if arr[idx] < arr[idx + 1]:
        cnt += 1 
    idx += 1 
print(cnt)