a, b = map(int,input().split())
arr = []
i = 0
while len(arr) <= 1000:  # 충분히 큰 배열을 만들기 위한 조건
    arr += [i] * i  # 각 숫자를 그 수만큼 배열에 추가
    i += 1

print(sum(arr[a-1:b]))