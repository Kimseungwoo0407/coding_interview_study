# 큰 문제를 해결하기 위해 작은 문제를 호출한다 -> 탑다운 방식

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)