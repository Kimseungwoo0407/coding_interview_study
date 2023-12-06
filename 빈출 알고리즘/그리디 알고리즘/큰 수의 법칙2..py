# 반복되는 수열에 대해서 파악하자 -> 가장 큰 수와 두 번째로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
# n,m,k = 5, 8 ,3일 때 수열은 {6,6,6,5}가 반복된다 그럼 수열의 길이는 K+1이 된다
# 따라서 M을 (K+1)로 나눈 몫이 수열의 반복 되는 횟수가 된다. + 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# M이 (K+1)로 나누어 떨어지지 않는 경우는 M을 (K+1)로 나눈 나머지 만큼 가장 큰 수가 추가로 더해지므로 이를 고려해야한다
# 가장 큰 수가 더해지는 횟수는 다음과 같다.
# int(M/(K+1)) * K+ M % (K+1)

n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)