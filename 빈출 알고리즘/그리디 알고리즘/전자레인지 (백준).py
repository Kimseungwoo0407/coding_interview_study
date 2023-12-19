t = int(input()) # 100

time = [300, 60, 10]

data = [0] * 3

for i in range(len(time)):
    data[i] = t // time[i]
    t = t % time[i]
if t == 0 :
    print(*data)
else:
    print(-1)
