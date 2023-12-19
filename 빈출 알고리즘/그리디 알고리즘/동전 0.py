n, k = map(int,input().split())

data = []

for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)

count = 0

while k > 0:
    for i in data:
        if k // i !=0:
            count += k//i
            k = k % i

print(count)