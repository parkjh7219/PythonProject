# 데이터의 휘발성(volatile)
# 프로그램이 종료되면 데이터가 사라지는 특성
# 즉 메모리(램)에 저장된 데이터는 기본적으로 휘발성
# 변수 , 리스트 등은 메모리에 존재
# 속도가 빠른 장치 내에서 데이터 관리가 목적

# 데이터의 영속성(persistent)
# 프로그램이 종료되더라도 데이터가 유지되게 하는 특성
# 파일, 데이터베이스, 로그 등에 저장
# 속도가 느린 장치 내에서 데이터 저장이 목적

# 파이썬에서의 데이터 영속성 부여
# 텍스트 파일에 데이터 저장, JSON 저장(구조화 방식), 객체 저장, 로컬디비, 외부디비

# 텍스트 파일에 데이터 읽고 쓰기
# 파일 입출력(I/O)은 파일을 열고, 읽거나 쓰는 기능을 의미
# 텍스트 파일을 다루는 순서 : 파일 열기 - 파일 읽기/쓰기 - 파일 닫기

# 파일 쓰기 예제
# say = 'Hello World'
# f = open('hello.txt', 'w')
# f.write(say)
# f.close()

# 파일에 내용 추가
# 파일 쓰기 모드가 w인 경우 파일을 새로 생성해서 내용 저장
# say = 'Hello Python'
# f = open('hello.txt', 'w')
# f.write(say)
# f.close()

# 파일에 내용 추가 2
# 파일쓰기 모드가 a인 경우 기존 파일에 내용 추가
# say = 'Hello World '
# f = open('hello2.txt', 'w')
# f.write(say)
# f. close()
#
# say = 'Hello Python'
# f = open('hello2.txt', 'a')
# f.write(say)
# f.close()

# 파일에 내용 쓰기 3
# 키보드로 입력받은 내용을 파일에 저장
# 파일 저장 시 한글을 위해 인코딩 지정 필요 - encoding = '인코딩 방식'
# utf-8 : 전 세계 표준, 다국어 저장 지원
# euc-kr : 한국어 전용
# cp949 : 윈도우 한국어 전용 인코딩

# while True:
#     jmenu = input('오늘의 점심 메뉴를 입력하세요 (종료-q) : ')
#     if jmenu == 'q': break
#     f = open('lunch.txt', 'a', encoding='UTF-8')
#     f.write(f'{jmenu}\n')
#     f.close()

# 파일 읽기 1
# fname = 'hello.txt'
# f = open(fname, 'r')
# print(f.read()) # 파일의 전체 내용을 하나 읽어 화면에 출력
# f.close()

# 파일 읽기 2
# fname = 'hello2.txt'
# f = open(fname, 'r')
# print(f.read())
# f.close()

# 파일 읽기 3
# fname = 'lunch.txt'
# f = open(fname, 'r', encoding='UTF-8')
# print(f.read())
# f.close()

# 파일 읽기 4 - EMPLOYEES.csv
fname = 'EMPLOYEES.csv'
f = open(fname, 'r', encoding='UTF-8')
print(f.read())
f.close()

# 파일 읽기 5 - EMPLOYEES.csv
# print('-----------------')
# fname = 'EMPLOYEES.csv'
# result = ''
# f = open(fname, 'r', encoding='UTF-8')
# while True:
#     line = f.readline() # 텍스트 파일의 내용들 중 한 줄을 읽어와서
#     if line == '': break # 그 줄의 내용이 없다면 반복 중단
#     result += line
#
# f.close()
# print(result)

# 문자열에 split 함수 사용하기
# split : 문자열을 구분자 (delimeter) 기준으로 잘라서 리스트로 출력

# text = '김밥 라면 부찌 짱깨'
# result = text.split(' ')
# print(result)
# print(result[1] , result[3])

# 파일 읽기 6 - 사원 정보 중 사번, 성, 이메일, 입사일, 직책, 상사 번호, 부서번호만 출력
# print('-----------------')
# fname = 'EMPLOYEES.csv'
# result = ''
# f = open(fname, 'r', encoding='UTF-8')
# while True:
#     line = f.readline()
#     if line == '': break
#     fields = line.split(',') # ,로 문자열을 나눠 결과를 리스트에 저장
#     result += f'{fields[0]} {fields[2]} {fields[3]} {fields[5]} {fields[6]} {fields[9]}  {fields[10]} \n'

# f.close()
# print(result)

# # 파일 읽기 7 = summermedals.csv
# fname = 'summermedals.csv'
# f = open(fname, 'r', encoding='UTF-8')
# print(f.read())
# f.close()

# 파일 읽기 8 - 올림픽 정보 중 년도, 개최지, 종목명, 선수명, 메달만 출력

# print('-----------------')
# fname = 'summermedals.csv'
# result = ''
# f = open(fname, 'r', encoding='UTF-8')
# while True:
#     line = f.readline()
#     if line == '': break
#     fields = line.split(',') # ,로 문자열을 나눠 결과를 리스트에 저장
#     if len(fields) == 10:
#         result += f'{fields[0]} {fields[1]} {fields[2]} {fields[4]} {fields[5]} {fields[6]} {fields[9]} \n'
#     elif len(fields) == 9:
#         result += f'{fields[0]} {fields[1]} {fields[2]} {fields[4]} {fields[5]} {fields[8]} \n'
#     elif len(fields) == 11:
#         result += f'{fields[0]} {fields[1]} {fields[2]} {fields[4]} {fields[5]} {fields[8]} \n'
# f.close()
# print(result)

# split 함수는 인용부호 안에 , 가 포함된 경우 문자열을 적절히 분리하지 못함
# 이런 경우 , csv 라는 외부 모듈을 이용하는 것이 좋음
# import csv
#
# text = '김밥 라면 부찌 "짱깨 우동"'
# items = text.split()
# print(items)
#
# item = next(csv.reader([text], delimiter = ' '))
# print(item)

# 파일 읽기 9 - 올림픽 정보 중 년도, 개최지, 종목명, 선수명, 메달만 출력

import csv

print('-----------------')
fname = 'summermedals.csv'
result = ''
f = open(fname, 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line : break # 조금 더 세련되게 코드 작성

    fields =  next(csv.reader([line]))
    result += f'{fields[0]} {fields[1]} {fields[2]} {fields[4]} {fields[5]} {fields[8]} \n'

f.close()
print(result)