n = int(input())

data = list(map(int,input().split()))

a = 0
result = []

for i in range(n-1):
    if data[i] < data[i+1]:
        a += data[i+1] - data[i]
    else:
        result.append(a)
        a = 0

result.append(a)
print(max(result))