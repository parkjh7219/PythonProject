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
#
# for i in range (1, 5+1):
#     for j in range (1, i+1): # 반복문의 변수는 i,j,k,l,m 순으로 사용
#         print ('*', end = '')
#     print()


# *****
# ****
# ***
# **
# *
#
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

for i in range(1,5+1):
    for j in range(5 - i):
         print (' ',end='')
    for k in range(i):
         print ('*',end='')
    print()

