x,y = map(int,input().split())

day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
cnt = 0
for i in range(1,13):
    for j in range(1,32):
        if i in [4,6,9,11]:
            if j > 30:
                break
        elif i in [2]:
            if j > 28:
                break
        if x == i and y == j:
            print(day[cnt])
            break
        cnt += 1
        if cnt > 6:
            cnt = 0
