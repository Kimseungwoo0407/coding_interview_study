import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    d = deque()
    d.append((x,y))

    while d:
        x,y = d.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0 <= ny < m and graph[nx][ny] == 1:
                d.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))
