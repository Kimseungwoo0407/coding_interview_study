def solution(x):
    answer = True
    a = str(x)
    result = 0
    for i in a:
        result += int(i)

    if x % result == 0:
        return answer
    else:
        return False