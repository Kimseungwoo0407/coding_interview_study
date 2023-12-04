# 내장 함수 : print(), input(), sort()와 같은 것을 포함
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리(순열, 조합)
# heapq : 힙 기능을 제공하는 라이브러리. 우선 순위 큐 기능 구현하기 위해 사용
# bisect : 이진 탐색 기능을 제공하는 라이브러리
# collections : 덱, 카운터 등의 유용한 자료구조를 포함하고 있는 라이브러리
# math : 팩토리얼, 제곱근, 최대공약수, 삼각 함수 관련 함수부터 파이와 같은 상수 포함

# 1. 내장함수 (iterable 객체 : 리스트, 사전 자료형, 튜플 자료형 등)
result = sum([1,2,3,4,5])
print(result)

result = min([1,2,3,4,5]) # max()
print(result)

# eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과 반환
result = eval("(3+5) * 7")
print(result)

# sorted() 함수는 iterable 객체가 들어왔을 때, 정렬된 결과 반환
result = sorted([9,1,8,5,4]) # 오름차순으로 정렬
print(result)
result = sorted([9,1,8,5,4],reverse=True) # 내림차순으로 정렬
print(result)

# 원소를 튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬
result = sorted([('홍길동',35), ('이순신',75), ('아무개',50)],key=lambda x:x[1], reverse=True)
print(result)

# iterable 객체는 기본적으로 sort() 함수 내장하고 있어서 sorted() 안써도 됨
data = [9,1,8,5,4]
data.sort()
print(data)

from itertools import permutations

# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 계산
data = ['A','B','C']
result = list(permutations(data,3)) # 모든 순열 구하기
print(result)

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
# 다만 원소를 중복하여 뽑음. product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다

from itertools import product
data = ['A','B','C']
result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)


# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서 고려 x
# 나열하는 모든 경우를 계산, 다만 원소를 중복해서 뽑는다.

from itertools import combinations_with_replacement

data = ['A','B','C']
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)


# heapq : 힙 기능을 위한 라이브러리
# 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
# 파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도는 O(NlogN)에 오름차순 정렬 완료
# 보통 최소 힙 자료구조의 최상단 원소는 항상 가장 작은 원소 이기 때문이다.

# 원소 삽입 시 heapq.heappush(), 꺼내고자 할 때는 heapq.heappop()

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 파이썬에서는 최대 힙을 제공 x 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식 사용
# 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)


# bisect
# 파이썬에서 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리 제공
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용
# bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용, 두 함수는 시간 복잡도 O(logN)에 동작
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽(오른쪽) 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때, 효과적
print(bisect_left(a,x))
print(bisect_right(a,x))

from bisect import bisect_left, bisect_right

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

# collections (deque() ,Counter())
# deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다.
# 다만 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입 or 삭제할 때는 매우 효과적으로 사용
# deque는 스택이나 큐의 기능을 모두 포함한다고도 볼 수 있기 때문에 스택 or 큐 자료구조의 대용으로 사용될 수 있다.
# 첫 번째 원소를 제거할 때 popleft()를 사용하며, 마지막 원소를 제거할 때 pop()을 사용한다.
# 첫 번째 인덱스에 원소 x를 삽입할 때 appendleft(x)를 사용하며, 마지막 인덱스에 원소를 삽입할 때 append(x)를 사용한다.
# 따라서 deque를 큐 자료구조로 이용할 때, 원소 삽입 시 append()을 사용하고, 원소를 삭제할 때에는 popleft()를 사용하면 된다.
# 그러면 먼저 들어온 원소가 항상 먼저 나가게 된다.

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# Counter는 등장 횟수를 세는 기능을 제공

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

# math : 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리

# factorail(x) 함수는 x! 값 반환

import math
print(math.factorial(5)) # 5 팩토리얼 출력

# sqrt(x) 함수는 제곱근 반환
import math

print(math.sqrt(7))


# 최대 공약수를 구해야 할 때는 gcd(a,b) 함수 이용
import math

print(math.gcd(21,14))

# 파이(pi)나 자연상수 e 제공한다.

import math

print(math.pi) # 파이(pi) 출력
print(math.e) # 자연상수 e 출력