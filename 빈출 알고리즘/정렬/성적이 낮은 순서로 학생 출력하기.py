# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
# 학생의 수 ( 1 <= N <= 100,000 )

n = int(input())

data = []

for _ in range(n):
    x, y = input().split()
    data.append((x,int(y)))

# 키를 이용하여, 정수 기준으로 정렬
data = sorted(data, key=lambda student : student[1])

for student in data:
    print(student[0], end=' ')