from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    d = deque(list(map(int, input().split())))
    cnt = 0
    while d:
        best = max(d)
        front = d.popleft()
        m -= 1

        if best == front:
            cnt+=1
            if m < 0:
                print(cnt)
                break
        else:
            d.append(front)
            if m < 0:
                m = len(d) - 1