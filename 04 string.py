# 문자열 다루기

#문자열 포매팅 사용하기 전

print ('Hello, World ~!!')
print ('Hello, Python~!!')

#---

say = 'World'
print ('Hello, ' + say + '~!!')
say = 'Python'
print ('Hello, ' + say + '~!!')


# 문자열 포매팅 1 - % , p ~67

print('Hello, %s~!!' % say)

name, weight, age = '홍길동' , 55.5 ,35
print('이름 : %s, 몸무게 : %.1fkg, 나이 : %d' # .1은 소수점 한자리까지만 출력
        % (name, weight, age))

# 문자열 포매팅 1 - .format

print('Hello, {0}~!!'.format(say))
print('이름 : {0}, 몸무게 : {1:.2f}kg, 나이 : {2}' # :.2f는 소수점 2자리까지 출력
      .format(name, weight, age))
print('이름 : {}, 몸무게 : {}kg, 나이 : {}' # 숫자 없어도 됨
      .format (name, weight, age))

# 문자열 포매팅 1 - f포매팅 (3.6 이상 , 추천) , p ~77

print(f'Hello, {say}~!!')
print(f'이름 : {name}, 몸무게 : {weight}, 나이 : {age}')

# 문자열 입력받기
# input(입력 시 표시할 메세지)
# name = input('이름을 입력하세요 : ')
# print(name)

# ex) 두 수를 입력받아 사칙연산 후 결과 출력
# input을 통해 입력받은 내용은 기본적으로 문자열
# 입력한 내용을 숫자로 바꾸려면 형변환 함수 필요 !
# 형변환 : 데이터의 자료형을 다른 형식으로 바꾸는 것
# 묵시적 (또는 암시적) 형변환 : 파이썬이 자동으로 변환해 줌 (= 프로모션)
# 명시적 형변환 : 프로그래머가 직접 변환
# int(대상), float(대상), str(대상)

# x = input('사칙연산 할 첫번째 숫자를 입력하세요 :')
# y = input('사칙연산 할 첫번째 숫자를 입력하세요 :') , 안됨 // control /

x = int(input('사칙연산 할 첫번째 숫자를 입력하세요 :'))
y = int(input('사칙연산 할 첫번째 숫자를 입력하세요 :'))

print(x + y , x - y , x * y)

#문자열 슬라이싱

