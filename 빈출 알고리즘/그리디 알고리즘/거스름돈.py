# 그리디 알고리즘 정당성 : 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을
# 종합해 다른 해가 나올 수 없기 때문이다.
# ex) 800원을 거슬러 줄 때, 500,400,100원이라면, 500원 + 100원 + 100원 + 100원이 아닌 400+400이 더 최적이다.

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500,100,50,10] # 화폐의 종류가 k라고 할 때, 위 소스 코드의 시간 복잡도는 O(K)이다.

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

