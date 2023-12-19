input_ = input().split('-')
total = sum(map(int, input_[0].split('+')))

for i in input_[1:]:
    total -= sum(map(int, i.split('+')))

print(total)