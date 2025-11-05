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




#문자열 슬라이싱

