m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

def dfs(x, y):
    visited[x][y] = 1
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)

count = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i, j)
            count += 1
print(count)