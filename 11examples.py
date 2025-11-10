# 21
# salary = int(input('연봉을 입력하세요(만원 단위): '))
# isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
# tax = 0
# rate = 0
#
# if isMarried == 'n':        # 미혼
#     rate = 25               # 연봉 3000 이상시 세율
#     if salary < 3000:
#         rate = 10
# elif isMarried == 'y':      # 기혼
#     rate = 25               # 연봉 6000 이상시 세율
#     if salary < 6000:
#         rate = 10
# else:
#     print('성별 오류!!')
#
# tax = salary * (rate / 100)
# result = f'''
# 적용세율 : {rate}%
# 납부해야 할 세금은 {tax}만원입니다
# '''
#
# print(result)


# 23
import random

# 문자열 슬라이싱을 위해 생성한 난수는 문자형으로 변환
lotto = str(random.randint(123, 789))
# 문자열 슬라이싱을 위해 문자형으로 입력받음
mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
# 상금
prize = 0

# lotto = 357    # 난수로 생성한 3자리 숫자
# mykey = 735    # 사용자가 입력한 3자리 숫자

# num1 = lotto // 100
# num2 = (lotto % 100) // 10
# num3 = ((lotto % 100) % 10)
#
# key1 = mykey // 100
# key2 = (mykey % 100) // 10
# key3 = ((mykey % 100) % 10)
#
# match = 0     # 일치여부
# if num1 == key1 or num1 == key2 or num1 == key3:
#     match += 1     # match = match + 1
# if num2 == key1 or num2 == key2 or num2 == key3:
#     match += 1     # match = match + 1
# if num3 == key1 or num3 == key2 or num3 == key3:
#     match += 1     # match = match + 1

# lotto = str(357)    # 난수로 생성한 3자리 숫자
# mykey = str(735)    # 사용자가 입력한 3자리 숫자

match = 0   # 일치수
if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
    match += 1     # match = match + 1
if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
    match += 1
if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
    match += 1

if match == 3: prize = 1000000
elif match == 2: prize = 10000
elif match == 1: prize = 1000

result = f'''
당첨번호 : {lotto}
당신의 복권번호 : {mykey}
일치한 숫자 갯수 : {match} 
당첨 금액 : {prize}원 
'''
print(result)


# 26
import random

# 1~100 사이 임의의 난수 생성
number = random.randint(1, 100)
# 사용자로부터 값을 하나 입력 받음
mynum = int(input('1~100사이 숫자를 하나 입력하세요: '))

result = '빙고! 숫자를 맞췄습니다!!'
if number > mynum: result = '추측한 숫자가 작아요!'
elif number < mynum: result = '추측한 숫자가 커요!'

print(f'{number} : {result}')


# 31

# 32