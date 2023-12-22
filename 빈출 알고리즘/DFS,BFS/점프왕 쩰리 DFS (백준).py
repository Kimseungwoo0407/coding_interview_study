def dfs(x,y):
    if x >= n or x <0 or y>=n or y < 0 or visited[x][y] == 1:
        return

    if graph[x][y] == -1:
        visited[x][y] = 1
        return

    visited[x][y] = 1

    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])


# 게임 구역의 크기 N을 입력받는다.
n = int(input())

# 게임판의 구역을 입력받는다. 2차원 리스트
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문여부를 저장할 visit 2차원 리스트를 만든다.
visited = [[0] * n for _ in range(n)]

# 출발은 0,0에서 하므로 dfs(0,0)을 호출한다.
dfs(0, 0)

# 결과 출력
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')