# 실습 시 고정폭 글꼴을 사용할 것

# 1번

a = '*'
b = ' '
print(a,b,b,b,a,b,b,b,b,a,a,b,b,b,b,a,a,a,a,b,b,b,b,a,a,a,a,b,b,b,b,a,b,b,b,a)
print(a,b,b,b,a,b,b,b,a,b,b,a,b,b,b,a,b,b,b,a,b,b,b,a,b,b,b,a,b,b,b,a,b,b,b,a )
print(a,a,a,a,a,b,b,a,b,b,b,b,a,b,b,a,a,a,a,b,b,b,b,a,a,a,a,b,b,b,b,b,a,b,a  ) # window 키 + . 누르면 이모지 생성
print(a,b,b,b,a,b,b,a,a,a,a,a,a,b,b,a,b,b,b,a,b,b,b,a,b,b,b,a,b,b,b,b,b,a  ) # ㅁ 누르고 한자키 쓰면 문자열 생성
print(a,b,b,b,a,b,b,a,b,b,b,b,a,b,b,a,b,b,b,b,a,b,b,a,b,b,b,b,a,b,b,b,b,a  ) #print('*  *') # 이렇게 하기

print('  //////')
print( ' | 0 0  |')
print('(|  ^   |)')
print(' | [_]  |')
print('  ----- ')

print('            +---+')
print('            |   |')
print('        +---+---+')
print('        |   |   |')
print('    +---+---+---+')
print('    |   |   |   |')
print('+---+---+---+---+')
print('|   |   |   |   |')
print('+---+---+---+---+')

print(' /\ /\     -----')
print("( ' ' )  / Hello \ ") # 큰 따음표를 쓰면 그 안의 작은 따음표는 문자로 처리됨
print('(  -  ) <  Junior |')
print(' | | |   \ Coder!/')
print('(__|__)    -----')

# 2번

name = '박진환'
weight = 72
age = 28

print(name, weight, age)
# 한글자만 쓰고 ctrl + space 키 누르면 생성한 변수를 불러올 수 있음
# 선택한 다음 enter 또는 tab 


# 3번

# 사람이 이해할 수 있는 수학식 (보기) 를 컴퓨터가 이해할 수 있는 표현식 , (+-*/를 사용한 한줄짜리 수식)으로 바꾸세요
# 3 * x
# 3 * x + y
# (x + y) / 7
# (3 * x + y) / (z + 2)

# 정확한 연산 결과가 필요할 경우에는 수학 관련 라이브러리를 사용해야 함

# 4번

# 넘버라는 변수는 (1/3)*3 의 값으로 할당 , 답은 1
# c나 java에서는 정수 나눗셈 1/3 은 몫만 챙기고 나머지는 버림

number = (1/3)*3
print(number)

# 5번

# quotient = 2.33 , / 는 나누기, // 는 몫, % 는 나머지
# remainder = 1 , 7 나누기 3에서 몫은 6 나머지 1

quotient = 7 / 3
print(quotient)

remainder = 7 % 3
print(remainder)

# 6번

result = 11
result /= 2 # result / 2 와 같은 뜻 , 그 결과값을 다시 result에 할당하세요

print(result)

# 7번

x = 2.5; y = -1.5; m = 18; n = 4

a = x + n * y - (x + n) * y
b = m / n + m % n
c = 5 * x - n / 5
d = 1- (1 - (1 - (1 -(1 - n))))

print(a, b, c, d)

