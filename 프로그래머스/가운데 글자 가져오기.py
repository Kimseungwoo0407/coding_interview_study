def solution(s):
    a = len(s) // 2
    if len(s) % 2 == 0:
        return s[a-1:a+1]
    else:
        return s[a]