import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

# 부모 저장 배열
parent = [0] * (n+1)

# 양방향 연결 정보 저장
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    for i in graph[v]:
        if parent[i]==0:
            parent[i] = v
            dfs(i)


dfs(1)

for i in range(2,n+1):
    print(parent[i])