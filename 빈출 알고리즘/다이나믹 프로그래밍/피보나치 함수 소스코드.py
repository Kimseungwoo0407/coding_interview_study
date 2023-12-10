# 이 경우 빅오 표기법을 이용하여 표기 시 -> O(2**N)
# N = 30이면, 약 10억 가량의 연산 수행해야함

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))