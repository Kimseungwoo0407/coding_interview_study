n = int(input())

i = 0

while n > 0:
    i += 1
    n -= i

if i % 2 == 0:
    print('{}/{}'.format(i+n,1-n))
else:
    print('{}/{}'.format(1-n,i+n))