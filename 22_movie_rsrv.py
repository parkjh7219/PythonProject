seats = [
    ['○','○','○','○','○'],
    ['○','○','○','○','○'],
    ['○','○','○','○','○'],
    ['○','○','○','○','○'],
    ['○','○','○','○','○']
]
while True:

    row = input('몇 행 좌석을 예약하시겠어요? 행(A~E) 입력 : ')
    column = int(input('몇 열 좌석을 예약하시겠어요? 열(1~5) 입력 : '))

    match row:
        case 'A':
            if 1 <= column <= 5:
                for i in range(1,6):
                    if column == i:
                        if seats[0][i-1] == 'X':
                            print('이미 예약된 좌석입니다')
                        else: seats[0][i-1] = 'X'
            else:
                print('열 번호를 잘못 입력하셨습니다.')
        case 'B':
            if 1 <= column <= 5:
                for i in range(1,6):
                    if column == i:
                        if seats[1][i-1] == 'X':
                            print('이미 예약된 좌석입니다')
                        else: seats[1][i-1] = 'X'
            else:
                print('열 번호를 잘못 입력하셨습니다.')
        case 'C':
            if 1 <= column <= 5:
                for i in range(1,6):
                    if column == i:
                        if seats[2][i-1] == 'X':
                            print('이미 예약된 좌석입니다')
                        else: seats[2][i-1] = 'X'
            else:
                print('열 번호를 잘못 입력하셨습니다.')
        case 'D':
            if 1 <= column <= 5:
                for i in range(1,6):
                    if column == i:
                        if seats[3][i-1] == 'X':
                            print('이미 예약된 좌석입니다')
                        else: seats[3][i-1] = 'X'
            else:
                print('열 번호를 잘못 입력하셨습니다.')
        case 'E':
            if 1 <= column <= 5:
                for i in range(1,6):
                    if column == i:
                        if seats[4][i-1] == 'X':
                            print('이미 예약된 좌석입니다')
                        else: seats[4][i-1] = 'X'
            else:
                print('열 번호를 잘못 입력하셨습니다.')
        case _:
            print('행 번호를 잘못 입력하셨습니다')

    for A, B, C, D, E in seats:
      print(A,B,C,D,E)

    cont =input('종료를 원하시면 quit를 입력해주세요 : ')
    if cont == 'quit':
        break