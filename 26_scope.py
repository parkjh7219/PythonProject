# 변수의 유효 범위 scope
# 변수나 이름이 유효하게 접근할 수 있는 범위
# 어떤 변수에 어디에서나 사용가능한지
# 어디서 접근할 수 없는지를 결정하는 규칙

# 파이썬의 scope : LEGB # LEG

# 지역 local 변수 . L
# 함수 내에 정의된 변수는 기본적으로 지역변수
# 따라서, 함수 내에서만 유효하고 함수를 벗어나면 사라짐

def greeting():
    msg = 'World'
    print(f'Hello {msg}!!')

greeting()
# print(msg) # 함수 내에 지정된 변수는 함수 내에서만 사용 가능 , 주석 풀고 실행해보면 변수가 선언되지 않았다고 나옴

# 전역 golbal 변수 , G
# 함수 밖에 정의된 변수는 기본적으로 전역 변수
# 따라서 함수 내에서도 접근 가능

message = 'Hello Python'

def greeting2():
    print(message) # 함수 밖에서 정의한 함수는 함수 내에서나 밖에서나 사용 가능하다

greeting2()

# 단, 전역벽수는 함수내에서 값을 수정하더라도
# 함수 밖으로 벗어나면 원래 값으로 되돌아 감

x,y = 3, 5

def swap(a,b):
    c = b
    b = a
    a = c
    print('함수 안 : ', a, b)
print('함수 호출 전 : ', x, y)
swap(x, y)                   # 함수 내에서 변수 수정, 함수 안에서만 사용 가능
print('함수 호출 후 : ', x, y) # 함수 내부에서 변수를 바꿔도 밖으로 나오면 원래대로 돌아온다

# 한편 , 함수 안에서 전역변수를 직접 변경하려면
# global 이라는 키워드를 사용해야 함!

def swap2():
    global x, y
    z = y
    y = x
    x = z
    print('함수 내부 : ', x, y)

print('함수 호출 전 : ', x, y)
swap2()
print('함수 호출 후 : ', x, y)