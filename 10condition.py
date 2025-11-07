# 프로그램의 3대 논리 - 순차 조건 반복
# 순차 - 명령어를 위에서 아래로 순서대로 실행
# 선택 - 조건에 따라 실행할 명령어가 달라짐
# 반복 - 같은 명령어를 반복 수행

# 조건문
# 어떤 조건에 따라 프로그램 실행 흐름을 제어하는 문장
# 명령의 분기를 만드는 도구
# 파이썬에서는 if문을 통해 조건문을 작성

# 단순 if문
# if 조건식 :
#   참일 때 실행할 명령 , 들여쓰기 (tab) 하세요

# 블럭 block
# 여러 개의 명령문을 하나의 논리적 단위로 묶은 것
# 조건문 / 반복문에서 조건이 참일 때 실행할 코드들을 묶은 부분
# 즉, 여러 줄의 코드를 하나의 실행 단위로 만든 것
# 파이썬에서는 블록을 들여쓰기 (indent) 로 구분함

# ex) 시험 점수가 85점 이상이면 '합격'이라 출력

jumsu = 80
result = '불합격입니다 !!'

if jumsu >= 85:
    result = '합격입니다 !!'
       # result = '111'

print(result)

# ex 4-5

eve = float(input('Enter you score : '))
result1 = '해외 연수 기회 부여하지 않음'

if eve >= 4.2:
    result1 = '해외 연수 기회 부여'

print('당신의 평점은 : ',eve)
print(result1)

# 기본 if 문
# if 조건식 :
#   참일 때 실행할 명령
# else
#   거짓일 때 실행할 명령
#
# ex 4-7

age = int(input('나이를 입력하세요 :'))

if age >= 65:
    result2 = '지하철 경로우대 승차권 발급'
else:
    result2 = '지하철 일반 승차권 발급'

print(result2)
print('자동 발매기를 이용해주셔서 감사합니다')

# ex 4-8

num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

if num1 > num2:
    result = f'두 수 중에 큰 수는 {num1}이고 작은 수는 {num2}입니다.'
else:
    result = f'두 수 중에 큰 수는 {num2}이고 작은 수는 {num1}입니다.'

print(result)

# 다중 if 문
# if 조건식1 :
#    조건식1 이 참일 때 실행할 명령
# elif 조건식2 :
#      조건식2 가 참일 때 실행할 명령
# else 
#      그 외 조건일 때 실행할 명령

# ex) 4-7 두 개의 수를 입력받아 큰 수를 출력
# 단, 같은 수 2개를 입력했을 때


num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

if num1 > num2:
    result = f'두 수 중에 큰 수는 {num1}이고 작은 수는 {num2}입니다.'
elif num2 > num1:
    result = f'두 수 중에 큰 수는 {num2}이고 작은 수는 {num1}입니다.'
else:
    result = '입력한 두 수는 같습니다'

print(result)

# ex 4-9

num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

if num1 % 2 == 0 and num2 % 2 == 0:
    result = '두 숫자가 모두 짝수입니다'
elif num1 % 2 != 0 and num2 % 2 != 0:
    result = '두 숫자가 모두 홀수입니다'
else :
    result = '짝수와 홀수가 섞여 있습니다'

print(result)

# ex 4-10
# 
# sco = int(input('점수를 입력하세요 : '))
# 
# if sco >= 90:
#     result = 'A학점입니다.'
# 
# elif sco >= 80:
#     result = 'B학점입니다.'
# 
# elif sco >= 70:
#     result = 'C학점입니다.'
# 
# elif sco >= 60:
#     result = 'D학점입니다.'
# 
# else:
#     result = 'F학점입니다.'
# 
# print(result)

# 중첩 if 문 - if문 속에 또 다른 if문을 작성

# if 조건1 :
#   if 조건2 :
#       실행문1
#   else:
#       실행문2
# else:
#   실행문3

# ex) 두 개의 수를 입력받아 큰 수를 출력
# 단, 음수 입력 시 양수만 입력하세요라고 하고 종료

num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

if num1 > 0 and num2 > 0:
    if num1 % 2 == 0 and num2 % 2 == 0:
        result = '두 숫자가 모두 짝수입니다'

    elif num1 % 2 != 0 and num2 % 2 != 0:
        result = '두 숫자가 모두 홀수입니다'
    else :
        result = '짝수와 홀수가 섞여 있습니다'

else:
    result = '양수만 입력하세요'

print(result)

# ex 4-10 b
# 단 입력한 점수가 100을 초과하면
# '점수를 잘못 입력하셨습니다!' 라고 출력하고 종료

sco = int(input('점수를 입력하세요 : '))

if sco <= 100 :
    if sco >= 90 and sco > 0:
        result = 'A학점입니다.'

    elif sco >= 80:
        result = 'B학점입니다.'

    elif sco >= 70:
        result = 'C학점입니다.'

    elif sco >= 60:
        result = 'D학점입니다.'

    else:
        result = 'F학점입니다.'
else:
    result = '점수를 잘못 입력하셨습니다!'

print(result)

# 문자열 비교
# == , != : 문자열 내용과 생성된 메모리 위치 비교
# >, <, >=, <= : 문자열을 사전순(유니코드 순서)으로 비교

print('a' > 'A') # a : 97, A : 65
print('*' < 'k') # * : 42, k : 107
print('김' < '강') # 김 : 44608, 강 : 44053
print('cskim' < 'CSKIM') # c : 99, C : 67

print('John' < 'Joho') # n : 110, o : 111
print('홍길덩' < '홍길딩') # 덩 : 46020, 딩 : 46308


# 대소문자 구분없이 비교

print('cskim' < 'CSKIM'.lower())
print('cskim'.upper() < 'CSKIM')

# ex 4-14

# 처리 
# gender = gender.upper() # 대문자변환
# is_valid_gender = gender == 'F' or gender == 'M'

# if is_valid_gender:

gen = input ("성별 입력('M or m' 또는 'F or f')")
sta = int (input('키 입력(cm)'))
wei = int (input('몸무게 입력(kg)'))

if gen == 'M' or gen ==  'm':
    Rw = float(sta * sta * 22) /10000
    per = wei / Rw * 100
    if 110 <= per <= 119:
        result = '과체중'
    elif per >= 120:
        result = '비만 체중'
    else:
        result = '정상체중'

elif gen == 'F' or  gen == 'f':
    Rw = float(sta * sta * 21)/10000
    per = wei / Rw * 100
    if 110 <= per <= 119:
        result = '과체중'
    elif per >= 120:
        result = '비만 체중'
    else:
        result = '정상체중'

else:
    result = '성별 입력이 잘못 되었습니다.'

print(result) # 같은 코드를 두번 적는건 안좋은방법


# match / case 문
# python 3.10 부터 새롭게 추가된 조건 판별 구문
# if 문은 조건식 결과가 참/거짓 여부에 따라 분기했었음
# 반면에 match/case 문은 값이나 패턴에 따라 분기함

# match 변수 :
# case 값 1:
#   실행문 1

# case 값 2:
#   실행문 2

# case 값 _:
#   실행문 3

# if vs match
# (복잡한)조건판단 : if
# 값 / 패턴 비교 : match case

#
# ex 4-10 c
# 단 입력한 점수가 100을 초과하면
# '점수를 잘못 입력하셨습니다!' 라고 출력하고 종료
# 학점 처리 부분을 match/case로 작성ㅈ

#     match jumsu:
#         case 100 | 99 | 98 | 97 | 96 | 95 | 94 | 93 | 92 | 91 | 90:  # or 패턴
#             grade = 'A학점입니다'
#        case x if 80 <= x < 90:
#             grade = 'B학점입니다'
#         case 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 | 70:
#             grade = 'C학점입니다'
#         case 69 | 68 | 67 | 66 | 65 | 64 | 63 | 62 | 61 | 60:
#             grade = 'D학점입니다'
#         case _:
#             grade = 'F학점입니다'


jumsu = int(input('점수를 입력하세요 : '))

if 0 <= jumsu <= 100:
    match jumsu // 10:
        case 100 | 9: # or 패턴
            result = 'A학점입니다.'
        case 8:
            result = 'B학점입니다.'
        case 7:
            result = 'C학점입니다.'
        case 6:
            result = 'D학점입니다.'
        case _:
            result = 'F학점입니다.'

else:
    result = '잘못~'

print(result)

# ex ) 1 부터 50까지 총합을 구하는 코드 작성

# 가우스 공식을 이용하면 빠르게 계산 가능
