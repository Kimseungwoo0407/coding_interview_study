# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array1 = [i*i for i in range(1,10)]
print(array1)

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array2 = [[0] * m for _ in range(n)]
print(array2)

# N * M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array3 = [[0]*m] * n
print(array3)

array3[1][1] = 5
print(array3)

# 리스트 관련 기타 메서드
a = [1,4,3]
print('기본 리스트:',a)

# append() : O(1)
# sort() : O(NlogN)
# reverse() : O(N)
# insert() : O(N)
# count() : O(N)
# remove() : O(N)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)