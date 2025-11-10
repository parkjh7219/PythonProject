# for 반복
#
# 정해진 횟수만큼 코드를 반복
#
# for 반복변수 in range (시작값, 종료값-1 , 증감값):
#
# 반복실행문장


# range 함수 사용하기 : 정수 시퀀스 생성
#
# print(range(1,10))
# print(list(range(1,10))) # range 객체를 리스트로 변환

# 1~10까지 출력하기

for i in range(1, 10+1):
    print(i, end = ',')
print('') # end 초기화용 코드

for _ in range (1,6):
    print('Hello World!!')