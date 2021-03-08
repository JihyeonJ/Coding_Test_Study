import sys
sys.setrecursionlimit(2000)

for k in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    visited = [False for i in range(n+1)]

    def dfs(v):
        visited[v] = True
        adjv = p[v]
        print(str(v) + " " + str(adjv))
        print(visited)
        if visited[adjv]:
            dfs(adjv)

    cycles = 0
    for j in range(1, n+1):
        if visited[j] == False:
            dfs(j)
            cycles += 1
    print(cycles)