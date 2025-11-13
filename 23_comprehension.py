# 컴프리헨션
# 시퀀스 자료형 (리스트, 딕셔너리 등) 에서
# 한줄로 간결하게 생성 , 관리하는 문법
# 코드를 직관적으로 작성 가능 - 한줄로 표현, 속도도 빠르다, p148

person = ['혜교', '123-4567-8912', 'ab@abc.co.kr']
for p in person:
    print(p, end=' ')
print()

# [표현식 for 변수 in 반복가능객체]
result = [p for p in person]
print(result)

[print(p, end=' ') for p in person]
print()

# numbers 라는 리스트의 요소를 제곱해서 출력
numbers = [1,2,3,4,5,6,7,8,9,10]

# 지금까지의 방식
for i in numbers:
    print(i * i, end =' ')
print()

# 이제부터
[print(i * i, end =' ') for i in numbers]
print()

# 1~ 100 사이 4의 배수이지만, 6의 배수는 아닌 수
for i in range(1,100+1):
    if i % 4 == 0 and i % 6 != 0:
        print(i,end= '')
print()

# 표현식 for 변수 in 반복가능객체 if 조건 # 리스트 , 딕셔너리 자료형만 이렇게 쓸 수 있음
[print(i,end= '') for i in range(1,100+1) if i % 4 == 0 and i % 6 != 0]
print()

# numbers 라는 리스트의 요소를 제곱해서 결과를 리스트로 출력

numbers = [3,6,9,12,15]

results1 = []
for i in numbers:
    result.append(i * i)
print(results1)

result2 = [i * i for i in numbers] # result 1, 2를 출력하는 두 가지 방법
print(result2)                     # 더 간단하게 사용 가능 # append 를 생략 가능하다

# 좌석 초기화 # 22번 75번 줄 줄여보기

seats = []

for i in range(10):
    seats.append('○')
print(seats)

seats = ['○' for i in range(10)]
print(seats)

# 1~9까지 정수를 3 x 3 2차원 리스트에 출력

matrix = []

for j in range(3): # 1
    row = []
    for i in range(3): #2
        row.append(i+j*3+1) #3
    matrix.append(row)

print(matrix)

# [표현식 for 변수 in 반복가능객체 for 변수 in 반복가능객체] # 1차원
# [[표현식 for 변수 in 반복가능객체] for 변수 in 반복가능객체] # 2차원

matrix2 = [i+j*3+1 for j in range(3) for i in range(3)] # 한 줄로 나옴 = 1차원
print(matrix2)

matrix3 = [[i+j*3+1 for i in range(3)] for j in range(3)] # i 와 j 위치 변환된 것 확인 # 리스트 안에 리스트 = 2차원
print(matrix3)

# 참고 변수 하나를 더 만들면 깔끔하게 나오지만 , 우리가 하려는 축약과는 맞지 않아서 참고만 할 것

# num = 1

# for j in range(3):
#     row = []
#     for i in range(3):
#         row.append(num)
#         num += 1
#     matrix.append(row)

# print(matrix)

