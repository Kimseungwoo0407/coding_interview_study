n = input()

left = []
right = []

for i in range(len(n)//2):
    left.append(int(n[i]))
    right.append(int(n[i+len(n)//2]))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')

