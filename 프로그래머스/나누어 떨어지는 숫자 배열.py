def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result += [i]

    if len(result) == 0:
        return [-1]
    else:
        return sorted(result)