from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1


n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
queue = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)