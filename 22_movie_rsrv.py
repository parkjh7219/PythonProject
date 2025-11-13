# seats = [
#     ['○','○','○','○','○'],
#     ['○','○','○','○','○'],
#     ['○','○','○','○','○'],
#     ['○','○','○','○','○'],
#     ['○','○','○','○','○']
# ]
# while True:
#
#     row = input('몇 행 좌석을 예약하시겠어요? 행(A~E) 입력 : ')
#     column = int(input('몇 열 좌석을 예약하시겠어요? 열(1~5) 입력 : '))
#
#     match row:
#         case 'A':
#             if 1 <= column <= 5:
#                 for i in range(1,6):
#                     if column == i:
#                         if seats[0][i-1] == 'X':
#                             print('이미 예약된 좌석입니다')
#                         else: seats[0][i-1] = 'X'
#             else:
#                 print('열 번호를 잘못 입력하셨습니다.')
#         case 'B':
#             if 1 <= column <= 5:
#                 for i in range(1,6):
#                     if column == i:
#                         if seats[1][i-1] == 'X':
#                             print('이미 예약된 좌석입니다')
#                         else: seats[1][i-1] = 'X'
#             else:
#                 print('열 번호를 잘못 입력하셨습니다.')
#         case 'C':
#             if 1 <= column <= 5:
#                 for i in range(1,6):
#                     if column == i:
#                         if seats[2][i-1] == 'X':
#                             print('이미 예약된 좌석입니다')
#                         else: seats[2][i-1] = 'X'
#             else:
#                 print('열 번호를 잘못 입력하셨습니다.')
#         case 'D':
#             if 1 <= column <= 5:
#                 for i in range(1,6):
#                     if column == i:
#                         if seats[3][i-1] == 'X':
#                             print('이미 예약된 좌석입니다')
#                         else: seats[3][i-1] = 'X'
#             else:
#                 print('열 번호를 잘못 입력하셨습니다.')
#         case 'E':
#             if 1 <= column <= 5:
#                 for i in range(1,6):
#                     if column == i:
#                         if seats[4][i-1] == 'X':
#                             print('이미 예약된 좌석입니다')
#                         else: seats[4][i-1] = 'X'
#             else:
#                 print('열 번호를 잘못 입력하셨습니다.')
#         case _:
#             print('행 번호를 잘못 입력하셨습니다')
#     for A, B, C, D, E in seats: # 언패킹으로 출력하면 리스트 구조가 나오기 때문에
#         print(A,B,C,D,E)        # for 문으로 언패킹을 풀어야 함
#                                 # 접근 방식 자체가 잘못 된 것 같음
#
#     cont =input('종료를 원하시면 quit를 입력해주세요 : ')
#     if cont == 'quit':
#         break



seats = []

# 반복문으로 좌석 만들기
for i in range(5): 
    row = []
    for j in range(5):
        row.append('○')
    seats.append(row)

# 예약 확인
result= '   1  2  3  4  5\n'
for j in range(5):
    result += f'{chr(65+j):3s}' # 아스키 코드로 변환 # 8번 이그잼 25번
    for i in range(5):
        result+= f'{seats[j][i]:3s}'
    result += '\n'
print(f'\n{result}')

# 예약 여부 입력 받음 (지정한 값 이외의 문자가 입력될 때 x)
rsrv_row = input('몇 행 좌석을 예약하시겠어요? 행(A~E) 입력 : ').upper() # 대문자 변환
rsrv_col = input('몇 열 좌석을 예약하시겠어요? 열(1~5) 입력 : ')

# 좌석 예약 처리 (이미 예약된 좌석이면 x)
posx = ord(rsrv_row) -65 # ABCDE 를 받아서 01234로 바꿈 (행 수)
posy = int(rsrv_col) -1
seats[posx][posy] = 'X'

# 처리 완료 메세지 출력
print(f'{rsrv_row}{rsrv_col} 좌석이 예약되었습니다 !')