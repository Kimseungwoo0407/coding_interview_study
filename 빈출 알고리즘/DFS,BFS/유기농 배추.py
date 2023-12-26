from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    d = deque()
    d.append((x,y))

    while d:
        x, y = d.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>=n or ny >= m:
                continue

            if matrix[nx][ny]:
                d.append((nx,ny))
                matrix[nx][ny] = 0
    return

for _ in range(t):
  m, n, k = map(int, input().split())
  matrix = [[0]*m for _ in range(n)]

  for i in range(k):
    x, y = map(int, input().split())
    matrix[y][x] = 1

  cnt = 0
  for i in range(n):
    for j in range(m):
      if matrix[i][j] ==1:
        bfs(i, j)
        cnt +=1

  print(cnt)