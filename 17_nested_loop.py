# 중첩 반복문
# 반복문 안에 또 다른 반복문이 들어있는 구조

# 표, 행렬 데이터를 순회시 주로 사용
# 계산량이 많아져서 실행시간이 급격하게 증가하는 단점 존재

# 다음의 별 모양을 반복문으로 구현하시오

# *
# **
# ***
# ****
# *****

# for i in range (1, 5+1):
#     for j in range (1, i+1): # 반복문의 변수는 i,j,k,l,m 순으로 사용
#         print ('*', end = '')
#     print()

# *****
# ****
# ***
# **
# *

# for i in range (1,5+1):
#     for j in range (i,5+1):
#         print('*',end='')
#     print()
#
# for i in range (5): # 0~4
#     for j in range (5-i):
#         print('*',end='')
#     print()


#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,5+1):
#     for j in range(i,4+1):
#         print (' ',end='')
#     for k in range(1,i+1):
#         print ('*',end='')
#     print()

# for i in range(1,5+1):
#     for j in range(5 - i):
#          print (' ',end='')
#     for k in range(i):
#          print ('*',end='')
#     print()

# # 개선된 코드 2
#
# import random
#
# lotto = str(random.randint(123, 789))
# mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
# prize = 0
# match = 0   # 일치수
# #
# 개선된 코드 1
# for i in range(0, 3):
#    if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]:
#        match += 1
#
# 개선된 코드 2
# for i in range(0, 3):
#     for j in range(3):
#         if lotto[i] == mykey[j]: match += 1
#
# if match == 3: prize = 1000000
# elif match == 2: prize = 10000
# elif match == 1: prize = 1000
#
# result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 갯수 : {match}
# 당첨 금액 : {prize}원
# '''
# print(result)



# 30 구구단 테이블 - 반복문으로 재작성

# result = f'''
#           Multiplication Table
#       1   2   3   4   5   6   7   8   9
# ---------------------------------------
# '''
#
# for i in range(1, 9+1):
#     result += f'{i} | {i*1:3d} {i*2:3d} {i*3:3d} {i*4:3d} '\
#               f'{i*5:3d} {i*6:3d} {i*7:3d} {i*8:3d} {i*9:3d}\n'
#
# print(result)

result = f'''
          Multiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------
'''

for i in range(1, 9+1):
    for j in range(1, 9+1):
        result += f'{i} | {i*j:3d}'

print(result)
