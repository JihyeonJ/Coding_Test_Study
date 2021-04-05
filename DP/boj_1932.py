N = int(input())
tri = []
dp = [0]

for i in range(N):
    tmp = list(map(int, input().split()))
    tri.append(tmp)

for i in range(1, N):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[N-1]))
