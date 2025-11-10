# # sum = 0
# #
# # for i in range(1, 101):
# #     if i % 3 == 0 and i % 2 != 0:
# #         sum += i
# #         print(i, end = ' ')
# #
# # print()
# # print(sum , end = '')
#
# for i in range (3, 100+1, 3):
#     if i % 2 == 0:
#         print(i, end =' ')
# print()

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

# 23 복권

# 24 구구단

# 26

# 30

# 32