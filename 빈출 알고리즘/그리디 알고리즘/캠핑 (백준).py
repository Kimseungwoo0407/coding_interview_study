i = 1
while True:
    result = 0
    l,p,v = map(int,input().split()) # 5 8 20
    if l+p+v == 0:
        break
    result = v//p * l + min(v%p, l)
    print('Case {}: {}'.format(i,result))
    i +=1
