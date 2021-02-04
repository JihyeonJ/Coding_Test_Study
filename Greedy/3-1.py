N, M = map(int, input().split());
arr = [[int(x) for x in input().split()] for _ in range(N)];
res = -1;
 
for i in range(0, N):
    maxtmp = min(arr[i]);
    res = max(res, maxtmp)
 
print(res);