n = 1000 - int(input())


money = [500,100,50,10,5,1]

result = 0

for i in money:
    result += n//i
    n = n % i

print(result)