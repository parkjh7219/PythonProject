# 실습시 고정폭 글꼴을 사용할 것!!
# 1
print('*   *    **    ****    ****    *   * ')
print('*   *   *  *   *   *   *   *   *   * ')
print('*****  *    *  ****    ****     * *  ')
print('*   *  ******  *   *   *   *     *   ')
print('*   *  *    *  *    *  *    *    *   ')

print('   /////   ')
print('  | o o |  ')
print(' (|  ^  |) ')
print('  | [_] |  ')
print('   -----   ')

print('            +---+')
print('            |   |')
print('        +---+---+')
print('        |   |   |')
print('    +---+---+---+')
print('    |   |   |   |')
print('+---+---+---+---+')
print('|   |   |   |   |')
print('+---+---+---+---+')

print('  /\_/\     -----    ')
print(" ( ' ' )  / Hello \ ")
print(' (  -  ) < Junior  | ')
print('  |   |   \ Coder!/  ')
print(' (__|__)    -----    ')

# 2
name = '홍길동'
weight = 55.5
age = 35
print(name, weight, age)

# 3
x, y, z = 10, 20, 30
print(3 * x)
print(3 * x + y)
print((x + y) / 7)
print((3 * x + y) / (z + 2))

# 4
# 정확한 연산 결과가 필요할 경우에는
# 수학관련 라이브러리를 사용해야 함
number = (1 / 3) * 3
print(number, 1 / 3, (1 / 3) * 3)
print(10 / 3, (10 / 3) * 3)

# 5
quotient = 7 // 3     # 몫
remainder = 7 % 3     # 나머지
print(7 / 3, quotient, remainder)

# 6
result = 11
result /= 2     # 복합연산자
print(result)

# 7
x, y, m, n = 2.5, -1.5, 18, 4

print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))
