# 파일 읽기 처리 함수 비교
# read() : 파일 전체를 문자열로 읽어들임
# readline() : 파일에서 한 줄씩 문자열로 읽어들임
# csv.reader : 파일 객체 직접 전달해서 자동으로 줄 단위로 읽음

# 파이썬에서 파일 입출력을 안정하고 간편하게 처리하기
# with open(파일명, 모드, 인코딩) as f
# with 블록이 끝나면 자동으로 f.close() 해줌

# import csv
#
# fname = 'summermedals.csv'
# result = ''
#
# with open(fname, 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f) # csv.reader 가 파일 전체를 읽음
#     for items in reader:
#         result += f'{items[0]} {items[1]} {items[2]} {items[4]} {items[5]} {items[8]} \n'
#
# print(result)

# 파일 쓰기 4
# 사용자로부터 이름, 이메일, 주소 등을 입력받아 persons.csv 로 저장

# name = 'abc123'
# email = '987xyz@abc123.co.kr'
# addr = '서울 광진구 자양 1동 321-123'
#
# fname = 'persons.csv'
# with open (fname, 'a', encoding = 'utf-8') as f:
#     row = f'{name}, {email}, {addr} \n'
#     f.write(row)

# 파일 쓰기 5
# 사용자로부터 이름, 이메일, 주소 등을 입력받아 persons2.csv 로 저장
# 단, 이름 입력 시 성과 이름을 ,로 구분해서 입력 받도록 함
# 입력을 종료하려면 exit를 입력하도록 작성

# fname = 'persons2.csv'
#
# while True:
#     cont = input('입력을 하시겠습니까? (start/exit)')
#     if cont == 'exit': break
#
#     name = input("이름 ('성,이름'을 입력하세요) : ")
#     email = input('이메일 : ')
#     addr = input('주소 : ')
#
#     with open (fname, 'a', encoding = 'utf-8') as f:
#         row = f'"{name}", {email}, {addr} \n'
#         f.write(row)

# TEXT vs JSON
# JSON : javascript object notation
# 자바 스크립트 객체 표기법에서 나온 데이터 표현 형식
# -> 지금은 자바, c#, go, 스위프트 등 다양한 프로그래밍 언어에서 사용
# 사람이 읽기 쉽고 , 프로그램도 읽기 쉬운 구조화 된 텍스트 데이터 형식

# text : 입력받은 내용을 모두 문자열로 취급해 파일에 저장
#        -> 데이터의 의미를 프로그램이 파악하기 어려움
#        구조 파악 어려움 : split 함수를 이용해서 구조 해석
# JSON : 키-값 구조로 데이터 저장 (딕셔너리-리스트 구조)
#        데이터를 구조화해서 저장 가능
#        -> 데이터의 형식이나 의미 유지 - 프로그램이 파악 가능

person = {
    "name" : "혜교", "email" : "abc123@zbc123.co.kr",
    "addr" : "서울 광진구 자양동 123-321"
}

# JSON 파일 저장 : dump(데이터, 파일 객체)
import json
with open('person.json', 'w', encoding = 'utf-8') as f:
    json.dump(person, f, ensure_ascii = False)

# JSON 파일 읽기 : load(파일 객체)
with open('person.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)
print(data) # dict 형식으로 출력