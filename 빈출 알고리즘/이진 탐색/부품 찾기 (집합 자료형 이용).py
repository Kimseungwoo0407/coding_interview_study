# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자

n = int(input())
data_1 = set(map(int, input().split()))
m = int(input())
data_2 = list(map(int, input().split()))

for i in data_2:
    if i in data_1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
