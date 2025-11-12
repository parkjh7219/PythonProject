# 21 - 반복 추가
#
# tax = 0
# rate = 0
#
# while True:
#     salary = int(input('연봉을 입력하세요(만원 단위): '))
#     isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
#     if isMarried == 'n':
#         if salary < 3000:
#             rate = 10
#             break
#         else:
#             rate = 25
#             break
#     elif isMarried == 'y':
#         if salary < 6000:
#             rate = 10
#             break
#         else:
#             rate = 25
#             break
#     else:
#         print('성별 오류!!')
#
# tax = salary * (rate / 100)
# result = f'''
# 적용세율 : {rate}%
# 납부해야 할 세금은 {tax}만원입니다
# '''
#
# print(result)

# 21 = 풀이

# tax = 0
# rate = 0
#
# while True:
#     salary = int(input('연봉을 입력하세요(만원 단위): '))
#     isMarried = input('결혼 여부를 입력하세요 (y:결혼, n:미혼)?').lower()
#     if isMarried == 'n':
#         if salary < 3000:
#             rate = 10
#         else:
#             rate = 25
#     elif isMarried == 'y':
#         if salary < 6000:
#             rate = 10
#         else:
#             rate = 25
#     else:
#         print('성별 오류!!')
#
#     tax = salary * (rate / 100)
#     result = f'''
#     적용세율 : {rate}%
#     납부해야 할 세금은 {tax}만원입니다
#     '''
#
#     print(result)
#     cont = input ('계속하시겠습니까?(y/n)').lower()
#     if cont == 'n' :
#         break

# 23 - 중첩
#
# import random
#
# while True:
#     lotto = str(random.randint(123, 789))
#     mykey = input('복권 숫자 3자리를 입력하세요 (예:123): ')
#
#     prize = 0
#     match = 0
#     message = '일치하는 숫자가 없습니다'
#
#     for i in range(3):
#         for j in range(3):
#             if lotto[i] == mykey[j]:
#                 match += 1
#     match match:
#         case 3:
#             prize = 1000000
#             message = '1등상입니다'
#         case 2:
#             prize = 10000
#             message = '2등상입니다'
#         case 1:
#             prize = 1000
#             message = '3등상입니다'
#
#     print(message)
#     if match > 1:
#         break
#
# result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 갯수 : {match}
# 당첨 금액 : {prize}원
# '''
# print(result)


# 26 - 반복 추가 2

# import random
# result = ''
#
# number = random.randint(1, 10)
#
# while True:
#     num = int(input('1~100사이 숫자를 하나 입력하세요: '))
#     result = '빙고! 숫자를 맞췄습니다!!'
#     if number > num: result = '추측한 숫자가 작아요!'
#     elif number < num: result = '추측한 숫자가 커요!'
#     elif number == num:
#         break
#     print(result)
#
# print(f'{number} : {result}')

# 30 - 중첩

# print(f'''
#           Multiplication Table
#       1   2   3   4   5   6   7   8   9
# ---------------------------------------''')
#
# result1 = 0
# result2 = 0
#
# for i in range(1, 9+1):
#     result1 =  f'{i} |'
#     print(result1, end = '')
#     for j in range(1, 9+1):
#         result2 = f'{i*j:4d}'
#         print(result2, end ='')
#     print()

# result=f'''
#           Multiplication Table
#       1   2   3   4   5   6   7   8   9
# ---------------------------------------
# '''
#
# for i in range(1, 9+1):
#     result +=  f'{i} |'
#     for j in range(1, 9+1):
#         result += f'{i*j:4d}'
#     result += '\n'
#
# print(result)


# # 31 - match case 로 변경
# type = '식별안됨'
# bank = '식별안됨'
# result = ''
#
#

#
# while True:
#     num = input('6자리 카드번호를 입력하세요: ')
#     if len(num) == 6:
#         if num[:2] == '35':
#             type = 'JCB카드'
#             match num[2:]:
#                 case '6317':
#                     bank = 'NH농협카드'
#                     break
#                 case '6901':
#                     bank = '신한카드'
#                     break
#                 case '6912':
#                     bank = 'KB국민카드'
#                     break
#         elif num[0] == '4':
#             type = '비자카드'
#             match num[1:]:
#                 case '04825':
#                     bank = '비씨카드'
#                     break
#                 case '38676':
#                     bank = '신한카드'
#                     break
#                 case '57973':
#                     bank = '국민은행'
#                     break
#         elif num[0] == '5':
#             type = '마스터카드'
#             match num[1:]:
#                 case '15594':
#                     bank = '신한카드'
#                     break
#                 case '24353':
#                     bank = '외환카드'
#                     break
#                 case '40926':
#                     bank = '국민은행'
#                     break
#         else:
#             print('카드 번호를 확인해서 다시 입력 해주세요')
#     else:
#         print('카드 번호를 확인해서 다시 입력 해주세요')
#
# result = f'카드 종류 및 은행: {type} - {bank}'
# print(result)


# num = input('6자리 카드번호를 입력하세요: ')
# type = '식별안됨'
# bank = '식별안됨'
# result = ''
#
# if len(num) == 6:
#     match num[0]:
#         case 3:
#             type = 'JCB카드'
#             match num[1]:
#                 case '56317': bank = 'NH농협카드'
#                 case '56901': bank = '신한카드'
#                 case '56912': bank = 'KB국민카드'
#         case 4:
#             type = '비자카드'
#         case 5:
#             type = 'JCB카드'
#             match num[1]:
#                 case '56317': bank = 'NH농협카드'
#                 case '56901': bank = '신한카드'
#                 case '56912': bank = 'KB국민카드'
#         case _: pass






