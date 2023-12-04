# 문자열 초기화
data = 'Hello World'
print(data)

data = " Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = 'World'

print(a+ " "+b)

a = 'String'
print(a*3)

a = 'ABCDEF'
print(a[2:4])

# 튜플 자료형

a = (1,2,3,4)
print(a)
# a[2] = 7 튜플의 경우 대입 연사자를 사용하여 값 변경할 수 없다.

# 사전 자료형 ( 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# 사전 자료형에 특정한 원소가 있는지 검사할 때는 '원소 in 사전'의 형태를 사용할 수 있다.
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")


# 사전 자료형 관련 함수
## 키 데이터만 담은 리스트
key_list = data.keys()

## 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])


# 집합 자료형 (set) : 중복 허용 x, 순서 없음 + 특정한 데이터가 이미 등장한 적이 있는지 여부 체크할 때 효과적
# 집합 자료형 초기화 방법 1
data =set([1,1,2,3,4,4,5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

# add(), remove() 함수는 모두 시간 복잡도 O(1) : 집합 자료형
data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)