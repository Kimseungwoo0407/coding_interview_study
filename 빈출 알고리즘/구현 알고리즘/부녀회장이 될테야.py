t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    data = []

    for i in range(1,n+1):
        data.append(i)

    for i in range(k):
        for j in range(1,n):
            data[j] += data[j-1]

    print(data[n-1])