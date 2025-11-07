#21

# mon = int (input('연봉을 입력하세요 (만원 단위): '))
# mar = input('결혼 여부를 입력하세요 (y: 결혼,n: 미혼) :')
#
# if mar == 'y':
#     if mon >= 6000:
#         tax = 0.25
#     else:
#         tax = 0.1
#
# else:
#     if mon >= 3000:
#         tax = 0.25
#     else:
#         tax = 0.1
#
# tlqkf = int(tax*100)
#
# print(tlqkf,'%')
# print(f'납부해야 할 세금은 {mon*tax}만원입니다.')


#23

# num = int(input('복권 숫자 3자리를 입력하세요 (예 : 123) : '))
#
# import random
# jackpot = random.randint(100, 999)
#
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
#
# x = jackpot // 100
# y = (jackpot % 100) // 10
# z = jackpot % 10
#
# if a == x :
#     ax = 1
# else:
#     ax = 0
#
# if b == y :
#     by = 1
# else:
#     by = 0
#
# if c == z :
#     cz = 1
# else:
#     cz = 0
#
# num = ax+by+cz
# if num > 0:
#     match num:
#         case 3:
#             result = '당첨 금액 : 100만원'
#         case 2:
#             result = '당첨 금액 : 만원'
#         case 1:
#             result = '당첨 금액 : 천원'
# else:
#     result = '당첨되지 못했습니다.'
#
# print (f'당첨번호 : {jackpot}')
# print (num)
# print (result)




# match = 0
# a == x or a == y or a == z
# match += 1
# b == x or b == y or b == z
# match += 1
# c == x or c == y or c == z
# match += 1

# print(match)


#26

#31

#32
