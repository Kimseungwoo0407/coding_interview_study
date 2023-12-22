from collections import deque

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# 오른쪽으로 이동
dx = [0,1]
# 아래로 이동
dy = [1,0]

def bfs(x,y):
    d = deque()
    d.append([x,y])

    while d:
        x,y = d.popleft()
        step = graph[x][y]

        if graph[x][y] == -1:
            return True

        for move in range(2):
            nx = x + dx[move] * step
            ny = y + dy[move] * step
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                d.append([nx,ny])

if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')