n = int(input())

count = 0
for _ in range(n):
    data = input()
    result = []
    for j in range(len(data)):
        if data[j] not in result or data[j] == data[j-1]:
            result.append(data[j])
        if len(result) == len(data):
            count += 1
print(count)