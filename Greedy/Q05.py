N, M = map(int, input().split());
ball = list(map(int, input().split()));
res = 0;

for i in range(0, N-1):
    for j in range(i+1, N):  
        if ball[i] != ball[j]:
            res += 1;

print(res)