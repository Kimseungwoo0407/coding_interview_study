# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 불가능할 때는 -1을 출력

n, m = int(input().split())

array = []

for _ in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])