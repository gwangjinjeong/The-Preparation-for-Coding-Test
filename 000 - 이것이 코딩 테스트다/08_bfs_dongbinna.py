from collections import deque
import sys

n, m = list(map(int, sys.stdin.readline().split()))

# 0. preparation
maze = []

for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

# 잘못된 예: visited = [[False] * m] * n
visited = [[False] * m for _ in range(n)] # 이렇게 해야한다.

# 1. initialization
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
que = deque()
que.append((0, 0))
visited[0][0] = True

# 2. Breadth first search
def bfs(n,m,que, visited, maze):
    result = []
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or n <= ny or nx < 0 or m <= nx:
                continue
            if not visited[ny][nx] and maze[ny][nx] > 0:# 이렇게하면 vistiedp[4][0] 이렇게 되어서 out of list
                que.append((nx, ny))
                visited[ny][nx] = True
                maze[ny][nx] = maze[y][x] + 1
                if ny == n-1 and nx == m-1:
                    result.append(maze[ny][nx])
    return result

# 2. Result
result = bfs(n,m,que, visited, maze)
print(min(result))