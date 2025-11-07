# 8번

# 9번

# 22번

# 35 - 거스름돈 계산
# 지불할 금액 32100
# 지불할 금액 50000
# 거스름돈 17900

product = 32100
pay = 50000
charge =  pay - product

print(f'물건가격 : {product}, 지불금액 : {pay}, '\
 f'거스름돈 : {charge}')

n50000 = int(charge / 50000)
print('50000원 : ', n50000, '개')
charge = charge - (50000 * n50000)

n10000 = int(charge / 10000)
print('10000원 : ', n10000, '개')
charge = charge - (10000 * n10000)

n5000 = int(charge / 5000)
print('5000원 : ', n5000, '개')
charge = charge - (5000 * n5000)

n1000 = int(charge / 1000)
print('1000원 : ', n1000, '개')
charge = charge - (1000 * n1000)

n500 = int(charge / 500)
print('500원 : ', n500, '개')
charge = charge - (500 * n500)

n100 = int(charge / 100)
print('100원 : ', n100, '개')
charge = charge - (100 * n100)

# =================================

# n5000 = chare // 5000
# print('5000원', n5000, '개')
# charge = cahrge % 5000

# 물건 가격을 입력하세요 17670
# 손님이 낸 돈을 입력하세요 20000

#
# 거스름돈 총액 7330
# 50000 : 0개
# 10000 : 0개
# 5000 : 1개
# 1000 : 2개
# 500 : 0개
# 100 : 3개
# 50 : 0개
# 10 : 3개

