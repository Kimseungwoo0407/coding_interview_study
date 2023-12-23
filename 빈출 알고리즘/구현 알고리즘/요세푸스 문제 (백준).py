n, k = map(int,input().split())

data = [i for i in range(1,n+1)]

result = []
count = 0

for i in range(n):
    count += k-1
    if count >= len(data):
        count = count%len(data)

    result.append(str(data.pop(count)))

print("<",", ".join(result),">", sep='')