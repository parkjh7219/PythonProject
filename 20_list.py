# # 시퀀스 자료형
# # 값들이 일정한 순서를 가지고 나열된 형태의 자료구조
#     # 자료구조
#     # 데이터를 효율적으로 저장하고 관리 활용하기 위한 방법, 구조
#     # 데이터는 어떻게 저장하고 , 어떻게 꺼내고, 지우고, 검색하는 것이 좋을까에 대해
#     # 연구하고 설계하는 학문
# # 여러 데이터를 순서대로 저장하고, 인덱스로 접근할 수 있음
# # 연산 기능 : 인덱싱, 슬라이싱, 반복, 길이, 멤버쉽 연산
# # 리스트, 튜플, 문자열
#
# # 리스트
# # 자료형(타입)이 동일한 여러 개의 데이터를 하나의 변수에 순서대로 저장할 수 있는 자료구조(상자)
# # 리스트는 []로 표현하고, 각 요소는 ,로 구분

# lunches = ['라면','김밥', '뚝불', '돈까스', '짜장면']
# # print(lunches)
# #
# # # 인덱싱
# # print(lunches[0], lunches[4])
# #
# # # 슬라이싱
# # print(lunches[0:3])
#
# # 요소 변경
# lunches[2] = '뚝배기 불고기'
# print(lunches)
#
# # 추가하기 : append, insert (위치, 값)
# lunches.append('짬뽕') # 맨 뒤에 추가
# print(lunches)
#
# lunches.insert(1,'떡볶이') # 숫자만 입력하고 콤마
# print(lunches)
#
# # 삭제하기 : pop , remove, del ,clear
# lunches.pop(3) # 4번째 엘리먼트 삭제 , 엘리먼트 - 리스트 안에 있는 요소 하나를 말함
# print(lunches)
#
# lunches.remove('김밥')
# print(lunches)
#
# lunches.clear()
# print(lunches)
#
# # 중첩 리스트 - 2차원 리스트, 다중 리스트 (중요)
persons = [
    ['혜교', '123-4567-8912', 'ab@abc.co.kr'],
    ['지현', '456-7891-2345', 'xy@xyz.co.kr']
]
#중첩 리스트에서의 인덱싱

# print(persons)
# print(persons[0])
# print(persons[1])
# print(persons[1][0], persons[1][2])

for i in range(2): # 반복문으로 persons 내용 출력
    for j in range(3):
        print (persons[i][j], end=' ')
print()

# 향상된 for 문 : for-each 문으로 persons 내용 출력 , 객체 즉 시퀀스 자료형일 때 사용 가능
for person in persons:
    for info in person:
        print(info, end=' ')
print()

# for-each + 언패킹 unpacking , 리스트의 구성 요소들 마다 변수를 선언한다고 이해하기
for name, phone, email in persons:
    print(name, phone, email, end=' ')


# 리스트 기타 함수
# print(persons) # sort 가 뭔지 잘 모르겠음
# persons.sort()
# print(persons)
#
# for person in persons:
#     print(person)
#     person.sort()
#     print(person)
#
# print(len(persons)) # 사람 수
# print(len(persons[0])) # 개인당 정보 수