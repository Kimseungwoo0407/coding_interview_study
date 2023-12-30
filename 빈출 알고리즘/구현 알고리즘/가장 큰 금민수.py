n = int(input())

for i in range(n,0,-1):
    if set(str(i)) <= {'4','7'}:
        print(i)
        break