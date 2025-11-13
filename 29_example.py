# 21 - 함수로 재작성 : computeTax

# from parkjh7269.example import compute_tax
#
# while True:
#     salary = int(input('연봉을 입력하세요(만원 단위): '))
#     isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
#
#     result = compute_tax(salary,isMarried)
#
#     print(result)
#     cont = input ('계속하시겠습니까?(y/n)').lower()
#     if cont == 'n' : break

# 23 - 함수로 재작성 : lotto999

# 1. 함수 하나로 작성해보기

# import random
# from parkjh7269.example import lotto999
#
# while True:
#
#     lotto = str(random.randint(123, 789))
#     mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
#
#     match = lotto999(mykey,lotto)
#     if match > 1:
#         break

# 2. 함수 세개로 나눠서 작성해보기

# import random
# from parkjh7269.example import lotto999_repeat
# from parkjh7269.example import lotto999_case
# from parkjh7269.example import lotto999_output
#
#
# while True:
#
#     lotto = str(random.randint(123, 789))
#     mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
#
#     match = lotto999_repeat(mykey,lotto)
#     prize = lotto999_case(match)
#     result = lotto999_output(lotto,mykey,match,prize)
#
#     print(result)
#
#     if match > 1:
#         break

# 24 - 함수로 재작성 : gugudan

# from parkjh7269.example import gugudan
#
# dan = int(input('출력할 구구단 단수를 입력하세요 (1-9): '))
#
# result = gugudan(dan)
#
# print(result)

# 32 - 함수로 재작성 : checkJumin

# jumin = '450124-1234590'
# sum = 0
#
# code = []
#
# code = [int(j) for j in jumin if j.isdigit()] # 코드 한줄로 줄여보기
#
# print(f'추출된 주민번호 : {code}')
#
# wght = []
#
#
# wght = [(i % 8) + 2 for i in range(12)]
#
# print(f'자동생성된 가중치 :{wght}')
#
# for i in range(12):
#     sum += code[i] * wght[i]
#
# print(sum)
#
# checker = 11 - (sum % 11)
# print(checker, str(checker)[-1] == jumin[13])