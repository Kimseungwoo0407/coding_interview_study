n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

count = -1

def dfs(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

dfs(1)
print(count)