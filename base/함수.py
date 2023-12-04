# 더하기 기능 함수 작성
def add(a,b):
    return a+b
print(add(3,7))

# return 문 없이 작성
def add(a,b):
    print('함수의 결과:', a+b)

add(3,7)

# 함수를 호출하는 라인에서 인자a와 b를 지칭해서 각각 값을 넣을 수 있음

def add(a,b):
    print('함수의 결과:',a+b)

add(b=7,a=3)

# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우
a = 0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

def add(a,b):
    return a+b

# 일반적으로 add() 매서드 사용
print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3,7))

# 입출력을 받을 때, 입력의 개수가 많은 경우
import sys
sys.stdin.readline().rstrip()

