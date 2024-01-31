def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)