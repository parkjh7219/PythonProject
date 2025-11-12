# while
# 조건이 참일동안 반복을 실행하는 문장
# 주로 언제 끝날지 명확하게 정해지지 않은 반복에 사용

# while 조건:
#   반복 실행할 문장

# Hello World 5번 출력하기

# i = 1           # 초기화
# while i <= 5:   # 반복 조건식
#     print('Hello World') # 여기까지만 쓰면 무한루프 , i 값이 고정돼있음
#     i += 1      # 증감식 , i값을 1씩 올려서 5에 도달하면 멈출 수 있게 함
#


# ex) 1 ~ 100 사이 정수 중
# 3의 배수지만, 2의 배수가 아닌 정수 출력
# 또한, 누적합도 계산해서 출력

# i = 1
# sum = 0
# while i <= 100:
#     if i % 3 == 0 and i % 2 != 0:
#         sum += i
#         print (i, end = ' ')
#     i += 1
# print()
# print(sum)

# i = 3
# sum = 0
# while i <= 100:
#      if i % 2 != 0:
#          sum += i
#          print (i, end = ' ')
#      i += 3
# print()
# print(sum)

# ----
# 만일 조건식이 언제나 참이라면?  - 무한루프

# while의 경우
#
# i = 1
# while True:
#     print (i, end = ' ')
#     i += 1
    
# for 문은 유한한 반복을 염두에 두고 설계 
# 그래도 무한루프를 만들고 싶다면 iter 함수 이용
#
# i = 1
#
# for _ in iter(int, 1):
#     if i == 99999: break # break 로 끝나는 값 지정
#     print (i, end = '')
#     i += 1
# print()
#
# #======
#
# import itertools
#
# for i in itertools.count():
#     if i == 99999: break
#     print (i, end = '')
#
# print()