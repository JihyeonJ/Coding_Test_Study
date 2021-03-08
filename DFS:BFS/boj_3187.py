from collections import deque 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1
    sheep_cnt, wolf_cnt = 0, 0
    while queue:
        a, b = queue.popleft()
        if g[a][b] == 'v':
            sheep_cnt += 1
        elif g[a][b] == 'k':
            wolf_cnt += 1
        for i in range(4):
            nx = a + dx[i]
            ny = a + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and g[nx][ny] != '#':
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

        if sheep_cnt >= wolf_cnt:
            wolf_cnt = 0
        else:
            sheep_cnt = 0
        return [sheep_cnt, wolf_cnt]

m, n = map(int, input().split())
g = [list(input().strip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
queue = deque()
sheep, wolf = 0, 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and g[i][j] != '#':
            sheep_cnt, wolf_cnt = bfs(i, j)
            sheep += sheep_cnt
            wolf += wolf_cnt
print(sheep, wolf)