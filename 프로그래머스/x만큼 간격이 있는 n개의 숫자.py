def solution(x, n):
    results = []
    a=0
    for i in range(n):
        a += x
        results.append(a)
    return results