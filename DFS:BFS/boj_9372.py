for _ in range(int(input())):
    n, m = map(int, input().split())

    g = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a - 1][b - 1] = 1
        g[b - 1][a - 1] = 1

    def dfs(v):
        visited[v] = True
        for i in g[v]:
            if not visited[i]:
                dfs(i)

    visited = [False] * n;
    count = 0

    for x in range(n):
        if visited[x] == False:
            dfs(x)
            count += 1

    print(count)