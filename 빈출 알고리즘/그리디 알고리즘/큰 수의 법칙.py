# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번을 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징
# 가장 큰수를 k번 더하고, 두 번째로 큰 수를 한 번 더하는 연산 반복


n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

first = data[n-1] # 6
second = data[n-2] # 5

result = 0

while True:
    for _ in range(k):
        if m != 0:
            result +=first
            m-=1
        else:break
    if m == 0 :
        break
    result +=second
    m -= 1

print(result)

# 앞서 작성한 코드는 M이 10,000 이하이므로 이 방식으로도 문제 해결 가능
# 만약 100억 이상처럼 커진다면 시간 초과 판정을 받을 것 이다.