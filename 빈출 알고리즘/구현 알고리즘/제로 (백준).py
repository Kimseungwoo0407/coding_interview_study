# K가 100,000
import sys
input = sys.stdin.readline

n = int(input())

data = []

for _ in range(n):
    a = int(input())
    if a != 0:
        data.append(a)
    else:
        data.pop()

result = sum(data)
print(result)